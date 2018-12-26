import re
import sys
import time
from PIL import Image, ImageDraw

sys.setrecursionlimit(3000)


class Clay_Bar:
    def __init__ (self, line):
        numbers = re.findall(r"\d+",line)
        if line[0] == "x":
            self.x_low = int(numbers[0])
            self.x_hi = int(numbers[0])
            self.y_low = int(numbers[1])
            self.y_hi = int(numbers[2])
        else:
            self.y_low = int(numbers[0])
            self.y_hi = int(numbers[0])
            self.x_low = int(numbers[1])
            self.x_hi = int(numbers[2])
    def __str__ (self):
        return str(vars(self))
        # print vars(self)

SPRING = 0
SAND = 1
CLAY = 2
FLOWING = 3
STANDING = 4
input_file = 'Day 17\\Day 17 Input.txt'
output_file = 'Day 17\\test.png'

grid_rep = {
    SPRING: "+",
    SAND: ".",
    CLAY: "#",
    FLOWING: "|",
    STANDING: "~"
}

def print_grid(grid):
    for y in sorted(grid.iterkeys()):
        grid_line = ""
        for x in sorted(grid[y].iterkeys()):
            grid_line += grid_rep[grid[y][x]]
        print grid_line
    
def image_grid(grid, bounds):
    sand = (194, 178, 128)
    flowing = (0, 0, 255)
    standing = (0, 255, 255)
    clay = (153, 0, 0)
    spring = (5, 91, 61)
    width = bounds['x_hi'] - bounds['x_low']+2
    height = bounds['y_hi']+1
    img = Image.new('RGB', (width, height), color = sand)
    dr = ImageDraw.Draw(img)
    for y in grid:
        for x in grid[y]:
            real_x = x - bounds['x_low']
            if y == 0 and x == 500:
                dr.rectangle(((real_x-1,y),(real_x+1,y)),fill=spring)
            elif grid[y][x] == CLAY:
                dr.rectangle(((real_x,y),(real_x,y)),fill=clay)
            elif grid[y][x] == FLOWING:
                dr.rectangle(((real_x,y),(real_x,y)),fill=flowing)
            elif grid[y][x] == STANDING:
                dr.rectangle(((real_x,y),(real_x,y)),fill=standing)
    img.save(output_file)

text_file = open(input_file)
lines = text_file.read().split('\n')

clay_bars = []
for line in lines:
    clay_bars.append(Clay_Bar(line))

bounds = {
    'x_low': clay_bars[0].x_low,
    'x_hi': clay_bars[0].x_hi,
    'y_low': clay_bars[0].y_low,
    'y_hi': clay_bars[0].y_hi
}
for clay_bar in clay_bars:
    if clay_bar.x_low < bounds["x_low"]:
        bounds["x_low"] = clay_bar.x_low
    if clay_bar.x_hi > bounds["x_hi"]:
        bounds["x_hi"] = clay_bar.x_hi
    if clay_bar.y_hi > bounds["y_hi"]:
        bounds["y_hi"] = clay_bar.y_hi
    if clay_bar.y_low < bounds["y_low"]:
        bounds["y_low"] = clay_bar.y_low

grid = {}

#Set up grid with sand, spring and clay bars
for y in range(0,bounds['y_hi']+1):
    grid[y] = {}
    for x in range(bounds['x_low']-1,bounds['x_hi']+2):
        grid[y][x] = SAND
grid[0][500] = SPRING
for clay_bar in clay_bars:
    for y in range(clay_bar.y_low, clay_bar.y_hi + 1):
        for x in range(clay_bar.x_low, clay_bar.x_hi + 1):
            grid[y][x] = CLAY

def spread_left(x,y):
    while grid[y+1][x] != SAND and grid[y][x] != CLAY:
        x-=1
    return x

def spread_right(x,y):
    while grid[y+1][x] != SAND and grid[y][x] != CLAY:
        x+=1
    return x

def spread_out(x,y):
    left = spread_left(x,y)
    right = spread_right(x,y)
    water_type = STANDING
    if grid[y][left] != CLAY or grid[y][right] != CLAY:
        water_type = FLOWING
    for x2 in range(left+1, right):
        if grid[y][x2] != CLAY:
            grid[y][x2] = water_type
    if grid[y][left] != CLAY:
        waterfall(left,y)
    if grid[y][right] != CLAY:
        waterfall(right,y)
    

def waterfall(x,y):
    if y+1 in grid:
        if grid[y+1][x] == FLOWING:
            grid[y][x] = FLOWING
        else:
            if grid[y+1][x] == SAND:
                grid[y][x] = FLOWING
                waterfall(x,y+1)
            elif grid[y+1][x] == CLAY:
                spread_out(x,y)
            if grid[y+1][x] == STANDING:
                spread_out(x,y)
    else:
        grid[y][x] = FLOWING

waterfall(500,0)

image_grid(grid,bounds)

water_p1 = 0
water_p2 = 0
for y in grid:
    for x in grid[y]:
        if y >= bounds['y_low'] and (grid[y][x] == FLOWING or grid[y][x] == STANDING):
            water_p1 = water_p1 + 1
        if y >= bounds['y_low'] and grid[y][x] == STANDING:
            water_p2 = water_p2 + 1

print "Part 1: " + str(water_p1)
print "Part 2: " + str(water_p2)
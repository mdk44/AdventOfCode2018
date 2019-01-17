from PIL import Image, ImageDraw

input_file = 'Day 13\\Day 13 Test.txt'
# input_file = 'Day 13\\Day 13 Input.txt'
input_track = 'Day 13\\Day 13 Test Track.txt'
# input_track = 'Day 13\\Day 13 Input Track.txt'
output_file = 'Day 13\\test.png'
text_file = open(input_file)
track_file = open(input_track)
lines = text_file.read().split('\n')
lines2 = track_file.read().split('\n')

def print_grid(grid):
    for y in sorted(grid.iterkeys()):
        grid_line = ""
        for x in sorted(grid[y].iterkeys()):
            grid_line += grid[y][x]
        print grid_line

def image_grid(grid):
    other = (226, 232, 148)
    track = (0, 0, 0)
    cart = (47, 191, 239)
    crash = (239, 47, 232)
    width = (len(lines[0]) + 1 ) * 2
    height = (len(lines) + 1 ) * 2
    img = Image.new('RGB', (width, height), color = other)
    dr = ImageDraw.Draw(img)
    for y in grid:
        for x in grid[y]:
            real_x = 2 * x + 1
            real_y = 2 * y + 1
            if  grid[y][x] == '|':
                dr.rectangle(((real_x,real_y),(real_x,real_y+1)),fill=track)
            elif grid[y][x] == '-':
                dr.rectangle(((real_x,real_y),(real_x+1,real_y)),fill=track)
            elif grid[y][x] == '+':
                dr.rectangle(((real_x,real_y),(real_x + 1,real_y)),fill=track)
                dr.rectangle(((real_x,real_y),(real_x,real_y + 1)),fill=track)
            elif grid[y][x] == '/':
                if y + 1 in grid and (grid[y + 1][x] == '|' or grid[y + 1][x] == '+' or grid[y + 1][x] == '>' or grid[y + 1][x] == '<' or grid[y + 1][x] == '^' or grid[y + 1][x] == 'v'):
                    dr.rectangle(((real_x,real_y),(real_x + 1,real_y)),fill=track)
                    dr.rectangle(((real_x,real_y),(real_x,real_y + 1)),fill=track)
                else:
                    dr.rectangle(((real_x,real_y),(real_x,real_y)),fill=track)
            elif grid[y][x] == '\\':
                if y + 1 in grid and (grid[y + 1][x] == '|' or grid[y + 1][x] == '+' or grid[y + 1][x] == '>' or grid[y + 1][x] == '<' or grid[y + 1][x] == '^' or grid[y + 1][x] == 'v'):
                    dr.rectangle(((real_x,real_y),(real_x,real_y + 1)),fill=track)
                else:
                    dr.rectangle(((real_x,real_y),(real_x + 1,real_y)),fill=track)
            elif grid[y][x] == '>' or grid[y][x] == '<' or grid[y][x] == '^' or grid[y][x] == 'v':
                dr.rectangle(((real_x,real_y),(real_x,real_y)),fill=cart)
                if x + 1 in grid and grid[y][x+1] != ' ':
                    dr.rectangle(((real_x + 1,real_y),(real_x + 1,real_y)),fill=track)
                if y + 1 in grid and grid[y+1][x] != ' ':
                    dr.rectangle(((real_x,real_y + 1),(real_x,real_y + 1)),fill=track)
            elif grid[y][x] == 'X':
                dr.rectangle(((real_x,real_y),(real_x,real_y)),fill=crash)
                if x + 1 in grid and grid[y][x+1] != ' ':
                    dr.rectangle(((real_x + 1,real_y),(real_x + 1,real_y)),fill=track)
                if y + 1 in grid and grid[y+1][x] != ' ':
                    dr.rectangle(((real_x,real_y + 1),(real_x,real_y + 1)),fill=track)
    img.save(output_file)

def move_right(x, y, curr_cart, curr_dir):
    if x + 1 in curr_grid:
        if curr_grid[y][x+1] == '-':
            curr_grid[y][x+1] = '>'
            curr_grid[y][x] = grid_track[y][x]
            curr_cart = '>'
        elif curr_grid[y][x+1] == '\\':
            curr_grid[y][x+1] = 'v'
            curr_grid[y][x] = grid_track[y][x]
            curr_cart = 'v'
        elif curr_grid[y][x+1] == '/':
            curr_grid[y][x+1] = '^'
            curr_grid[y][x] = grid_track[y][x]
            curr_cart = '^'
        elif curr_grid[y][x+1] == '+':
            curr_grid[y][x] = grid_track[y][x]
            if curr_dir == 'L':
                curr_grid[y][x+1] = '^'
                curr_cart = '^'
                curr_dir = 'S'
            elif curr_dir == 'S':
                curr_grid[y][x+1] = '>'
                curr_cart = '>'
                curr_dir = 'R'
            elif curr_dir == 'R':
                curr_grid[y][x-1] = 'v'
                curr_cart = 'v'
                curr_dir = 'L'
    return curr_cart, curr_dir

carts = 0
cart = []
curr_grid = {}
for y in range(0,len(lines)):
    curr_grid[y] = {}
    for x in range(0,len(lines[0])):
        curr_grid[y][x] = lines[y][x]
        if curr_grid[y][x] == '>' or curr_grid[y][x] == '<' or curr_grid[y][x] == '^' or curr_grid[y][x] == 'v':
            carts += 1
            cart.append(curr_grid[y][x])

grid_track = {}
for y in range(0,len(lines2)):
    grid_track[y] = {}
    for x in range(0,len(lines2[0])):
        grid_track[y][x] = lines2[y][x]

print "Initial Grid:"
print_grid(curr_grid)
image_grid(curr_grid)

cart_dir = []
for i in range(0,len(cart)):
    cart_dir.append('L')

print cart
print cart_dir

print 'Track:'
print_grid(grid_track)

for y in curr_grid:
    for x in curr_grid[y]:
        if curr_grid[y][x] == '>':
            cart[0],cart_dir[0] = move_right(x, y, cart[0], cart_dir[0])

print "New Grid:"
print_grid(curr_grid)
print cart
print cart_dir
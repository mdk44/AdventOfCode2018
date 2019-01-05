from PIL import Image, ImageDraw

input_file = 'Day 13\\Day 13 Test.txt'
# input_file = 'Day 13\\Day 13 Input.txt'
output_file = 'Day 13\\test.png'
text_file = open(input_file)
lines = text_file.read().split('\n')

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
    img.save(output_file)

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

print "Initial Grid:"
print_grid(curr_grid)
image_grid(curr_grid)

cart_dir = []
for i in range(0,len(cart)):
    cart_dir.append('L')

print cart
print cart_dir
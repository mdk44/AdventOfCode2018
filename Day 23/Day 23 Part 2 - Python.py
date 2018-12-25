# Day 23, Part 2

import re
import sys

class Data_Read:
    def __init__ (self, line):
        numbers = re.findall(r"[+-]?\d+(?:\.\d+)?",line)
        self.x = long(numbers[0])
        self.y = long(numbers[1])
        self.z = long(numbers[2])
        self.r = long(numbers[3])
        # print vars(self)
    def __str__ (self):
        return str(vars(self))

input_file = 'Day 23\\Day 23 Input.txt'
output_file = 'Day 23\\test.png'

text_file = open(input_file)
lines = text_file.read().split('\n')

input_data = []
for line in lines:
    input_data.append(Data_Read(line))

maxR = input_data[0].r
minX = minY = minZ = 1000
maxX = maxY = maxZ = 0
posRx = posRy = posRz = 0

for line_input in input_data:
    if line_input.r > maxR:
        maxR = line_input.r
    if line_input.x < minX:
        minX = line_input.x
    if line_input.y < minY:
        minY = line_input.y
    if line_input.z < minZ:
        minZ = line_input.z
    if line_input.x > maxX:
        maxX = line_input.x
    if line_input.y > maxY:
        maxY = line_input.y
    if line_input.z > maxZ:
        maxZ = line_input.z

man_dist = 0
max_count = 0
final_man_dist = 0
new_man_dist = 0
min_man_dist = 10000000

for x2 in range(minX, maxX):
    for y2 in range(minY, maxY):
        for z2 in range(minZ, maxZ):
            range_num =  0
            for line_input in input_data:
                man_dist = abs(x2 - line_input.x) + abs(y2 - line_input.y) + abs(z2 - line_input.z)
                if man_dist <= line_input.r:
                    range_num += 1
            if range_num >= max_count:
                new_man_dist = abs(x2) + abs(y2) + abs(z2)
                if new_man_dist < min_man_dist:
                    posRx = x2
                    posRy = y2
                    posRz = z2
                max_count = range_num
                

final_man_dist = abs(posRx) + abs(posRy) + abs(posRz)

print "Part 2: " + str(final_man_dist)
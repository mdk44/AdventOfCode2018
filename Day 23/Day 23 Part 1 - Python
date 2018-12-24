# Day 23, Part 1

import re
import sys
import time
from PIL import Image, ImageDraw

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
posRx = 0
posRy = 0
posRz = 0
for line_input in input_data:
    if line_input.r > maxR:
        maxR = line_input.r
        posRx = line_input.x
        posRy = line_input.y
        posRz = line_input.z

man_dist = 0
range = 0
for line_input in input_data:
    man_dist = abs(posRx - line_input.x) + abs(posRy - line_input.y) + abs(posRz - line_input.z)
    if man_dist <= maxR:
        range += 1

print "Part 1: " + str(range)
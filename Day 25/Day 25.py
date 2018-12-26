# Day 25

import re
import sys

class Data_Read:
    def __init__ (self, line):
        numbers = re.findall(r"[+-]?\d+(?:\.\d+)?",line)
        self.x = long(numbers[0])
        self.y = long(numbers[1])
        self.z = long(numbers[2])
        self.aa = long(numbers[3])
        # print vars(self)
    def __str__ (self):
        return str(vars(self))

input_file = 'Day 25\\Day 25 Test 0.txt'

text_file = open(input_file)
lines = text_file.read().split('\n')

input_data = []
for line in lines:
    input_data.append(Data_Read(line))

for line in lines:
    print line
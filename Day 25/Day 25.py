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

input_file = 'Day 25\\Day 25 Test 3.txt'

text_file = open(input_file)
lines = text_file.read().split('\n')

inp = []
for line in lines:
    inp.append(Data_Read(line))

constellation = 0
point = 0

c = 0
d = 1
point = 0
const = 0
no_const = 0

def man_dist(p1, p2):
    p1x = inp[p1].x
    p1y = inp[p1].y
    p1z = inp[p1].z
    p1aa = inp[p1].aa
    p2x = inp[p2].x
    p2y = inp[p2].y
    p2z = inp[p2].z
    p2aa = inp[p2].aa
    dist = abs(p1x - p2x) + abs(p1y - p2y) + abs(p1z - p2z) + abs(p1aa - p2aa)
    return dist

const = {}
for c in range(0,len(inp)):
    const[c] = 0
    
point = 1
const[0] = 1

for d in range(0,len(inp)):
    added = False
    for c in range(0,len(inp)):
        if c != d:
            if const[c] != 0 and const[d] == 0 and man_dist(c,d) <= 3:
                const[d] = const[c]
                added = True
            if const[d] != 0 and const[c] == 0 and man_dist(c,d) <= 3:
                const[c] = const[d]
                added = True
    if added == False:
        if const[d] == 0:
            const[d] = point
            point += 1

print "Part 1: " + str(point) + " constellations"

for c in range(0,len(inp)):
    print str(inp[c]) + " " + str(const[c])
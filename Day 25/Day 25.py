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

# input_file = 'Day 25\\Day 25 Test 0.txt'
# Answer should be 2 -- CORRECT
# input_file = 'Day 25\\Day 25 Test 1.txt'
# Answer should be 4 -- CORRECT
# input_file = 'Day 25\\Day 25 Test 2.txt'
# Answer should be 3 -- CORRECT
# input_file = 'Day 25\\Day 25 Test 3.txt'
# Answer should be 8 -- CORRECT
input_file = 'Day 25\\Day 25 Input.txt'
# Generated answer: 381 -- CORRECT

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

for d in range(0,len(inp)):
    if const[d] == 0:
        const[d] = point
        point += 1
    for c in range(d,len(inp)):
        if man_dist(c,d) <= 3:
            if const[c] != 0:
                old_const = const[d]
                for i in range(0,len(inp)):
                    if const[i] == old_const:
                        const[i] = const[c]
            else:
                const[c] = const[d]

unique_const = []
for i in range(0,len(inp)):
    if const[i] not in unique_const:
        unique_const.append(const[i])

print "Part 1: " + str(len(unique_const)) + " constellations"

# for c in range(0,len(inp)):
#     print str(inp[c].x) + " " + str(inp[c].y) + " " + str(inp[c].z) + " " + str(inp[c].aa) + "          " + str(const[c])
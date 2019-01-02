# Day 16

import re

input_file = 'Day 16\\Day 16 Test.txt'

text_file = open(input_file)
lines = text_file.read().split('\n')

def effect(fn):
    def new(before, instr):
        after = list(before)
        after[instr[3]] = fn(before, instr[1], instr[2])
        return after
    return new

def addr(before, instr):
    new_after = list(before)
    new_after[instr[3]] = before[instr[1]] + before[instr[2]]
    return new_after

def addi(before, instr):
    new_after = list(before)
    new_after[instr[3]] = before[instr[1]] + instr[2]
    return new_after

def mulr(before, instr):
    new_after = list(before)
    new_after[instr[3]] = before[instr[1]] * before[instr[2]]
    return new_after

muli = effect(lambda before,x,y: before[x]*y)
banr = effect(lambda before,x,y: before[x] & before[y])
bani = effect(lambda before,x,y: before[x] & y)
borr = effect(lambda before,x,y: before[x] | before[y])
bori = effect(lambda before,x,y: before[x] | y)
setr = effect(lambda before,x,y: before[x])
seti = effect(lambda before,x,y: x)
gtir = effect(lambda before,x,y: 1 if x > before[y] else 0)
gtri = effect(lambda before,x,y: 1 if before[x] > y else 0)
gtrr = effect(lambda before,x,y: 1 if before[x] > before[y] else 0)
eqir = effect(lambda before,x,y: 1 if x == before[y] else 0)
eqri = effect(lambda before,x,y: 1 if before[x] == y else 0)
eqrr = effect(lambda before,x,y: 1 if before[x] == before[y] else 0)

opcodes = []
    # addr, addi,
    # mulr, muli,
    # banr, bani,
    # borr, bori,
    # setr, seti,
    # gtir, gtri, gtrr,
    # eqir, eqri, eqrr

# options = {}
# for code in range(16):
#     options[code] = list(enumerate(opcodes))

# Part 1

ans = 0
for i in range(0, len(lines), 4):
    if 'Before' in lines[i]:
        before = map(int, re.findall(r'\d+', lines[i]))
        instr = map(int, re.findall(r'\d+', lines[i+1]))
        after = map(int, re.findall(r'\d+', lines[i+2]))
        opcodes[0] = addr(before, instr)
        opcodes[0] = addi(before, instr)
        print opcodes
        # options[instr[0]] = [(index,fn) for (index,fn) in options[instr[0]] if fn(before,instr) == after]

        # matches = 0
        # for index,fn in options[instr[0]]:
        #     if fn(before, instr) == after:
        #         matches += 1
        # if matches >= 3:
        #     ans += 1

print ans
print before
print instr
print after
# print matches
print addr(before, instr)
print addi(before, instr)


# for _ in range(16):
#     for code in range(16):
#         if len(options[code]) == 1:
#             for other_code in range(16):
#                 if other_code != code:
#                     options[other_code] = [(index,fn) for (index,fn) in options[other_code] if index!=options[code][0][0]]
        

# #for code in range(16):
# #    print code, options[code]

# registers = [0,0,0,0]
# for line in program.strip().split('\n'):
#     instr = map(int, re.findall('-?\d+', line))
#     old_registers = list(registers)
#     registers = options[instr[0]][0][1](registers, instr)
# print registers[0]
# Day 16

import re

input_file = 'Day 16\\Day 16 Input.txt'

text_file = open(input_file)
lines = text_file.read().split('\n')

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

def muli(before, instr):
    new_after = list(before)
    new_after[instr[3]] = before[instr[1]] * instr[2]
    return new_after

def banr(before, instr):
    new_after = list(before)
    new_after[instr[3]] = before[instr[1]] & before[instr[2]]
    return new_after

def bani(before, instr):
    new_after = list(before)
    new_after[instr[3]] = before[instr[1]] & instr[2]
    return new_after

def borr(before, instr):
    new_after = list(before)
    new_after[instr[3]] = before[instr[1]] | before[instr[2]]
    return new_after

def bori(before, instr):
    new_after = list(before)
    new_after[instr[3]] = before[instr[1]] | instr[2]
    return new_after

def setr(before, instr):
    new_after = list(before)
    new_after[instr[3]] = before[instr[1]]
    return new_after

def seti(before, instr):
    new_after = list(before)
    new_after[instr[3]] = instr[1]
    return new_after

def gtir(before, instr):
    new_after = list(before)
    if instr[1] > before[instr[2]]:
        new_after[instr[3]] = 1
    else:
        new_after[instr[3]] = 0
    return new_after

def gtri(before, instr):
    new_after = list(before)
    if before[instr[1]] > instr[2]:
        new_after[instr[3]] = 1
    else:
        new_after[instr[3]] = 0
    return new_after

def gtrr(before, instr):
    new_after = list(before)
    if before[instr[1]] > before[instr[2]]:
        new_after[instr[3]] = 1
    else:
        new_after[instr[3]] = 0
    return new_after

def eqir(before, instr):
    new_after = list(before)
    if instr[1] == before[instr[2]]:
        new_after[instr[3]] = 1
    else:
        new_after[instr[3]] = 0
    return new_after

def eqri(before, instr):
    new_after = list(before)
    if before[instr[1]] == instr[2]:
        new_after[instr[3]] = 1
    else:
        new_after[instr[3]] = 0
    return new_after

def eqrr(before, instr):
    new_after = list(before)
    if before[instr[1]] == before[instr[2]]:
        new_after[instr[3]] = 1
    else:
        new_after[instr[3]] = 0
    return new_after

opcodes = {
    0: addr,
    1: addi,
    2: mulr,
    3: muli,
    4: banr,
    5: bani,
    6: borr,
    7: bori,
    8: setr,
    9: seti,
    10: gtir,
    11: gtri,
    12: gtrr,
    13: eqir,
    14: eqri,
    15: eqrr
}


options = {}
for code in range(16):
    options[code] = list(enumerate(opcodes))

# Part 1

ans = 0
for i in range(0, len(lines), 4):
    if 'Before' in lines[i]:
        before = map(int, re.findall(r'\d+', lines[i]))
        instr = map(int, re.findall(r'\d+', lines[i+1]))
        after = map(int, re.findall(r'\d+', lines[i+2]))
        
        match = 0
        for c in opcodes:
            calc_after = opcodes[c](before, instr)
            if calc_after == after:
                match += 1
        if match > 2:
            ans += 1

print 'Part 1: ' + str(ans)

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
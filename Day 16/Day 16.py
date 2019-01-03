# Day 16

import re

input_file = 'Day 16\\Day 16 Input.txt'
input_file2 = 'Day 16\\Day 16 Input 2.txt'

text_file = open(input_file)
lines = text_file.read().split('\n')
text_file2 = open(input_file2)
lines2 = text_file2.read().split('\n')

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
    0: addr,  # 15
    1: addi,  # 12
    2: mulr,  # 7
    3: muli,  # 2
    4: banr,  # 1
    5: bani,  # 0
    6: borr,  # 13
    7: bori,  # 4
    8: setr,  # 3
    9: seti,  # 9
    10: gtir,  # 6
    11: gtri,  # 10
    12: gtrr,  # 8
    13: eqir,  # 14
    14: eqri,  # 11
    15: eqrr  # 5
}

# Part 1

ans = 0
known_codes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
for i in range(0, len(lines), 4):
    if 'Before' in lines[i]:
        before = map(int, re.findall(r'\d+', lines[i]))
        instr = map(int, re.findall(r'\d+', lines[i+1]))
        after = map(int, re.findall(r'\d+', lines[i+2]))
        
        match = 0
        code = []
        for c in opcodes:
            calc_after = opcodes[c](before, instr)
            if calc_after == after:
                match += 1
                if c not in known_codes:
                    code.append(c)
        if match > 2:
            ans += 1
        # Manually brute-forced finding each opcode's function and added the opcode index to known_codes to help find the next
        if len(code) == 1:
            print str(code) + ' ' + str(instr[0])

# Part 2

registers = [0, 0, 0, 0]
known_opcodes = {
    15: addr,
    12: addi,
    7: mulr,
    2: muli,
    1: banr,
    0: bani,
    13: borr,
    4: bori,
    3: setr,
    9: seti,
    6: gtir,
    10: gtri,
    8: gtrr,
    14: eqir,
    11: eqri,
    5: eqrr
}

c = 0
for i in range(0, len(lines2)):
    instr = map(int, re.findall(r'\d+', lines2[i]))
    old_registers = list(registers)
    c = instr[0]
    registers = known_opcodes[c](old_registers, instr)

print 'Part 1: ' + str(ans)
print 'Part 2: ' + str(registers[0])
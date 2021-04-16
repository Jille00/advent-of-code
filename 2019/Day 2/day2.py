import os
import numpy as np

def read_code(full_code):
	def read_intcode(code, full_code):
		if code[0] == 1: full_code[code[3]] = full_code[code[1]] + full_code[code[2]]
		elif code[0] == 2: full_code[code[3]] = full_code[code[1]] * full_code[code[2]]
		elif code[0] == 99: return True
		return False

	for i in range(0, len(full_code), 4):
		if read_intcode(full_code[i:i+4], full_code):
			break
	return full_code

def set_noun_verb(code, noun, verb):
	code[1:3] = [noun, verb]
	return code

def find_value(full_code, value):
	for noun in range(0,100):
		for verb in range(0,100):
			if read_code(set_noun_verb(full_code.copy(), noun, verb))[0] == value:
				return noun, verb

with open('day2.txt') as file:
    total_code = np.array([i for i in file.read().split(',')]).astype('int')

print("Part 1 is: ", read_code(set_noun_verb(total_code.copy(), 12, 2).copy())[0])
print("Part 2 is: ", find_value(total_code.copy(), 19690720))

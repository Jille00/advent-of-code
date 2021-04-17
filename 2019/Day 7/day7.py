import itertools
import numpy as np

class ReadCode:
	def __init__(self, total_code):
		self.index = 0
		self.index_update = {1:4, 2:4, 3:2, 4:2, 5:3, 6:3, 7:4, 8:4}
		self.output = []
		self.phase = None
		self.full_code = total_code

	def print_index(self):
		print(self.index)

	def read_code(self, amp, input_order):
		def read_intcode(code, full_code):
			def position_input(index):
				if par[index-1] == 0:
					return full_code[code[index]]
				return code[index]

			op = "0000" + str(code[0]) 
			opcode = int(op[-2:])
			par = [int(op[-3]),int(op[-4]),int(op[-5])]

			if opcode == 1: 
				full_code[code[3]] = position_input(1) + position_input(2)
			elif opcode == 2: 
				full_code[code[3]] = position_input(1) * position_input(2)
			elif opcode == 3: 
				if self.phase is None:
					self.phase = amp
					full_code[code[1]] = self.phase
				else:
					full_code[code[1]] = input_order
			elif opcode == 4: 
				self.output.append(position_input(1))
				self.index += self.index_update[opcode]
				return True, opcode, full_code
			elif opcode == 5:
				if position_input(1) != 0: self.index = position_input(2) - 3
			elif opcode == 6:
				if position_input(1) == 0: self.index = position_input(2) - 3
			elif opcode == 7:
				if position_input(1) < position_input(2): full_code[code[3]] = 1
				else: full_code[code[3]] = 0
			elif opcode == 8:
				if position_input(1) == position_input(2): full_code[code[3]] = 1
				else: full_code[code[3]] = 0
			elif opcode == 99: return True, opcode, full_code
			self.index += self.index_update[opcode]
			return False, opcode, full_code

		opcode = None
		for _ in range(0, len(self.full_code)):
			bo, opcode, full_code = read_intcode(self.full_code[self.index:self.index+4], self.full_code)
			self.full_code = full_code
			if bo:
				break
		return self.output, opcode

def run_phases(phases):
	def get_inputs(total_code, phase_setting):
		inputs = [0,0,0,0,0,0]
		readers = [ReadCode(total_code.copy()) for i in range(len(phase_setting))]
		while True:
			for index, i in enumerate(phase_setting):
				output, opcode = readers[index].read_code(i, inputs[index])
				inputs[index+1] = output[-1]
				if index == 4:
					inputs[0] = output[-1]
					if opcode == 99:
						return inputs

	outputs = []
	for phase_setting in itertools.permutations(phases, 5):
		inputs = get_inputs(total_code, phase_setting)
		outputs.append(inputs[-1])
	return np.max(outputs)

with open('day7.txt') as file:
    total_code = [int(i) for i in file.read().split(',')]

print("Part 1 is: ", run_phases([0,1,2,3,4]))
print("Part 2 is: ", run_phases([5,6,7,8,9]))
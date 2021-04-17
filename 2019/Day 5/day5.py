class ReadCode:
	def __init__(self):
		self.index = 0
		self.index_update = {1:4, 2:4, 3:2, 4:2, 5:3, 6:3, 7:4, 8:4}

	def read_code(self, full_code):
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
				full_code[code[1]] = int(input("INPUT: "))
			elif opcode == 4: 
				print(position_input(1))
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
			elif opcode == 99: return True
			self.index += self.index_update[opcode]
			return False

		for _ in range(0, len(full_code)):
			if read_intcode(full_code[self.index:self.index+4], full_code):
				break
		return full_code

with open('day5.txt') as file:
    total_code = [int(i) for i in file.read().split(',')]
reader = ReadCode()
reader.read_code(total_code)


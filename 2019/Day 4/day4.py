import numpy as np
import regex

rx = r'(\d)\1{2,}(*SKIP)(*F)|(\d)\2'

def has_doubles(n):
	for i in ('11', '22', '33', '44', '55', '66', '77', '88', '99'):
		if i in n: return True
	return False

def goes_up(digit):
	if "".join(sorted(digit)) == digit:
		return True
	return False

def check_numbers(n1, n2, extra=False):
	no = 0
	for i in range(n1, n2+1):
		if not goes_up(str(i)): no += 1
		elif extra and not bool(regex.search(rx, str(i))): no += 1
		elif not has_doubles(str(i)): no += 1
	return no

n1, n2, no = 147981, 691423, 0

no = check_numbers(n1, n2)
print("Part 1 is: ", n2-n1-no+1)
no = check_numbers(n1, n2, True)
print("Part 2 is: ", n2-n1-no+1)
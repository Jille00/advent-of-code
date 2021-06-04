import numpy as np
import os
from tqdm import tqdm

def check_line(a, b, c):
	a,b,c = np.array(a), np.array(b), np.array(c)
	crossproduct = (c[1] - a[1]) * (b[0] - a[0]) - (c[0] - a[0]) * (b[1] - a[1])
	# compare versus epsilon for floating point values, or != 0 if using integers
	if abs(crossproduct) != 0:
		return False

	dotproduct = (c[0] - a[0]) * (b[0] - a[0]) + (c[1] - a[1])*(b[1] - a[1])
	if dotproduct < 0:
		return False

	squaredlengthba = (b[0] - a[0])*(b[0] - a[0]) + (b[1] - a[1])*(b[1] - a[1])
	if dotproduct > squaredlengthba:
		return False

	return True

def calculate_LOS(astroid, astroid_coords):
	index = 0
	index1 = 0
	while True:
		if index >= len(astroid_coords):
			break
		while True:
			if index1 >= len(astroid_coords):
				break
			if index != index1 and check_line(astroid, astroid_coords[index], astroid_coords[index1]):
				astroid_coords.remove(astroid_coords[index1])
				index1 -= 1
				index -= 1
			index1 += 1
		index += 1
		index1 = 0
	return len(astroid_coords)

def sort_it(astroid, astroid_coords):
	astroid_coords_check = astroid_coords.copy()
	astroid_coords_check.sort(key = lambda p: (p[0] - astroid[0])**2 + (p[1] - astroid[1])**2)
	astroid_coords_check.remove(astroid)
	return astroid_coords_check

with open('day10.txt') as file:
    string = [i for i in file.read().split('\n')]
astroid_coords = []

for y, row in enumerate(string):
	for x, element in enumerate(row):
		if element == '#':
			astroid_coords.append((x,y))

number_of_LOS = dict()
for astroid in tqdm(astroid_coords):
	astroid_coords_check = sort_it(astroid, astroid_coords)
	number_of_LOS[astroid] = calculate_LOS(astroid, astroid_coords_check)

print(list({k: v for k, v in sorted(number_of_LOS.items(), key=lambda item: item[1])}.values())[-1])
print(list({k: v for k, v in sorted(number_of_LOS.items(), key=lambda item: item[1])}.keys())[-1])

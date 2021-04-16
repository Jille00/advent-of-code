import os
import numpy as np

with open('day1.txt') as f:
	masses = np.array([i.strip() for i in f.read().splitlines()]).astype('int')

print("Part 1 is: ", np.sum(masses // 3 - 2))

def calculate_fuel_cost(mass):
	cost = mass // 3 - 2
	if cost < 0:
		return 0 
	return cost + calculate_fuel_cost(cost)

print("Part 2 is: ", np.sum([calculate_fuel_cost(mass) for mass in masses]))
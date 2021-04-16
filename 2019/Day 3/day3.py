import os
import numpy as np

def calculate_xy(wire):
	wire = [(i[0], int(i[1:])) for i in wire.split(',')]
	current_coordinate, all_coordinates = np.array([0,0]), []

	for index, coordinate in enumerate(wire):
		if coordinate[0] == 'U': 
			li = np.array([[0,i] for i in range(1, coordinate[1] + 1)])
			all_coordinates.append(current_coordinate + li)
			current_coordinate += np.array([0, coordinate[1]])

		elif coordinate[0] == 'D': 
			li = np.array([[0,i] for i in range(1,coordinate[1] + 1)])
			all_coordinates.append(current_coordinate - li)
			current_coordinate -= np.array([0, coordinate[1]])

		elif coordinate[0] == 'R': 
			li = np.array([[i,0] for i in range(1, coordinate[1] + 1)])
			all_coordinates.append(current_coordinate + li)
			current_coordinate += np.array([coordinate[1], 0])

		elif coordinate[0] == 'L': 
			li = np.array([[i,0] for i in range(1, coordinate[1] + 1)])
			all_coordinates.append(current_coordinate - li)
			current_coordinate -= np.array([coordinate[1], 0])

	return np.array([item for sublist in all_coordinates for item in sublist])

def calculate_distance(points):
	return [np.abs(point - [0,0]).sum() for point in points]

def distance(intersection, wire):
	return np.where((wire == intersection).all(axis=1))[0][0] + 1

with open('day3.txt') as file:
    wire_one, wire_two = file.read().split("\n")[0:2]

wire_one, wire_two = calculate_xy(wire_one), calculate_xy(wire_two)
combined = np.array([x for x in set(tuple(x) for x in wire_one) & set(tuple(x) for x in wire_two)])

distances = calculate_distance(combined)
print('Part 1 is: ', np.min(distances))

distances = [distance(inter, wire_one) + distance(inter, wire_two) for inter in combined]
print("Part 2 is: ", np.min(distances))
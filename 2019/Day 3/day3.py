import os
import numpy as np

def calculate_xy(wire):
	wire = [(i[0], int(i[1:])) for i in wire.split(',')]
	current_coordinate = np.array([0,0])
	all_coordinates = []

	for index, coordinate in enumerate(wire):
		if coordinate[0] == 'U': 
			li = np.array([[0,i] for i in range(coordinate[1] + 1)])
			all_coordinates.append(current_coordinate + li)
			current_coordinate += np.array([0, coordinate[1]])

		elif coordinate[0] == 'D': 
			li = np.array([[0,i] for i in range(coordinate[1] + 1)])
			all_coordinates.append(current_coordinate - li)
			current_coordinate -= np.array([0, coordinate[1]])

		elif coordinate[0] == 'R': 
			li = np.array([[i,0] for i in range(coordinate[1] + 1)])
			all_coordinates.append(current_coordinate + li)
			current_coordinate += np.array([coordinate[1], 0])

		elif coordinate[0] == 'L': 
			li = np.array([[i,0] for i in range(coordinate[1] + 1)])
			all_coordinates.append(current_coordinate - li)
			current_coordinate -= np.array([coordinate[1], 0])

	return np.unique([item for sublist in all_coordinates for item in sublist], axis=0)

def calculate_distance(points):
	def manhattan_distance(a, b):
		return np.abs(a - b).sum()
	return [manhattan_distance(point, [0,0]) for point in points]

with open('day3.txt') as file:
    wire_one, wire_two = file.read().split("\n")[0:2]

wire_one = calculate_xy(wire_one)
wire_two = calculate_xy(wire_two)

combined = [x for x in set(tuple(x) for x in wire_one) & set(tuple(x) for x in wire_two)]
combined.remove((0,0))
combined = np.array(combined)
distances = calculate_distance(combined)
print('Part 1 is: ', np.min(distances))

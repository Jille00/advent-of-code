import numpy as np
from collections import defaultdict

def create_dic(bidirectional=False):
	with open('day6.txt') as file:
	    orbits = file.read().split('\n')
	orbits = np.array([i.split(")") for i in orbits])

	di = defaultdict(list)
	for orbit in orbits:
		di[orbit[0]].append(orbit[1])
		if bidirectional: di[orbit[1]].append(orbit[0])
	return di

def find_shortest_path(graph, start, end, path=[]):
    """
    __source__='https://www.python.org/doc/essays/graphs/'
    __author__='Guido van Rossum'
    """
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = find_shortest_path(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest

def calculate_distance(di):
	def distance(value, dis):
		dis += len(di[value])
		for node in di[value]:
			dis = distance(node, dis)
		return dis
	return np.sum([distance(node, 0) for node in list(di)])

print("Part 1 is: ", calculate_distance(create_dic()))
print("Part 2 is: ", len(find_shortest_path(create_dic(True),'YOU','SAN'))-3)
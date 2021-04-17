import numpy as np
from collections import Counter
import matplotlib.pyplot as plt

def find_next_non_transparant(layers, index):
	for i in layers:
		if i[index] != 2:
			return i[index]

with open('day8.txt') as file:
    total_image = np.array([i for i in file.read()])

WIDTH = 25
HEIGHT = 6
layers = np.array(np.array_split(total_image, len(total_image)/(WIDTH*HEIGHT))).astype('int')
zeros = np.count_nonzero(layers==0, axis=1)
correct_layer = layers[np.argmin(zeros)]
print("Part 1 is: ", np.count_nonzero(correct_layer==1)* np.count_nonzero(correct_layer==2))

main_layer = layers[0]
for index, i in enumerate(main_layer):
	if i == 2:
		main_layer[index] = find_next_non_transparant(layers, index)

plt.imshow(main_layer.reshape((HEIGHT, WIDTH)), cmap='gray')
plt.show()
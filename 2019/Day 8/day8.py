import numpy as np
import matplotlib.pyplot as plt

def find_next_non_transparant(layers, index):
	for i in layers:
		if i[index] != 2:
			return i[index]

with open('day8.txt') as file:
    total_image = np.array([i for i in file.read()])

WIDTH, HEIGHT = 25, 6
layers = np.array(np.array_split(total_image, len(total_image)/(WIDTH*HEIGHT))).astype('int')
zeros = np.count_nonzero(layers==0, axis=1)
correct_layer = layers[np.argmin(zeros)]
print("Part 1 is: ", np.count_nonzero(correct_layer==1) * np.count_nonzero(correct_layer==2))

main_layer = [find_next_non_transparant(layers, index) if i == 2 else i for index, i in enumerate(layers[0])]
plt.imshow(np.array(main_layer).reshape((HEIGHT, WIDTH)), cmap='gray')
plt.show()
import iqif
import matplotlib.pyplot as plt

def neuron(potential):
	lines = []
	for filename in potential:
		with open(filename,'r') as f:
			for line in f:
				lines.append(int(line.strip(), 10))
	return lines
	
def update(list, tmp):
	# index = 5最舊  index = 0 最新
	for i in range(len(tmp)):
		for j in range(9,-1,-1):
			list[i][j] = list[i][j-1]
		list[i][0] = tmp[i]
	return list
	
def turn_strength(x):
    return x//0.3

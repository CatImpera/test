import iqif
import matplotlib.pyplot as plt

def neuron(potential):
	lines = []
	for filename in potential:
		with open(filename) as f:
			for line in f:
				lines.append(int(line.strip(), 10))
	return lines
	
def update(list, tmp):
	# index = 9最舊  index = 0 最新
	for i in range(13):
		for j in range(9,-1,-1):
			list[i][j] = list[i][j-1]
		list[i][0] = tmp[i]
	return list
	
def turn_strength(x):
    if x >= 0.5:
        return 5
    elif x > 0:
        return int(x * 10)+1
    else:
        return 0

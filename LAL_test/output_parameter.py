connection = open("parameter/Connection_Table_LIF.txt","w")
neuron = open("parameter/neuronParameter_LIF.txt","w")

#inhead<->inhead

#connection.write(f"1 12 1 64\n")
#0 -0.1 128 192 64 3
#index, g, rest, threshold, reset, noise 
con1 = 0.3
threshold = 150
for i in range(12):
	connection.write(f"{i} 12 {con1} 64\n")
	neuron.write(f"{i} -0.1 128 {threshold} 64 3\n")

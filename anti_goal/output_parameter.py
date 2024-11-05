"""
"neu_list": [
"L017","R017",
"L112","R112",
"L153","R153",
"L_DN","R_DN"
]
"""
connection = open("parameter/Connection_Table_LIF.txt","w")
neuron = open("parameter/neuronParameter_LIF.txt","w")

#0 -0.1 128 192 64 3
#index, g, rest, threshold, reset, noise
threshold = 150
for i in range(8):
	neuron.write(f"{i} -0.1 128 {threshold} 64 3\n")
	
#153->017
con = 0.5
connection.write(f"4 1 {con} 64\n")
connection.write(f"5 0 {con} 64\n")

#153->122
con = 0.5
connection.write(f"4 3 {con} 64\n")
connection.write(f"5 2 {con} 64\n")

#153->DN
con = 1
connection.write(f"4 7 {con} 64\n")
connection.write(f"5 6 {con} 64\n")

#017->122
con = 0.5
connection.write(f"0 2 {con} 64\n")
connection.write(f"1 3 {con} 64\n")

#122-|017
con = -0.5
connection.write(f"2 1 {con} 64\n")
connection.write(f"3 0 {con} 64\n")

#122-|DB
con = -0.5
connection.write(f"2 7 {con} 64\n")
connection.write(f"3 6 {con} 64\n")



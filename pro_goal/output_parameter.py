inhead_list = [i for i in range(8)]               #inhead     0~7
ingoal_list = [i for i in range(8,20)]            #ingoal     8~19
inheadin_list = [20]                              #inheadin   20
ingoalin_list = [21]                              #ingoalin   21
FC2_list = [i for i in range(22,34)]              #FC2        22~33
headinput_list = [i for i in range(34,50)]        #headinput  34~49
PFL3_list = [i for i in range(50,74)]             #PFL3       50~73
LAL_list = [i for i in range(74, 82)]             #LAL        74~81
connection = open("parameter/Connection_Table_LIF.txt","w")
neuron = open("parameter/neuronParameter_LIF.txt","w")

#0 -0.1 128 192 64 3
#index, g, rest, threshold, reset, noise
threshold = 150
for i in range(82):
	neuron.write(f"{i} -0.1 128 {threshold} 64 3\n")
#inhead<->inhead

con = 1
for i in range(0,7):
	connection.write(f"{i} {i+1} {con} 64\n")
for i in range(1,8):
	connection.write(f"{i} {i-1} {con} 64\n")
connection.write(f"7 0 {con} 64\n")
connection.write(f"0 7 {con} 64\n")


#inhead<->inheadin

con1 = 1
con2 = -0.4
for i in inhead_list:
	connection.write(f"{i} {inheadin_list[0]} {con1} 64\n")
	connection.write(f"{inheadin_list[0]} {i} {con2} 64\n")


#ingoal<->ingoal

con = 0.8
for i in ingoal_list:
	if i == 19:
		break
	connection.write(f"{i} {i+1} {con} 64\n")
for i in ingoal_list:
	if i == 8:
		continue
	connection.write(f"{i} {i-1} {con} 64\n")
connection.write(f"8 19 {con} 64\n")
connection.write(f"19 8 {con} 64\n")


#ingoal<->ingoalin

con1 = 1
con2 = -0.4
for i in ingoal_list:
	connection.write(f"{i} {ingoalin_list[0]} {con1} 64\n")
	connection.write(f"{ingoalin_list[0]} {i} {con2} 64\n")

#ingoal->FC2

con = 2
for i in range(len(ingoal_list)):
	connection.write(f"{ingoal_list[i]} {FC2_list[i]} {con} 64\n")


#inhead->headinput

con = 1.8
connection.write(f"0 41 {con} 64\n")
connection.write(f"1 42 {con} 64\n")
connection.write(f"2 34 {con} 64\n")
connection.write(f"2 43 {con} 64\n")
connection.write(f"3 35 {con} 64\n")
connection.write(f"3 44 {con} 64\n")
connection.write(f"4 36 {con} 64\n")
connection.write(f"4 46 {con} 64\n")
connection.write(f"5 37 {con} 64\n")
connection.write(f"5 47 {con} 64\n")
connection.write(f"6 39 {con} 64\n")
connection.write(f"6 48 {con} 64\n")
connection.write(f"7 40 {con} 64\n")
connection.write(f"7 49 {con} 64\n")
connection.write(f"5 38 {con} 64\n")
connection.write(f"3 45 {con} 64\n")
connection.write(f"6 38 {con} 64\n")
connection.write(f"4 45 {con} 64\n")


#FC2->PFL3
con = 1.5

for i in range(12):
	connection.write(f"{FC2_list[i]} {PFL3_list[2*i]} {con} 64\n")
	connection.write(f"{FC2_list[i]} {PFL3_list[2*i+1]} {con} 64\n")


#headinput->PFL3
con = 1.5
connection.write(f"34 50 {con} 64\n")
connection.write(f"35 52 {con} 64\n")
connection.write(f"36 54 {con} 64\n")
connection.write(f"36 56 {con} 64\n")
connection.write(f"37 58 {con} 64\n")
connection.write(f"38 60 {con} 64\n")
connection.write(f"39 62 {con} 64\n")
connection.write(f"40 51 {con} 64\n")
connection.write(f"40 64 {con} 64\n")
connection.write(f"41 53 {con} 64\n")
connection.write(f"41 66 {con} 64\n")
connection.write(f"41 68 {con} 64\n")
connection.write(f"42 55 {con} 64\n")
connection.write(f"42 57 {con} 64\n")
connection.write(f"42 70 {con} 64\n")
connection.write(f"43 59 {con} 64\n")
connection.write(f"43 72 {con} 64\n")
connection.write(f"44 61 {con} 64\n")
connection.write(f"45 63 {con} 64\n")
connection.write(f"46 65 {con} 64\n")
connection.write(f"47 67 {con} 64\n")
connection.write(f"47 69 {con} 64\n")
connection.write(f"48 71 {con} 64\n")
connection.write(f"49 73 {con} 64\n")

#PFL3->LAL
con = 0.05
for i in range(50,74,2):
	connection.write(f"{i} 74 {con} 64\n")
for i in range(51,74,2):
	connection.write(f"{i} 75 {con} 64\n")
#LAL->E
con = 2
connection.write(f"74 77 {con} 64\n")
connection.write(f"75 76 {con} 64\n")

#Exc->inh
con = 1
connection.write(f"76 78 {con} 64\n")
connection.write(f"77 79 {con} 64\n")

#inh->Exc
con = -0.5
connection.write(f"78 77 {con} 64\n")
connection.write(f"79 76 {con} 64\n")

#Exc->LR
con = 2
connection.write(f"76 80 {con} 64\n")
connection.write(f"77 81 {con} 64\n")

#inh->LR
con = -0.5
connection.write(f"78 81 {con} 64\n")
connection.write(f"79 80 {con} 64\n")

"""
inhead         0~7
ingoal         8~19
inheadin       20
ingoalin       21
FC2            22~33
headinput      34~49
PFL3           50~73
LAL            74~81
017            82, 83
112            84, 85
153   			86, 87
"""
#-------------------------neuron parameter-----------------------
g = -0.1
rest = 128
threshold = 150
reset = 64
noise = 3
#-------------------------synapse parameter----------------------
S_inhead = 1
S_inhead_In = 1
S_In_inhead = -0.4
S_ingoal = 0.8
S_ingoal_In = 1
S_In_ingoal = -0.4
S_ingoal_FC2 = 2
S_inhead_headinput = 1.8
S_FC2_FPL3 = 1.5
S_headinput_PFL3 = 1.5
S_PFL3_LAL = 0.05
S_LAL_E = 2
S_E_I = 1
S_I_E = -0.5
S_E_DN = 2
S_I_DN = -0.5
S_153_017 = 1
S_153_122 = 1
S_153_DN = 1
S_017_122 = 1
S_122_017 = -1
S_122_DN = -1
S_122_E = -0.2

#----------------------neuron---------------------------------
neuron = open("parameter/neuronParameter_LIF.txt","w")

#0 -0.1 128 192 64 3
#index, g, rest, threshold, reset, noise
for i in range(88):
	neuron.write(f"{i} {g} {rest} {threshold} {reset} {noise}\n")

#---------------------synapse---------------------------------
connection = open("parameter/Connection_Table_LIF.txt","w")

#------------pro-goal--------------------------
#inhead<->inhead
for i in range(0,7):
	connection.write(f"{i} {i+1} {S_inhead} 64\n")
for i in range(1,8):
	connection.write(f"{i} {i-1} {S_inhead} 64\n")
connection.write(f"7 0 {S_inhead} 64\n")
connection.write(f"0 7 {S_inhead} 64\n")

#inhead<->inheadin
for i in range(8):
	connection.write(f"{i} 20 {S_inhead_In} 64\n")
	connection.write(f"20 {i} {S_In_inhead} 64\n")

#ingoal<->ingoal
for i in range(8,20):
	if i == 19:
		break
	connection.write(f"{i} {i+1} {S_ingoal} 64\n")
for i in range(8,20):
	if i == 8:
		continue
	connection.write(f"{i} {i-1} {S_ingoal} 64\n")
connection.write(f"8 19 {S_ingoal} 64\n")
connection.write(f"19 8 {S_ingoal} 64\n")

#ingoal<->ingoalin
for i in range(8,20):
	connection.write(f"{i} 21 {S_ingoal_In} 64\n")
	connection.write(f"21 {i} {S_In_ingoal} 64\n")

#ingoal->FC2
for i in range(8,20):
	connection.write(f"{i} {i+14} {S_ingoal_FC2} 64\n")

#inhead->headinput
connection.write(f"0 41 {S_inhead_headinput} 64\n")
connection.write(f"1 42 {S_inhead_headinput} 64\n")
connection.write(f"2 34 {S_inhead_headinput} 64\n")
connection.write(f"2 43 {S_inhead_headinput} 64\n")
connection.write(f"3 35 {S_inhead_headinput} 64\n")
connection.write(f"3 44 {S_inhead_headinput} 64\n")
connection.write(f"4 36 {S_inhead_headinput} 64\n")
connection.write(f"4 46 {S_inhead_headinput} 64\n")
connection.write(f"5 37 {S_inhead_headinput} 64\n")
connection.write(f"5 47 {S_inhead_headinput} 64\n")
connection.write(f"6 39 {S_inhead_headinput} 64\n")
connection.write(f"6 48 {S_inhead_headinput} 64\n")
connection.write(f"7 40 {S_inhead_headinput} 64\n")
connection.write(f"7 49 {S_inhead_headinput} 64\n")
connection.write(f"5 38 {S_inhead_headinput} 64\n")
connection.write(f"3 45 {S_inhead_headinput} 64\n")
connection.write(f"6 38 {S_inhead_headinput} 64\n")
connection.write(f"4 45 {S_inhead_headinput} 64\n")

#FC2->PFL3
for i in range(12):             
	connection.write(f"{i+22} {50+2*i} {S_FC2_FPL3} 64\n")
	connection.write(f"{i+22} {50+2*i+1} {S_FC2_FPL3} 64\n")

#headinput->PFL3
connection.write(f"34 50 {S_headinput_PFL3} 64\n")
connection.write(f"35 52 {S_headinput_PFL3} 64\n")
connection.write(f"36 54 {S_headinput_PFL3} 64\n")
connection.write(f"36 56 {S_headinput_PFL3} 64\n")
connection.write(f"37 58 {S_headinput_PFL3} 64\n")
connection.write(f"38 60 {S_headinput_PFL3} 64\n")
connection.write(f"39 62 {S_headinput_PFL3} 64\n")
connection.write(f"40 51 {S_headinput_PFL3} 64\n")
connection.write(f"40 64 {S_headinput_PFL3} 64\n")
connection.write(f"41 53 {S_headinput_PFL3} 64\n")
connection.write(f"41 66 {S_headinput_PFL3} 64\n")
connection.write(f"41 68 {S_headinput_PFL3} 64\n")
connection.write(f"42 55 {S_headinput_PFL3} 64\n")
connection.write(f"42 57 {S_headinput_PFL3} 64\n")
connection.write(f"42 70 {S_headinput_PFL3} 64\n")
connection.write(f"43 59 {S_headinput_PFL3} 64\n")
connection.write(f"43 72 {S_headinput_PFL3} 64\n")
connection.write(f"44 61 {S_headinput_PFL3} 64\n")
connection.write(f"45 63 {S_headinput_PFL3} 64\n")
connection.write(f"46 65 {S_headinput_PFL3} 64\n")
connection.write(f"47 67 {S_headinput_PFL3} 64\n")
connection.write(f"47 69 {S_headinput_PFL3} 64\n")
connection.write(f"48 71 {S_headinput_PFL3} 64\n")
connection.write(f"49 73 {S_headinput_PFL3} 64\n")

#PFL3->LAL
for i in range(50,74,2):
	connection.write(f"{i} 74 {S_PFL3_LAL} 64\n")
for i in range(51,74,2):
	connection.write(f"{i} 75 {S_PFL3_LAL} 64\n")

#LAL->E
connection.write(f"74 77 {S_LAL_E} 64\n")
connection.write(f"75 76 {S_LAL_E} 64\n")

#Exc->inh
connection.write(f"76 78 {S_E_I} 64\n")
connection.write(f"77 79 {S_E_I} 64\n")

#inh->Exc
connection.write(f"78 77 {S_I_E} 64\n")
connection.write(f"79 76 {S_I_E} 64\n")

#Exc->LR
connection.write(f"76 80 {S_E_DN} 64\n")
connection.write(f"77 81 {S_E_DN} 64\n")

#inh->LR
connection.write(f"78 81 {S_I_DN} 64\n")
connection.write(f"79 80 {S_I_DN} 64\n")

#-----------anti_goal---------------------
#153->017
connection.write(f"87 82 {S_153_017} 64\n")
connection.write(f"86 83 {S_153_017} 64\n")

#153->122
connection.write(f"87 84 {S_153_122} 64\n")
connection.write(f"86 85 {S_153_122} 64\n")

#153->DN    #不確定是不是接對邊
connection.write(f"87 80 {S_153_DN} 64\n")
connection.write(f"86 81 {S_153_DN} 64\n")

#017->122
connection.write(f"82 84 {S_017_122} 64\n")
connection.write(f"83 85 {S_017_122} 64\n")

#122-|017
connection.write(f"84 83 {S_122_017} 64\n")
connection.write(f"85 82 {S_122_017} 64\n")

#122-|DN    #不確定是不是接對邊
connection.write(f"84 81 {S_122_DN} 64\n")
connection.write(f"85 80 {S_122_DN} 64\n")

#122-|Exc
connection.write(f"84 77 {S_122_E} 64\n")
connection.write(f"85 76 {S_122_E} 64\n")


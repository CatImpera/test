connection = open("parameter/Connection_Table_LIF.txt","w")
#inhead<->inhead

#connection.write(f"1 12 1 64\n")
con1 = 0.3
for i in range(12):
	connection.write(f"{i} 12 {con1} 64\n")


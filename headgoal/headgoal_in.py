import matplotlib.pyplot as plt

###input angle
inp_g = 24
inp_h = 24
record_inp_h = []
record_g1 = []
record_g2 = []
record_h1 = []
record_h2 = []

goal_angle = [2,6,10,14,18,22,24,28,32,36,42,46]    #input range(12 - 36)
head_angle = [3, 9, 15, 21, 27, 33, 39, 45]     #input range(12-36)

goaln1 = 999999
goaln2 = 999999

headn1 = 999999
headn2 = 999999


#####goal#####
for k in range(0,11):
    if inp_g == goal_angle[k]:
        goaln1 = k
        break
    if inp_g == 46:
        goaln1=345
        break
    if inp_g > 46 or inp_g < 2:
        goaln1 = 11
        goaln2 = 0
        break
    if inp_g > goal_angle[k] and inp_g < goal_angle[k+1] :
        goaln1 = k
        goaln2 = k+1
        break


ratio_g = 0

#30 = 360/12
#48/12 = 4

if inp_g < 2:
    ratio_g = (inp_g+1)/4
elif inp_g > 46:
    ratio_g = (48-inp_g)/4
elif inp_g == 48:
    ratio_g = 0.5
elif goaln2 == 999999:
    ratio_g = 0
    goaln2 = goaln1
else:
    ratio_g = (inp_g-goal_angle[goaln1])/4

gIn1 = 1*(1-ratio_g)
gIn2 = 1*ratio_g

inp_g+=0.2
record_g1.append(gIn1)
record_g2.append(gIn2)


#####head#####


for k in range(1,7):
    if inp_h == head_angle[k]:
        headn1 = inp_h
        print('flag')
        break
    if inp_h > head_angle[k] and inp_h < head_angle[k+1] :
        headn1 = k
        headn2 = k+1
        break

ratio_h =0

#45 = 360/8
#48/8 = 6

if inp_h < 3:
    ratio_h = (inp_h+3)/6
elif inp_h > 45:
    ratio_h = (48-inp_h)/6
elif inp_h == 48:
    ratio_h = 0.5
elif headn2 == 999999:
    ratio_h = 0
    headn2 = headn1
else:
    ratio_h = (inp_h-head_angle[headn1])/6

hIn1 = 1*(1-ratio_h)
hIn2 = 1*ratio_h


inp_h+= 0.2
record_h1.append(hIn1)
record_h2.append(hIn2)
record_inp_h.append(inp_h)
#print(inp_h)
    




print("headn1 = ", headn1,"hIn1 = ", hIn1)
print("headn2 = ", headn2,"hIn2 = ", hIn2)
print("goaln1 = ", goaln1,"gIn1 = ", gIn1)
print("goaln2 = ", goaln2,"gIn2 = ", gIn2)
"""
plt.figure()
plt.plot(record_h1)
plt.plot(record_h2)
#plt.plot(record_inp_h)
plt.savefig('head.png')
plt.close()
"""

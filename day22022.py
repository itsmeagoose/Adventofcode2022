#advent of code 2022
#day 2 both parts 
f = open('inputday2.txt','r').read().splitlines()
y= 0
o= 0
score = 0
for i in f:
    if i[0] == "A":
        o = 1
    elif i[0] == "B":
        o = 2
    elif i[0] =="C":
        o = 3
        
    if i[2] == "X":
        score += 0
        y = o - 1
    elif i[2] == "Y":
        score += 3
        y = o
    elif i[2] == "Z":
        score  += 6
        y = o + 1

    if y == 0:
        y =3
    elif y == 4:
        y =1

    score += y

print(score)
    

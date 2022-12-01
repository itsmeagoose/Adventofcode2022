#advent of code 2022
#day 1 both parts 
f = open('inputday1.txt','r').read().splitlines()
totals = []
total = 0
for i in f:
    if i == "":
        totals.append(total)
        total =  0
    else:
        total += int(i)
m = 0
s = 0
t = 0
for i in totals:
    if i > m:
        t = s
        s = m
        m = i
    elif i > s:
        t = s
        s = i
    elif i > t:
        t = i
print(m + s + t)
    
    
    

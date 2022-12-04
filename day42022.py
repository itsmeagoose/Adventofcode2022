#advent of code 2022
#day 4 both parts 
f = open('inputday4.txt','r').read().splitlines()
score = 0
for i in f:
    pairs = i.split(",")
    one = pairs[0].split("-")
    two = pairs[1].split("-")
    if int(one[0]) <= int(two[0]) and int(one[1]) >= int(two[1]):
        score += 1
    elif int(one[0]) >= int(two[0]) and int(one[1]) <= int(two[1]):
        score += 1
    elif int(one[0]) <= int(two[0]) and int(one[1]) >= int(two[0]):
        score += 1
    elif int(one[0]) >= int(two[0]) and int(one[0]) <= int(two[1]):
        score += 1
    
print(score)
    
    

#advent of code 2022
#day 3 both parts 
f = open('inputday3.txt','r').read().splitlines()
same = []
score = 0
"""
for i in f:
    half = len(i)//2
    c = 0
    done = False
    while c <= half-1 and not done:
        c1 = half
        while c1 < len(i) and not done:
            if i[c] == i[c1]:
                same.append(i[c])
                done = True
            else:
                c1+=1
        c += 1
"""
i = 0
while i < len(f) - 1:
    both = []
    a = f[i]
    b = f[i + 1]
    c = f[i + 2]
    for k in a:
        for m in b:
            if k == m:
                both.append(k)
    done = False
    for k in both:
        for m in c:
            if k == m:
                same.append(k)
                done = True
                break
        if done == True:
            break
    i += 3
                

                
for i in same:
    if i.isupper() == True:
        score += 26
        score += ord(i) - 64
    else:
        score += ord(i) - 96
print(score)          

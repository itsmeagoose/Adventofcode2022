#advent of code 2022
#day 5 both parts 
f = open('inputday5.txt','r').read().splitlines()
stacks =[]
c = 0
t = 0
stop = ["move", "from", "to"]
while c < 9:
    done = False
    i = 0
    m = 1
    colnum = []
    while not done:
        m += 1
        if f[i][(c*4)+1].isnumeric() == True:
            if m > t:
                t = m
            c += 1
            stacks.append(colnum)
            #print(stacks)
            done = True
        else:
            colnum.append(f[i][(c*4)+1])
            i +=1
for i in range(0, t):
    f.remove(f[0])
for i in stacks:
    while " " in i:
        i.remove(" ")
#print(stacks)
for i in f:
    k = i.split()
    p = []
    for l in k:
        if l.isnumeric() == True:
            l = int(l)
            p.append(l)
    #print(len(stacks[p[1]-1]), len(stacks[p[2]-1]), p[0])
    for z in range(0,p[0]):
        #print(stacks)
        stacks[p[2]-1][:0] = stacks[p[1]-1][p[0] - (z+1)]
        #print("move from", p[1], "to", p[2])
        stacks[p[1]-1].pop(p[0] - (z+1))
    #print(len(stacks[p[1]-1]), len(stacks[p[2]-1]))
    #print(stacks)
for i in range (0,9):
    print(stacks[i][0])
        

    

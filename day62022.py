#advent of code 2022
#day 6 both parts 
f = open('inputday6.txt','r').read().splitlines()
f = list(f[0])
i = 0
done = False
while i < len(f)-13 and not done:
    packet = []
    for l in range (0,14):
        packet.append(f[i+l])
    if len(packet) == len(set(packet)):
        print(i+14)
        done = True
    i += 1
    

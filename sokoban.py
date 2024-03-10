from func import *

level = []
fd = open("./map.skb")
y = 0
mapNbr = int(fd.read(1)) #read number of levels
fd.read(1)
print(mapNbr)
while y < mapNbr: #parse map
    subsublist = []
    for line in fd:
        sublist = []
        for x in line:
            if x == "N":                
                break
            elif (x != '\n'):
                sublist.append(int(x))
        if x == "N":
            break
        subsublist.append(sublist)
    level.append(subsublist)
    y += 1
mainMenu(level) #start gane
        
     


from func import *

level = []
fd = open("/Users/blndl/Documents/python/sokoban/map.skb")
y = 0
mapNbr = int(fd.read(1))
fd.read(1)
print(mapNbr)
while y < mapNbr:
    subsublist = []
    for line in fd:
        sublist = []
        for x in line:
            if x == "N":                
                break
            elif (x != '\n'):
                sublist.append(int(x))
        if x == "N":
        #    fd.read(1)
            break
            
        subsublist.append(sublist)

    level.append(subsublist)
    y += 1
print(level)
adventureLoop(level)
#gameLoop(level)
        
     


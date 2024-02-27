from func import *

level = []
fd = open("/Users/blndl/Documents/python/sokoban/map.skb")
for line in fd:
    sublist = []
    for x in line:
        if (x != '\n'):
            sublist.append(int(x))
    level.append(sublist)
gameLoop(level)
        
     


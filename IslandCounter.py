import numpy as np
import sys
import matplotlib.pyplot as plt




def islandCounter(map):
    # map accepted as numpy matrix
    count=0
    for i in range(0,map.shape[0]):
        for j in range(0,map.shape[1]):
            (isIsland,map) = markIsland(map,i,j)
            if(isIsland):
                count+=1
    return count

def markIsland(map,r,c):
    if((r >= map.shape[0]) or (c >= map.shape[1])):
       return (False, map)
    if(map[r,c] == 0):
        return (False, map)
    else:
       map[r][c] = 0
       (dummy,map) = markIsland(map,r+1,c)
       (dummy,map) = markIsland(map,r-1,c)
       (dummy,map) = markIsland(map,r,c+1)
       (dummy,map) = markIsland(map,r,c-1)
       return (True,map)



##################IslandCounter Test

test=np.zeros((10,10))
test[5,5] = 1
test[6,5] = 1
test[1,1] = 1
test[2,2] = 1

# Plot the grid
plt.imshow(test)
plt.gray()
plt.show()
print("Number of Islands: ",islandCounter(test))

test2 = np.zeros((10,10))

for i in range(0,test2.shape[0]):
    for j in range(0, test2.shape[1]):
        if((i%2==0) and (j%2 == 1)):
           test2[i,j]=1
        elif ((i%2==1) and (j%2 == 0)):
           test2[i,j]=1

# Plot the grid
plt.imshow(test2)
plt.gray()
plt.show()
print("Number of Islands: ",islandCounter(test2))







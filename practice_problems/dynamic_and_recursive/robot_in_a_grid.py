'''

 Robot in a Grid:
  Imagine a robot sitting on the upper left corner of grid with r rows and c columns. 
  The robot can only move in two directions, right and down, but certain celss are "off limits" such that 
  the rebot cannot step on them. Design an algorithm to find a path for the robot from the top left to the bottom right.

'''

import numpy as np

class Grid:
    def __init__(self, r,c):
        self.r = r
        self.c = c
        self.grid = np.zeros(shape=(r,c))
        
    def block(self, i , j):
        self.grid[i][j] = -1
     
    def _exist(self,i,j):
        return i>=0 and i<self.r and j>=0 and j<self.c and self.grid[i][j]==0
        
    def findPath(self,x1,y1,x2,y2,path):
        self.grid[x1][y1] = 1
        if x1==x2 and y1==y2:
            return True,path
        if self._exist(x1+1,y1):
            path.append((x1+1,y1))
            flag, p =self.findPath(x1+1,y1,x2,y2,path)
            if flag:
                return True,p
            else:
                path.pop()
        if self._exist(x1,y1+1):
            path.append((x1,y1+1))
            flag,p = self.findPath(x1,y1+1,x2,y2,path)
            if flag:
                return True,p
            else:
                path.pop()
        return False,None


#### TEST #####

g = Grid(10,10)

g.block(9,8)
g.block(2,0)
g.block(4,1)
g.block(8,0)
g.block(8,2)

path = [(0,0)]

flag, path = g.findPath(0,0,9,9,path)
print(flag, path)









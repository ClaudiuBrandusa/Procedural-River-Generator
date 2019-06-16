#input : the size of the matrix

#===================================================Imports=============================================================

import random

#===================================================Classes=============================================================

#setting up the World class

class World:
    def __init__(self):
        self.isGenerated=False
        self.matrix=[]
        self.x=0 # i have set to 0 to get access to it outside of the 'try'
        self.y=0
        while self.x < 2 :
            try:
                self.x=int(input("introduce an integer that is greater than 1 for the X axis\n")) # width of the matrix
            except ValueError:
                print("integers only!")
        while self.y < 2 :
            try:
                self.y=int(input("introduce a number that is greater than 1 for the Y axis\n")) # height of the matrix
            except ValueError:
                print("integers only!")
    def __str__(self):
        return "{} {}".format(self.x,self.y)
    def __repr__(self):
        return "{} {}".format(self.x,self.y)
    # generating the matrix
    def Generate(self):
        for i in range(self.y):
            l=[]
            for j in range(self.x):
                l.append(0)
            self.matrix.append(l)
        self.isGenerated = True
    def PrintMatrix(self):
        if self.isGenerated == False: # if the matrix has not been generated, then we will generate it
            self.Generate()
        s='' # we will store our matrix in this string
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                s+=str(self.matrix[i][j])+" "
            s+="\n"
        print(s)
    def GetMatrix(self):
        if self.isGenerated == False: # we will generate the matrix if it was not generated yet
            self.Generate()
        return self.matrix
    def ApplyPath(self,path): # this function just iterates the path and puts 1's where the path goes
        for i in range(len(path)):
            self.matrix[path[i][1]][path[i][0]]=1

#setting up the River class

class River:
    def __init__(self,matrix):
        self.map=matrix # here we are storing a reference from the matrix
        self.path=[] # here we will store the coordinates from where the river pases
        self.start=[] # here we are storing the start coordinate, it can start from the left or from the up part of the matrix
        self.direction=-1 # -1 means that the direction has not been set
        self.hasStartPoint=False
        self.hasGeneratedPath=False
    def SetStartPoint(self):
        # 0 for left and 1 for up
        self.direction=random.randint(0,1)
        if self.direction == 0 :
            self.start=[0,random.randint(0,len(self.map)-1)]
        else:
            self.start = [random.randint(0,len(self.map[0])-1),0]
        self.path.append(self.start)
        self.hasStartPoint=True
    def GetStartPoint(self):
        if self.hasStartPoint == False:
            self.SetStartPoint()
        return self.start
    def GeneratePath(self):
        if self.direction == 1 : # up
            print('up')
            for i in range(len(self.map)-1): # it will iterate until the end of the matrix
                possibleDirections = []
                if self.path[i][0]<1: # then we cant have values lesser than that so we will have only two possible directions
                    possibleDirections.append([self.path[i][0],i+1])
                    possibleDirections.append([self.path[i][0] + 1,i+1])
                elif self.path[i][0]>=len(self.map[0])-1: # then we cant have values greater than that so we will have only two possible directions
                    possibleDirections.append([self.path[i][0] - 1,i+1])
                    possibleDirections.append([self.path[i][0],i+1])
                else: # else we can have all three possible directions
                    possibleDirections.append([self.path[i][0] - 1,i+1])
                    possibleDirections.append([self.path[i][0],i+1])
                    possibleDirections.append([self.path[i][0] + 1,i+1])
                self.path.append(possibleDirections[random.randint(0,len(possibleDirections)-1)])
        else: # left
            print("left")
            for i in range(len(self.map[0])-1): # it will iterate until the end of the matrix
                possibleDirections = []
                if self.path[i][1]<1: # then we cant have values lesser than that so we will have only two possible directions
                    possibleDirections.append([i+1,self.path[i][1]])
                    possibleDirections.append([i+1,self.path[i][1] + 1])
                elif self.path[i][1]>=len(self.map[i])-1: # then we cant have values greater than that so we will have only two possible directions
                    possibleDirections.append([i+1,self.path[i][1]])
                    possibleDirections.append([i+1,self.path[i][1] - 1])
                else: # else we can have all three possible directions
                    possibleDirections.append([i + 1, self.path[i][1] - 1])
                    possibleDirections.append([i + 1, self.path[i][1]])
                    possibleDirections.append([i + 1, self.path[i][1] + 1])
                self.path.append(possibleDirections[random.randint(0,len(possibleDirections)-1)])
        self.hasGeneratedPath = True
    def GetPath(self):
        if self.hasGeneratedPath == False:
            self.GeneratePath()
        return self.path

#======================================================Objects==========================================================

# getting the user's input

world = World()
river = River(world.GetMatrix())
print("Start point : ",river.GetStartPoint())
world.ApplyPath(river.GetPath())
world.PrintMatrix()

#out: a matrix of 0's and a line of 1's that will form a line (thats the river).
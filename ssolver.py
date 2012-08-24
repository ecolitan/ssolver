from math import *

testposition = [[5,3,None,None,7,None,None,None,None],
              [6,None,None,1,9,5,None,None,None],
              [None,9,8,None,None,None,None,6,None],
              [8,None,None,None,None,6,None,None,None,None,3],
              [4,None,None,8,None,3,None,None,1],
              [7,None,None,None,None,2,None,None,None,None,6],
              [None,6,None,None,None,None,2,8,None],
              [None,None,None,4,1,9,None,None,5],
              [None,None,None,None,8,None,None,7,9]]

class SPosition():
    def __init__(self):
        self.position = [[None,None,None,None,None,None,None,None,None],
                         [None,None,None,None,None,None,None,None,None],
                         [None,None,None,None,None,None,None,None,None],
                         [None,None,None,None,None,None,None,None,None],
                         [None,None,None,None,None,None,None,None,None],
                         [None,None,None,None,None,None,None,None,None],
                         [None,None,None,None,None,None,None,None,None],
                         [None,None,None,None,None,None,None,None,None],
                         [None,None,None,None,None,None,None,None,None]]
                         
    def UpdatePosition(self, _positionvector):
        self.position = _positionvector
        
    def UpdateField(self, _ij, _n):
        """_ij is a list with coordinates
        n is the new number"""
        self.position[_ij[0]][_ij[1]] = _n

def UpdatePossiblitiySquare(_positionvector):
    """Where number is known, possibility is None. Otherwise possibility is a list
    Return possibility position object"""
    def createCube(locy, locx):
        cube = []
        for i in locy:
            for j in locx:
                cube.append([i, j])
        return cube
    cube00 = createCube([0,1,2],[0,1,2])
    cube01 = createCube([0,1,2],[3,4,5])
    cube02 = createCube([0,1,2],[6,7,8])
    cube10 = createCube([3,4,5],[0,1,2])
    cube11 = createCube([3,4,5],[3,4,5])
    cube12 = createCube([3,4,5],[6,7,8])
    cube20 = createCube([6,7,8],[0,1,2])
    cube21 = createCube([6,7,8],[3,4,5])
    cube22 = createCube([6,7,8],[6,7,8])
    
    
    

UpdatePossiblitiySquare(testposition)
        



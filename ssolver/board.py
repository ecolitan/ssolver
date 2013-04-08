'''
    ssolver: Solve sudoku puzzles.
    Copyright (C) <2012-2013>  <Aaron Cossey (aaron dot cossey at gmail dot com)>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

from collections import OrderedDict

class BoardBlock(object):
    """
    Base object for sudoku board
    
    There are 9 Blocks on the sudoku board.
    """
    def __init__(self, squares=OrderedDict()):
        self.squares = squares            # OrderedDict( ( (x0,y0),[] ), ((x1,y1), []), ... , ((xn,yn), []) )
        self.position = ()
        
        #set position value
        for i in self.squares.keys():
            self.position = i
            break
        
    def __key(self):
        return (self.squares)

    def __eq__(x, y):
        return x.__key() == y.__key()

    def __hash__(self):
        return hash(self.__key())
        
    def group(self):
        """
        Return the possible-values list of the Block
        """
        return self.squares.values()
        
    def update_squares_from_group(self, group):
        """
        Update values of squares attribute
        """
        for index, key in enumerate(self.squares):
            self.squares[key] = group[index]
        return self.squares
        
class BoardBlockGroup(object):
    """
    Collection of three BoardBlock Objects
    
    * There are 6 Possible BoardBlockRows
    * Initiate the group by specifying three BoardBlocks in an tuple.
    * The members must make up three adjacent rows or columns.
    * Invalid groups are checked for. 
    * Orientation is calculated from the group members specified. 
    """
    
    def __init__(self, members):
        self.members = members
        self.row1 = OrderedDict()            # OrderedDict( ( (x0,y0),[] ), ((x1,y1), []), ... , ((xn,yn), []) )
        self.row2 = OrderedDict()
        self.row3 = OrderedDict()
        self.legal_combinations = ( ((0,0),(0,3),(0,6)),
                                    ((3,0),(3,3),(3,6)),
                                    ((6,0),(6,3),(6,6)),
                                    ((0,0),(3,0),(6,0)),
                                    ((0,3),(3,3),(6,3)),
                                    ((0,6),(3,6),(6,6)) )
            
        #instanciate only with three unique BoardBlock instances
        for i in (self.members[0], self.members[1], self.members[2]): 
            if not i.__class__.__name__ == "BoardBlock":
                raise BoardError('BoardBlockGroup must be instanciated with 3 unique BoardBlock Instances')
        if (self.members[0] == self.members[1] or self.members[1] == self.members[2]):
            raise BoardError('BoardBlockGroup must be instanciated with 3 unique BoardBlock instances')
            
        #BoardBlock instances must be adjacent group in a line
        if (self.members[0].position, self.members[1].position, self.members[2].position) not in self.legal_combinations:
            raise BoardError('BoardBlockGroup must be adjacent in a line')
            
        #generate row attributes
        
    def lines(self):
        '''
        Return three lines
        '''
        pass
    
class BoardError(Exception):
    def __init__(self, msg=''):
        self.msg = msg
        print self.msg

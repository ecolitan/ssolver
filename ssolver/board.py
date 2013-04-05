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
    def __init__(self,position=(),squares=OrderedDict()):
        self.position = position          # Position of Block 
        self.squares = squares            # OrderedDict( ( (x0,y0),[] ), ((x1,y1), []), ... , ((xn,yn), []) )
        
    def __key(self):
        return (self.position, self.squares)

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
        self.row_group1 = []
        self.row_group2 = []
        self.row_group3 = []
        
        for i in (self.members[0], self.members[1], self.members[2]): 
            if not i.__class__.__name__ == "BoardBlock":
                raise BoardError('BoardBlockGroup must be instanciated with 3 BoardBlock Instances')
    
class BoardError(Exception):
    def __init__(self, msg=''):
        self.msg = msg
        print self.msg

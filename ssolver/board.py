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
        
    def rows(self):
        """
        return rows
        """
        row1 = ((self.squares.items()[0],self.squares.items()[1],self.squares.items()[2]))
        row2 = ((self.squares.items()[3],self.squares.items()[4],self.squares.items()[5]))
        row3 = ((self.squares.items()[6],self.squares.items()[7],self.squares.items()[8]))
        return (row1,row2,row3)
            
    def cols(self):
        """
        return cols
        """
        col1 = ((self.squares.items()[0],self.squares.items()[3],self.squares.items()[6]))
        col2 = ((self.squares.items()[1],self.squares.items()[4],self.squares.items()[7]))
        col3 = ((self.squares.items()[2],self.squares.items()[5],self.squares.items()[8]))
        return (col1,col2,col3)
        
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
        self.rows = ()              # ( OrderedDict(), OrderedDict(), OrderedDict() )
        self.orientation = ''       # row or col
        self.row_mapper = { ((0,0),(0,3),(0,6)):(((0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8)),
                                                ((1,0),(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(1,7),(1,8)),
                                                ((2,0),(2,1),(2,2),(2,3),(2,4),(2,5),(2,6),(2,7),(2,8))),
                            ((3,0),(3,3),(3,6)):(((3,0),(3,1),(3,2),(3,3),(3,4),(3,5),(3,6),(3,7),(3,8)),
                                                ((4,0),(4,1),(4,2),(4,3),(4,4),(4,5),(4,6),(4,7),(4,8)),
                                                ((5,0),(5,1),(5,2),(5,3),(5,4),(5,5),(5,6),(5,7),(5,8))),
                            ((6,0),(6,3),(6,6)):(((6,0),(6,1),(6,2),(6,3),(6,4),(6,5),(6,6),(6,7),(6,8)),
                                                ((7,0),(7,1),(7,2),(7,3),(7,4),(7,5),(7,6),(7,7),(7,8)),
                                                ((8,0),(8,1),(8,2),(8,3),(8,4),(8,5),(8,6),(8,7),(8,8))),
                            ((0,0),(3,0),(6,0)):(((0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0)),
                                                ((0,1),(1,1),(2,1),(3,1),(4,1),(5,1),(6,1),(7,1),(8,1)),
                                                ((0,2),(1,2),(2,2),(3,2),(4,2),(5,2),(6,2),(7,2),(8,2))),
                            ((0,3),(3,3),(6,3)):(((0,3),(1,3),(2,3),(3,3),(4,3),(5,3),(6,3),(7,3),(8,3)),
                                                ((0,4),(1,4),(2,4),(3,4),(4,4),(5,4),(6,4),(7,4),(8,4)),
                                                ((0,5),(1,5),(2,5),(3,5),(4,5),(5,5),(6,5),(7,5),(8,5))),
                            ((0,6),(3,6),(6,6)):(((0,6),(1,6),(2,6),(3,6),(4,6),(5,6),(6,6),(7,6),(8,6)),
                                                ((0,7),(1,7),(2,7),(3,7),(4,7),(5,7),(6,7),(7,7),(8,7)),
                                                ((0,8),(1,8),(2,8),(3,8),(4,8),(5,8),(6,8),(7,8),(8,8)))}
        self.row_col = { ((0,0),(0,3),(0,6)):'row',
                         ((3,0),(3,3),(3,6)):'row',
                         ((6,0),(6,3),(6,6)):'row',
                         ((0,0),(3,0),(6,0)):'col',
                         ((0,3),(3,3),(6,3)):'col',
                         ((0,6),(3,6),(6,6)):'col'}
            
        #instanciate only with three unique BoardBlock instances
        for i in self.members: 
            if not i.__class__.__name__ == "BoardBlock":
                raise BoardError('BoardBlockGroup must be instanciated with 3 unique BoardBlock Instances')
        if (self.members[0] == self.members[1] or self.members[1] == self.members[2]):
            raise BoardError('BoardBlockGroup must be instanciated with 3 unique BoardBlock instances')
            
        #BoardBlock instances must be adjacent group in a line
        members_positions = (self.members[0].position, self.members[1].position, self.members[2].position)
        if members_positions not in self.row_mapper.keys():
            raise BoardError('BoardBlockGroup must be adjacent in a line')
        #Update orientation
        self.orientation = self.row_col[members_positions]
        
        #update long lines (called rows)
        self.rows = self.lines()
        
    def lines(self):
        '''
        Return three lines
        '''
        if self.orientation == 'col':
            line1_seg1 = self.members[0].cols()[0]
            line2_seg1 = self.members[0].cols()[1]
            line3_seg1 = self.members[0].cols()[2]
            line1_seg2 = self.members[1].cols()[0]
            line2_seg2 = self.members[1].cols()[1]
            line3_seg2 = self.members[1].cols()[2]
            line1_seg3 = self.members[2].cols()[0]
            line2_seg3 = self.members[2].cols()[1]
            line3_seg3 = self.members[2].cols()[2]
        elif self.orientation == 'row':
            line1_seg1 = self.members[0].rows()[0]
            line2_seg1 = self.members[0].rows()[1]
            line3_seg1 = self.members[0].rows()[2]
            line1_seg2 = self.members[1].rows()[0]
            line2_seg2 = self.members[1].rows()[1]
            line3_seg2 = self.members[1].rows()[2]
            line1_seg3 = self.members[2].rows()[0]
            line2_seg3 = self.members[2].rows()[1]
            line3_seg3 = self.members[2].rows()[2]
        line1 = OrderedDict(line1_seg1 + line1_seg2 + line1_seg3)
        line2 = OrderedDict(line2_seg1 + line2_seg2 + line2_seg3)
        line3 = OrderedDict(line3_seg1 + line3_seg2 + line3_seg3)
        return (line1, line2, line3)
    
class BoardError(Exception):
    def __init__(self, msg=''):
        self.msg = msg
        print self.msg

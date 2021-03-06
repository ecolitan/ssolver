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

import sys
import copy
from collections import Counter

class SSolver():
    def __init__(self):
        pass
        
    def test_group(self, group):
        """
        test group is valid
        """
        
        if (not len(group) == 9):
            raise DimError()
            
        if (not type(group) == list):
            raise DimError()
            
        for word in group:
            if not type(word) == list:
                raise DimError()
                
        return True
        
    def search_hidden_singles(self, group):
        """
        reduce group to find hidden singles
        leave other squares with reduced possible values lists
        """
        all_possibility = [1,2,3,4,5,6,7,8,9]
        known_numbers = []
        
        #reduce group until no further hidden_singles
        startgroup = []
        while not (group == startgroup):
            startgroup = copy.deepcopy(group)
            # find unique items in group
            u_elements = [k for k, v in Counter([item for sublist in group for item in sublist]).iteritems() if v == 1 ]
            for element in group:
                #if single value already in a square, add to known_numbers and continue
                if len(element) == 1:
                    known_numbers.append(element[0])
                    continue
                    
            for position, element in enumerate(group):
                #if square empty, square = all_possibility - known_numbers
                if len(element) == 0:
                    group[position] = list(set(all_possibility) - set(known_numbers))
                    
                #if square has multiple possibilities, square = possibility - known_numbers
                if len(element) >1:
                    group[position] = list(set(group[position]) - set(known_numbers))
                    
                    #if a number in square-possiblities is unique in the group, assign it
                    for number in element:
                        try:
                            if number in u_elements:
                                group[position] = [number]
                        except:
                            continue
        return group
                
    def search_locked_candidate_box(self, row_set):
        """
        find and reduce locked candidates in a box
        
        row_set must be a list of three adjacent boxes: [group1, group2, group3]
        these should already be reduced for hidden singles. 
        """
        pass
            
        
        
        
        
class DimError(Exception):
    def __init__(self, msg=''):
        self.msg = msg
        print self.msg









class SSolverOld():
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
                         
        self.cube0 = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
        self.cube1 = [[0, 3], [0, 4], [0, 5], [1, 3], [1, 4], [1, 5], [2, 3], [2, 4], [2, 5]]
        self.cube2 = [[0, 6], [0, 7], [0, 8], [1, 6], [1, 7], [1, 8], [2, 6], [2, 7], [2, 8]]
        self.cube3 = [[3, 0], [3, 1], [3, 2], [4, 0], [4, 1], [4, 2], [5, 0], [5, 1], [5, 2]]
        self.cube4 = [[3, 3], [3, 4], [3, 5], [4, 3], [4, 4], [4, 5], [5, 3], [5, 4], [5, 5]]
        self.cube5 = [[3, 6], [3, 7], [3, 8], [4, 6], [4, 7], [4, 8], [5, 6], [5, 7], [5, 8]]
        self.cube6 = [[6, 0], [6, 1], [6, 2], [7, 0], [7, 1], [7, 2], [8, 0], [8, 1], [8, 2]]
        self.cube7 = [[6, 3], [6, 4], [6, 5], [7, 3], [7, 4], [7, 5], [8, 3], [8, 4], [8, 5]]
        self.cube8 = [[6, 6], [6, 7], [6, 8], [7, 6], [7, 7], [7, 8], [8, 6], [8, 7], [8, 8]]
        
        self.row0 = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8]]
        self.row1 = [[1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8]]
        self.row2 = [[2, 0], [2, 1], [2, 2], [2, 3], [2, 4], [2, 5], [2, 6], [2, 7], [2, 8]]
        self.row3 = [[3, 0], [3, 1], [3, 2], [3, 3], [3, 4], [3, 5], [3, 6], [3, 7], [3, 8]]
        self.row4 = [[4, 0], [4, 1], [4, 2], [4, 3], [4, 4], [4, 5], [4, 6], [4, 7], [4, 8]]
        self.row5 = [[5, 0], [5, 1], [5, 2], [5, 3], [5, 4], [5, 5], [5, 6], [5, 7], [5, 8]]
        self.row6 = [[6, 0], [6, 1], [6, 2], [6, 3], [6, 4], [6, 5], [6, 6], [6, 7], [6, 8]]
        self.row7 = [[7, 0], [7, 1], [7, 2], [7, 3], [7, 4], [7, 5], [7, 6], [7, 7], [7, 8]]
        self.row8 = [[8, 0], [8, 1], [8, 2], [8, 3], [8, 4], [8, 5], [8, 6], [8, 7], [8, 8]]
        
        self.col0 = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0]]
        self.col1 = [[0, 1], [1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1]]
        self.col2 = [[0, 2], [1, 2], [2, 2], [3, 2], [4, 2], [5, 2], [6, 2], [7, 2], [8, 2]]
        self.col3 = [[0, 3], [1, 3], [2, 3], [3, 3], [4, 3], [5, 3], [6, 3], [7, 3], [8, 3]]
        self.col4 = [[0, 4], [1, 4], [2, 4], [3, 4], [4, 4], [5, 4], [6, 4], [7, 4], [8, 4]]
        self.col5 = [[0, 5], [1, 5], [2, 5], [3, 5], [4, 5], [5, 5], [6, 5], [7, 5], [8, 5]]
        self.col6 = [[0, 6], [1, 6], [2, 6], [3, 6], [4, 6], [5, 6], [6, 6], [7, 6], [8, 6]]
        self.col7 = [[0, 7], [1, 7], [2, 7], [3, 7], [4, 7], [5, 7], [6, 7], [7, 7], [8, 7]]
        self.col8 = [[0, 8], [1, 8], [2, 8], [3, 8], [4, 8], [5, 8], [6, 8], [7, 8], [8, 8]]
        
    def __str__(self):
        return unicode(self.position).encode('utf-8')
    
    def UpdatePosition(self, _positionvector):
        self.position = _positionvector
        
    def PrintPosition(self):
        """Print the current position"""
        for i in range(0,len(self.position)):
            print "Row",i,self.position[i]
        print '\n'
        
    def UpdateField(self, _ij, _n):
        """_ij is a list with coordinates
        n is the new number or list"""
        self.position[_ij[0]][_ij[1]] = _n
        
    def IsSolved(self):
        """Return true if position is solved"""
        for i in xrange(0,9):
            for j in xrange(0,9):
                if type(self.position[i][j]) is not int:
                    return False
        for _grouping in [self.cube0, self.cube1, self.cube2, self.cube3, self.cube4, self.cube5,
                            self.cube6, self.cube7, self.cube8, self.col0, self.col1, self.col2,
                            self.col3, self.col4, self.col5, self.col6, self.col7, self.col8,
                            self.row0, self.row1, self.row2, self.row3, self.row4, self.row5,
                            self.row6, self.row7, self.row8]:
            _poss = [1,2,3,4,5,6,7,8,9]
            for _ij in _grouping:
                if type(self.position[_ij[0]][_ij[1]]) is not int:
                    return False
                try:
                    _poss.remove(self.position[_ij[0]][_ij[1]])
                except ValueError:
                    print "Error: Solution Inconsistent!"
                    return False
            if _poss:
                return False
        return True
        
    def ConvertGroup(self, _group):
        for index, _ij in enumerate(_group):
            _group[index] = self.position[_ij[0]][_ij[1]]
        return _group
        
    def CheckConsistent(self, _group):
        """Check that a group (row,cube,col)is consistent"""
        _group = self.ConvertGroup(_group)
        for i in [1,2,3,4,5,6,7,8,9]:
            if _group.count(i) > 1:
                sys.exit("Inconsistent solution: {0}".format(_group))
        return True
        
    def MapCoordCube(self, _ij):
        """Return the cube that a coord belongs to."""
        for _cube in [self.cube0, self.cube1, self.cube2, self.cube3, self.cube4, self.cube5, self.cube6, self.cube7, self.cube8]:
            if _ij in _cube:
                return _cube
                
    def MapCoordCol(self, _ij):
        """Return the col that a coord belongs to."""
        for _col in [self.col0, self.col1, self.col2, self.col3, self.col4, self.col5, self.col6, self.col7, self.col8]:
            if _ij in _col:
                return _col
                
    def MapCoordRow(self, _ij):
        """Return the row that a coord belongs to."""
        for _row in [self.row0, self.row1, self.row2, self.row3, self.row4, self.row5, self.row6, self.row7, self.row8]:
            if _ij in _row:
                return _row
        
    def UpdateFieldPossibilies(self):
        """Create possibility lists and update position"""
        for i in xrange(0,9):
            for j in xrange(0,9):
                if self.position[i][j] is not None:
                    continue
                else:
                    _possibilites = [1,2,3,4,5,6,7,8,9]
                    print i, j
                    _cube = self.MapCoordCube([i, j])
                    print _cube
                    for _ij in _cube:
                        if type(self.position[_ij[0]][_ij[1]]) is int:
                            _possibilites = filter (lambda a: a != self.position[_ij[0]][_ij[1]], _possibilites)
                    self.CheckConsistent(_cube)
                    _row = self.MapCoordRow([i, j])
                    for _ij in _row:
                        if type(self.position[_ij[0]][_ij[1]]) is int:
                            _possibilites = filter (lambda a: a != self.position[_ij[0]][_ij[1]], _possibilites)
                    _col = self.MapCoordCol([i, j])
                    for _ij in _col:
                        if type(self.position[_ij[0]][_ij[1]]) is int:
                            _possibilites = filter (lambda a: a != self.position[_ij[0]][_ij[1]], _possibilites)
                if len(_possibilites) is 1:
                    _possibilites = _possibilites[0]
                self.UpdateField([i,j], _possibilites)
        
    def SearchHiddenSingles(self):
        """Search for hidden singles in cubes, rows and cols"""
        def updateSingles(_position_list):
            for _position in _position_list:
                _templist = []
                for _ij in _position:
                    if type(self.position[_ij[0]][_ij[1]]) is list:
                        _templist.append([_ij,self.position[_ij[0]][_ij[1]]])
                _catlist = []
                _singles = []
                for _list in _templist:
                    _catlist = _catlist + _list[1]
                for _poss in [1,2,3,4,5,6,7,8,9]:
                    if _catlist.count(_poss) == 1:
                        _singles.append(_poss)
                for _list in _templist:
                    for _poss in _singles:
                        if (_poss in _list[1]):
                            self.UpdateField(_list[0], _poss)
        updateSingles([self.cube0, self.cube1, self.cube2, self.cube3, self.cube4, self.cube5, self.cube6, self.cube7, self.cube8])
        updateSingles([self.row0, self.row1, self.row2, self.row3, self.row4, self.row5, self.row6, self.row7, self.row8])
        updateSingles([self.col0, self.col1, self.col2, self.col3, self.col4, self.col5, self.col6, self.col7, self.col8])



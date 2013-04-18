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

import unittest
import pickle
from collections import OrderedDict

from ssolver.ssolver import SSolver, DimError
from ssolver.board import BoardBlock, BoardBlockGroup, BoardError

class TestBoardBlock(unittest.TestCase):
    
    def setUp(self):
        pass
        
    def test_init(self):
        #__init__()
        base_attrs = {'position': (), 'squares': OrderedDict()}
        self.assertEqual(base_attrs, BoardBlock().__dict__)
        
    def test_group(self):
        #group()
        
        test_squares1 = OrderedDict(( ((0,0),[2]),
                                      ((0,1),[1,9]),
                                      ((0,2),[1,5,9]),
                                      ((1,0),[3]),
                                      ((1,1),[8]),
                                      ((1,2),[1,5,6,9]),
                                      ((2,0),[4]),
                                      ((2,1),[7]),
                                      ((2,2),[1,5,9]) ) )
        test_group1 = [ [2], [1,9], [1,5,9], [3], [8], [1,5,6,9], [4], [7], [1,5,9], ]
        test_block1 = BoardBlock(test_squares1)
        
        self.assertEqual(test_group1, test_block1.group())
        
    def test_update_squares_from_group(self):
        #update_squares_from_group()
        
        test_group2 = [[2], [1, 9], [1, 5, 9], [3], [8], [6], [4], [7], [1, 5, 9]]
        test_squares2 = OrderedDict(( ((0,0),[2]),
                                      ((0,1),[1,9]),
                                      ((0,2),[1,5,9]),
                                      ((1,0),[3]),
                                      ((1,1),[8]),
                                      ((1,2),[1,5,6,9]),
                                      ((2,0),[4]),
                                      ((2,1),[7]),
                                      ((2,2),[1,5,9]) ) )
        test_squares3 = OrderedDict(( ((0,0),[2]),
                                      ((0,1),[1,9]),
                                      ((0,2),[1,5,9]),
                                      ((1,0),[3]),
                                      ((1,1),[8]),
                                      ((1,2),[6]),
                                      ((2,0),[4]),
                                      ((2,1),[7]),
                                      ((2,2),[1,5,9]) ) )
        test_block2 = BoardBlock(test_squares2)
        self.assertEqual(test_squares3, test_block2.update_squares_from_group(test_group2))
        
    def test_hash(self):
        #test correct hashability of BoardBlock
        test_squares1 = OrderedDict(( ((0,0),[2]),
                                      ((0,1),[1,9]),
                                      ((0,2),[1,5,9]),
                                      ((1,0),[3]),
                                      ((1,1),[8]),
                                      ((1,2),[6]),
                                      ((2,0),[4]),
                                      ((2,1),[7]),
                                      ((2,2),[1,5,9]) ) )
        test_block1 = BoardBlock(test_squares1)
        test_block2 = BoardBlock(test_squares1)
            
        self.assertTrue(test_block1 == test_block2)
        
    def test_rows(self):
        #test BoardBlock correctly returns its rows
        test_squares1 = OrderedDict(( ((0,0),[2]),
                                      ((0,1),[1,9]),
                                      ((0,2),[1,5,9]),
                                      ((1,0),[3]),
                                      ((1,1),[8]),
                                      ((1,2),[6]),
                                      ((2,0),[4]),
                                      ((2,1),[7]),
                                      ((2,2),[1,5,9]) ) )
        test_block1 = BoardBlock(test_squares1)
        test_row1 = ((((0,0),[2]),((0,1),[1,9]),((0,2),[1,5,9])))
        test_row2 = ((((1,0),[3]),((1,1),[8]),((1,2),[6])))
        test_row3 = ((((2,0),[4]),((2,1),[7]),((2,2),[1,5,9])))
        self.assertEqual(test_block1.rows(), (test_row1, test_row2, test_row3))
        
    def test_cols(self):
        #test BoardBlock correctly returns its cols
        test_squares1 = OrderedDict(( ((0,0),[2]),
                                      ((0,1),[1,9]),
                                      ((0,2),[1,5,9]),
                                      ((1,0),[3]),
                                      ((1,1),[8]),
                                      ((1,2),[6]),
                                      ((2,0),[4]),
                                      ((2,1),[7]),
                                      ((2,2),[1,5,9]) ) )
        test_block1 = BoardBlock(test_squares1)
        test_col1 = ((((0,0),[2]),((1,0),[3]),((2,0),[4])))
        test_col2 = ((((0,1),[1,9]),((1,1),[8]),((2,1),[7])))
        test_col3 = ((((0,2),[1,5,9]),((1,2),[6]),((2,2),[1,5,9])))
        self.assertEqual(test_block1.cols(), (test_col1, test_col2, test_col3))
        
class TestBoardBlockGroup(unittest.TestCase):
    def SetUp(self):
        pass
        
    def test_init(self):
        #__init__()
        
        #raise if not instanciated correctly
        with self.assertRaises(BoardError):
            BoardBlockGroup([1,2,3])
        with self.assertRaises(TypeError):
            BoardBlockGroup(1)
        with self.assertRaises(IndexError):
            BoardBlockGroup([])
            
        #test that BoardBlock instances are unique
        test_squares1 = OrderedDict(( ((0,0),[2]),
                                      ((0,1),[1,9]),
                                      ((0,2),[1,5,9]),
                                      ((1,0),[3]),
                                      ((1,1),[8]),
                                      ((1,2),[6]),
                                      ((2,0),[4]),
                                      ((2,1),[7]),
                                      ((2,2),[1,5,9]) ) )
        test_block1 = BoardBlock(test_squares1)
        with self.assertRaises(BoardError):
            BoardBlockGroup((test_block1, test_block1, test_block1))
        
        #BoardBlock instances must be adjacent
        test_squares1 = OrderedDict(( ((0,0),[]),((0,1),[]),((0,2),[]),
                                      ((1,0),[]),((1,1),[]),((1,2),[]),
                                      ((2,0),[]),((2,1),[]),((2,2),[]) ) )
        test_squares2 = OrderedDict(( ((3,0),[]),((3,1),[]),((3,2),[]),
                                      ((4,0),[]),((4,1),[]),((4,2),[]),
                                      ((5,0),[]),((5,1),[]),((5,2),[]) ) )
        test_squares3 = OrderedDict(( ((6,0),[]),((6,1),[]),((6,2),[]),
                                      ((7,0),[]),((7,1),[]),((7,2),[]),
                                      ((8,0),[]),((8,1),[]),((8,2),[]) ) )
        test_squares4 = OrderedDict(( ((6,3),[]),((6,3),[]),((6,3),[]),
                                      ((7,4),[]),((7,4),[]),((7,4),[]),
                                      ((8,5),[]),((8,5),[]),((8,5),[]) ) )
        test_block1 = BoardBlock(test_squares1)
        test_block2 = BoardBlock(test_squares2)
        test_block3 = BoardBlock(test_squares3)
        test_block4 = BoardBlock(test_squares4)
        #not adjactent (raises BoardError)
        with self.assertRaises(BoardError):
            BoardBlockGroup((test_block1, test_block2, test_block4))
        
        #test correct orientation
        test_boardblock = BoardBlockGroup((test_block1, test_block2, test_block3))
        self.assertEqual('col', test_boardblock.orientation)
        
        #correctly calculate group rows
        test_boardblock = BoardBlockGroup((test_block1, test_block2, test_block3))
        test_row1 = OrderedDict(( ((0,0),[]),((1,0),[]),((2,0),[]),
                                  ((3,0),[]),((4,0),[]),((5,0),[]),
                                  ((6,0),[]),((7,0),[]),((8,0),[]) ) )
        test_row2 = OrderedDict(( ((0,1),[]),((1,1),[]),((2,1),[]),
                                  ((3,1),[]),((4,1),[]),((5,1),[]),
                                  ((6,1),[]),((7,1),[]),((8,1),[]) ) )
        test_row3 = OrderedDict(( ((0,2),[]),((1,2),[]),((2,2),[]),
                                  ((3,2),[]),((4,2),[]),((5,2),[]),
                                  ((6,2),[]),((7,2),[]),((8,2),[]) ) )
        self.assertEqual((test_row1, test_row2, test_row3), test_boardblock.rows)
        
    def test_lines(self):
        #lines()
        test_squares1 = OrderedDict(( ((0,0),[]),((0,1),[]),((0,2),[]),
                                      ((1,0),[]),((1,1),[]),((1,2),[]),
                                      ((2,0),[]),((2,1),[]),((2,2),[]) ) )
        test_squares2 = OrderedDict(( ((3,0),[]),((3,1),[]),((3,2),[]),
                                      ((4,0),[]),((4,1),[]),((4,2),[]),
                                      ((5,0),[]),((5,1),[]),((5,2),[]) ) )
        test_squares3 = OrderedDict(( ((6,0),[]),((6,1),[]),((6,2),[]),
                                      ((7,0),[]),((7,1),[]),((7,2),[]),
                                      ((8,0),[]),((8,1),[]),((8,2),[]) ) )
        test_block1 = BoardBlock(test_squares1)
        test_block2 = BoardBlock(test_squares2)
        test_block3 = BoardBlock(test_squares3)
        test_boardblock = BoardBlockGroup((test_block1, test_block2, test_block3))
        test_row1 = OrderedDict(( ((0,0),[]),((1,0),[]),((2,0),[]),
                                  ((3,0),[]),((4,0),[]),((5,0),[]),
                                  ((6,0),[]),((7,0),[]),((8,0),[]) ) )
        test_row2 = OrderedDict(( ((0,1),[]),((1,1),[]),((2,1),[]),
                                  ((3,1),[]),((4,1),[]),((5,1),[]),
                                  ((6,1),[]),((7,1),[]),((8,1),[]) ) )
        test_row3 = OrderedDict(( ((0,2),[]),((1,2),[]),((2,2),[]),
                                  ((3,2),[]),((4,2),[]),((5,2),[]),
                                  ((6,2),[]),((7,2),[]),((8,2),[]) ) )
            
        self.assertEqual((test_row1, test_row2, test_row3), test_boardblock.lines())
        
#TODO Extend suite
suite1 = unittest.TestLoader().loadTestsFromTestCase(TestBoardBlockGroup)
suite2 = unittest.TestLoader().loadTestsFromTestCase(TestBoardBlock)
unittest.TextTestRunner(verbosity=2).run(suite1)
unittest.TextTestRunner(verbosity=2).run(suite2)


        

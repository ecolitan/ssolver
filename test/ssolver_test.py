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
from ssolver.ssolver import SSolver, DimError

class TestSSolver(unittest.TestCase):
    
    def setUp(self):
        pass
        
    def sort_nested(self, group):
        group.sort()
        for i in group:
            i.sort()
        return group
        
    def test_test_group(self):
        # test_group([group])
        
        bad_group1 = [[],[]]
        bad_group2 = 'abc123ab'
        bad_group3 = [ [],[],[],[],[],'',[],[],[] ]
        bad_group4 = [ [1],[1],[],[],[],[],[],[],[] ]
        
        good_group = [ [],[],[],[],[],[],[],[],[] ]
        
        #raise DimError if group wrong size
        self.assertRaises(DimError, SSolver().test_group, bad_group1)
        #raise DimError if group wrong type
        self.assertRaises(DimError, SSolver().test_group, bad_group2)
        #raise DimError all elements not lists
        self.assertRaises(DimError, SSolver().test_group, bad_group3)
        
        #TODO
        #raise DimError if group is inconsistent (cannot have same number twice)
        #self.assertRaises(DimError, SSolver().test_group, bad_group4)
        
        #good groups should return True
        self.assertTrue(SSolver().test_group(good_group))
        
    def test_fill_group(self):
        # fill_group([group])
        
        test1   = [ [],[],[],[],[],[],[],[],[] ]
        result1 = [ [1,2,3,4,5,6,7,8,9],
                    [1,2,3,4,5,6,7,8,9],
                    [1,2,3,4,5,6,7,8,9],
                    [1,2,3,4,5,6,7,8,9],
                    [1,2,3,4,5,6,7,8,9],
                    [1,2,3,4,5,6,7,8,9],
                    [1,2,3,4,5,6,7,8,9],
                    [1,2,3,4,5,6,7,8,9],
                    [1,2,3,4,5,6,7,8,9] ]
                    
        test2 =   [ [1],
                    [1,2,3,4,5,6,7,8,9],
                    [1,2,3,4,5,6,7,8,9],
                    [1,2,3,4,5,6,7,8,9],
                    [1,2,3,4,5,6,7,8,9],
                    [1,2,3,4,5,6,7,8,9],
                    [1,2,3,4,5,6,7,8,9],
                    [1,2,3,4,5,6,7,8,9],
                    [1,2,3,4,5,6,7,8,9] ]
        result2 = [ [1],
                    [2,3,4,5,6,7,8,9],
                    [2,3,4,5,6,7,8,9],
                    [2,3,4,5,6,7,8,9],
                    [2,3,4,5,6,7,8,9],
                    [2,3,4,5,6,7,8,9],
                    [2,3,4,5,6,7,8,9],
                    [2,3,4,5,6,7,8,9],
                    [2,3,4,5,6,7,8,9] ]
                    
        test3   = [ [1],[2],[3],[4],[5],[6],[7],[8],[9] ]
        result3 = [ [1],[2],[3],[4],[5],[6],[7],[8],[9] ]
                            
        self.assertEqual(result1, SSolver().fill_group(test1))
        self.assertEqual(result2, SSolver().fill_group(test2))
        self.assertEqual(result3, SSolver().fill_group(test3))
        
        
    #~ def test_search_hidden_singles(self):
        #~ #search_hidden_singles()
        #~ 
        #~ test1 =   [ [1],
                    #~ [2,3],
                    #~ [3,4],
                    #~ [5],
                    #~ [6,7,8,9],
                    #~ [6,7,8,9],
                    #~ [6,7,8,9],
                    #~ [6,7,8,9],
                    #~ [4,6,7,8,9] ]
        #~ result1 = [ [1],
                    #~ [2],
                    #~ [3],
                    #~ [5],
                    #~ [6,7,8,9],
                    #~ [6,7,8,9],
                    #~ [6,7,8,9],
                    #~ [6,7,8,9],
                    #~ [4] ]
                    #~ 
        #~ test2 =   [ [1],
                    #~ [1,2],
                    #~ [2,3],
                    #~ [3,4],
                    #~ [4,5],
                    #~ [5,6],
                    #~ [6,7],
                    #~ [7,8],
                    #~ [8,9], ]
        #~ result2 = [ [1],
                    #~ [2],
                    #~ [3],
                    #~ [4],
                    #~ [5],
                    #~ [6],
                    #~ [7],
                    #~ [8],
                    #~ [9] ]
                    #~ 
        #~ #order not important for this test
        #~ self.assertEqual(self.sort_nested(result1), self.sort_nested(SSolver().fill_group(test1)))
        #~ self.assertEqual(result2, SSolver().fill_group(test2))


suite = unittest.TestLoader().loadTestsFromTestCase(TestSSolver)
unittest.TextTestRunner(verbosity=2).run(suite)

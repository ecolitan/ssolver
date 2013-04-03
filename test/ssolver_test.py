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
        
    def test_search_hidden_singles(self):
        # search_hidden_singles([group])
        
        def sort_nested(group):
            """To test equality of nested lists regardless of ordering"""
            group.sort()
            for i in group:
                i.sort()
            return group
        
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
        
        test4 =   [ [1],
                    [2,3],
                    [3,4],
                    [5],
                    [6,7,8,9],
                    [6,7,8,9],
                    [6,7,8,9],
                    [6,7,8,9],
                    [4,6,7,8,9] ]
        result4 = [ [1],
                    [2],
                    [3],
                    [5],
                    [6,7,8,9],
                    [6,7,8,9],
                    [6,7,8,9],
                    [6,7,8,9],
                    [4] ]
                    
        test5 =   [ [1],
                    [1,2],
                    [2,3],
                    [3,4],
                    [4,5],
                    [5,6],
                    [6,7],
                    [7,8],
                    [8,9], ]
        result5 = [ [1],
                    [2],
                    [3],
                    [4],
                    [5],
                    [6],
                    [7],
                    [8],
                    [9] ]
                    
        test6 = [[2], [1, 9], [1, 5, 9], [3], [8], [1, 5, 6, 9], [4], [7], [1, 5, 9]]
        result6 = [[2], [1, 9], [1, 5, 9], [3], [8], [6], [4], [7], [1, 5, 9]]
        
        #test return of basic groups
        self.assertEqual(result1, SSolver().search_hidden_singles(test1))
        self.assertEqual(result2, SSolver().search_hidden_singles(test2))
        self.assertEqual(result3, SSolver().search_hidden_singles(test3))
        
        #test finding hidden singles
        #order not important for this test
        self.assertEqual(sort_nested(result4), sort_nested(SSolver().search_hidden_singles(test4)))
        self.assertEqual(result5, SSolver().search_hidden_singles(test5))
        self.assertEqual(result6, SSolver().search_hidden_singles(test6))
        
    def test_search_locked_candidate_box(self):
        #search_locked_candidate_box()
        pass
        test_group1 = [ [1,6],[1,5,7,8],[1,5,7],[1,4,3],[1,3,4,5,7,8],[2],[1,4,6],[9],[1,4,5] ]
        test_group2 = [ [9],[1,2,5,7,8],[1,2,5,8],[6],[1,4,5,7,8],[1,5,8],[2,4,5],[1,2,4,5,8],[3] ]
        test_group3 = [ [4],[3],[1,5,6,8],[9],[5,8],[1,5,8],[2,6,8],[2,5,6,8],[7] ]
        test_row_set1 = [test_group1, test_group2, test_group3]
        
        #TODO
        
        result_group1 = [ [1,6],[1,5,7,8],[1,5,7],[1,4,3],[1,3,4,5,7,8],[2],[1,4,6],[9],[1,4,5] ]
        result_group2 = [ [9],[1,2,5,7,8],[1,2,5,8],[6],[1,4,5,7,8],[1,5,8],[2,4,5],[1,2,4,5,8],[3] ]
        result_group3 = [ [4],[3],[1,5,6,8],[9],[5,8],[1,5,8],[2,6,8],[2,5,6,8],[7] ]
        result_row_set1 = [result_group1, result_group2, result_group3]
        
        
    
suite = unittest.TestLoader().loadTestsFromTestCase(TestSSolver)
unittest.TextTestRunner(verbosity=2).run(suite)

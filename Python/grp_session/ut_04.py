import unittest
import ut_fns_04 

class MyTest(unittest.TestCase):

    def test_count(self):
        binary = 1010111011
        length = ut_fns_04.FindLength(binary)
        self.assertEqual(length, 3)
    def test_number(self):
        string = 'nf3124fsf9823'
        ph_no = ut_fns_04.number(string)
        self.assertEqual(ph_no, '31249823fs')
    def test_MatrixSwap(self):
        listt = [[2,7,1,8],
                 [1,9,5,0],
                 [3,6,7,8]]
        swapped = ut_fns_04.swap(listt)
        self.assertEqual(swapped, [[2,7,1,8],
                                   [1,7,6,0],
                                   [3,9,5,8]])        
if __name__ == '__main__':
    unittest.main()
    

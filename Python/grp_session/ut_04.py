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
        
if __name__ == '__main__':
    unittest.main()
    
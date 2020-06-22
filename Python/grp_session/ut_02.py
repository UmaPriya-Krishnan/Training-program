import unittest
import ut_fns_02

class MyTest(unittest.TestCase):
    def test_btd(self):
        str1 = '10'
        str2 = '01'
        status = ut_fns_02.btd(str1, str2)
        self.assertEqual(status, 9)
    def test_plaindrome(self):
        string = 'malayalam'
        status = ut_fns_02.isPal(string)
        self.assertEqual(status, True)
    def test_plaindrome_neg(self):
        string = 'python'
        status = ut_fns_02.isPal(string)
        self.assertEqual(status,False)
    def test_yr(self):
        yr = 2000
        result = ut_fns_02.date(yr)
        self.assertEqual(result,(30, 10950, 262800, 15768000, 946080000))

if __name__ == '__main__':
    unittest.main()  
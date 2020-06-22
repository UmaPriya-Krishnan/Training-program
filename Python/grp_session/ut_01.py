import unittest
import ut_fns_01

class MyTest(unittest.TestCase):
    def test_count(self):
        str1 = 'Hey there'
        status = ut_fns_01.count(str1)
        self.assertEqual(status, {'h': 2,'y': 1,'e': 3,' ': 1,'t': 1,'r': 1})
    def test_is_numeric(self):
        string = 'python3.8'
        status = ut_fns_01.is_numeric(string)
        self.assertEqual(status, '38')
    def test_consonant(self):
        string = 'python'
        result = ut_fns_01.consonant(string)
        self.assertEqual(result,'pyth')

if __name__ == '__main__':
    unittest.main()  
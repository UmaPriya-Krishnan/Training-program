import unittest
import ut_fns_03

class MyTest(unittest.TestCase):
    def test_count(self):
        s ='I like coffee'
        status = ut_fns_03.count(s)
        self.assertEqual(status,{'I': 1, 'like': 2, 'coffee': 3})
        
    def test_MatSum_2(self):
        list1 = [[1,2],
                [1,2]]
        list2 = [[1,2],
                [1,2]]
        status = ut_fns_03.mat_sum2(list1,list2)
        self.assertEqual(status, [[2, 4], [2, 4]])
        
    def test_MatMul_2(self):
        list1 = [[1,2],
                [1,2]]
        list2 = [[1,2],
                [1,2]]
        status = ut_fns_03.mat_mul2(list1,list2)
        self.assertEqual(status, [[1, 4], [1, 4]])
        
    def test_MatSum_3(self):
        list1 = [[1,2,3],
                [1,2,3],
                [1,2,3]]
        list2 = [[1,2,3],
                [1,2,3],
                [1,2,3]]
        status = ut_fns_03.mat_sum3(list1,list2)
        self.assertEqual(status, [[2, 4, 6], [2, 4, 6], [2, 4, 6]])
        
    def test_MatMul_3(self):
        list1 = [[1,2,3],
                [1,2,3],
                [1,2,3]]
        list2 = [[1,2,3],
                [1,2,3],
                [1,2,3]]
        status = ut_fns_03.mat_mul3(list1,list2)
        self.assertEqual(status, [[1, 4, 9], [1, 4, 9], [1, 4, 9]])
        
if __name__ == '__main__':
    unittest.main()  
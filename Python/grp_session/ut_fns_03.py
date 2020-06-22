def VowelCount(s):
    ct = 0
    vowel = 'aeiouAEIOU'
    for i in s:
        if i in vowel:
            ct+=1
    return ct
def count(s):
    listt = s.split(' ')
    d={}
    vowel = 'aeiouAEIOU'
    for i in listt:
       d[i] = VowelCount(i)
    return d

s = 'I Am Writing'
count(s)



def mat_sum2(list1,list2):
    sum=[[0,0],
         [0,0]]
    for i in range(len(list1)):
        for j in range(len(list1[0])):
            sum[i][j] = list1[i][j]+list2[i][j]
    return sum
list1 = [[1,2],
         [1,2]]
list2 = [[1,2],
         [1,2]]
mat_sum2(list1,list2)



def mat_mul2(list1,list2):
    product = [[0,0],
               [0,0]]
    for i in range(len(list1)):
        for j in range(len(list1[0])):
            product[i][j] = list1[i][j]*list2[i][j]
    return product
list1 = [[5,3],
         [1,2]]
list2 = [[1,0],
         [3,2]]
mat_mul2(list1,list2)



def mat_sum3(list1,list2):
    sum=[[0,0,0],
         [0,0,0],
         [0,0,0]]
    for i in range(len(list1)):
        for j in range(len(list1[0])):
            sum[i][j] = list1[i][j]+list2[i][j]
    return sum
    
list1 = [[1,6,3],
         [1,2,3],
         [6,2,2]]
list2 = [[1,1,3],
         [7,6,4],
         [5,2,3]]
mat_sum3(list1,list2)


def mat_mul3(list1,list2):
    product = [[0,0,0],
               [0,0,0],
               [0,0,0]]
    for i in range(len(list1)):
        for j in range(len(list1[0])):
            product[i][j] = list1[i][j]*list2[i][j]
    return product
list1 = [[7,3,3],
         [0,2,2],
         [8,2,1]]
list2 = [[8,6,3],
         [1,5,2],
         [0,2,3]]
mat_mul3(list1,list2)


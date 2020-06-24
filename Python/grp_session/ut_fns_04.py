def FindLength(binary):
    binary = str(binary)
    bin_list = []
    for i in binary:
        bin_list.append(i)
        count = 0
        lis = []
        i = 0
    while i < len(binary):
        if binary[i] == 1 or binary[i] == '1':
            count+=1
            lis.append(count)
        else: 
            count = 0
        i+=1
    return max(lis)

binary = 101111
FindLength(binary)

def number(string):
    l = []
    for i in string:
        if i.isnumeric():
            l.append(i)
        length = len(l)
        al = []
        al = [al for al in string if al.isalpha()]
    for i in al[::-1]:
        if length < 10 and i.isalpha():
            l.append(i)
        length+=1
    no = ''.join(l)
    return no
    
number('abcd123ef45')

def swap(a):
    row = len(a)-1
    for i in range(row,-1,-1):
        col = len(a[i]) -1
        for j in range(1,col):
            if i == row-1 and j == col-2:
                temp = a[i][j] #A11
                a[i][j] = a[i+1][j+1]   #A11 = A21
                a[i+1][j+1] = a[i][j+1] #A22 = A12
                a[i][j+1] = a[i+1][j]   #A12 = A21
                a[i+1][j] = temp        #A11 = A21 A12 = A22 A21 = A11 A22 = A12 
    return a
a = [[1, 2, 3, 4], 
    [7, 8, 9, 10], 
    [11, 12, 13, 14]]
swap(a)

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
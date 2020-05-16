a = int(input('Enter your 1st integer: '))
b = int(input('Enter your 2nd integer: '))
c = int(input('Enter your 3rd integer: '))
d = int(input('Enter your 4th integer: '))
e = int(input('Enter your 5th integer: '))
f = int(input('Enter your 6th integer: '))
g = int(input('Enter your 7th integer: '))
h = int(input('Enter your 8th integer: '))
i = int(input('Enter your 9th integer: '))
j = int(input('Enter your 10th integer: '))

for num in (a,b,c,d,e,f,g,h,i,j):

 if num%2 ==0:
    num = 0  
 else:
    num = num
value = a, b, c, d, e, f, g, h, i, j
max = max(value)
if max ==0:
    print ('All the integers entered, are even.')
else: 
    print (max, 'is the largest odd number.')

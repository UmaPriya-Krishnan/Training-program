def division(list1):
    '''To print the numbers  which are divisible by 7 but not a multiple of 5 with in the given range 
    return the result as comma separated sequence'''
    list2 = []
    count=0
    for i in list1:
        if i%7 == 0 and i%5 != 0:
            list2.append(i)
    print99oh (list2)
print('\n',division.__doc__)
list1 = range(5000,7501)
division(list1)



def convert(value):
    '''Conversion of set of comma separated values into lists and tuples which contains every number'''
    value1= value.split(',')
    list1 = list(value1)
    tup = tuple(value1)
    print(list1)
    print(tup)
print('\n',convert.__doc__)
value = ("34,67,55,48,45")
convert(value)


def fibonacci(n):
    '''To generate the fibonacci series for the given integer 
    each number is the sum of the two preceding ones, starting from 0 and 1'''
    i,a,b = 0,0,1
    c = 0
    if n>0:
        while i < n:
            print(a)
            c = a+b
            a=b
            b=c
            i+=1            
    else:
        print("Please Enter a positive integer")
print('\n',fibonacci.__doc__)       
fibonacci(11)            


#To open a partiular file and display the names of fucntions alone
with open("C:\\Users\\mohan\\Desktop\\Virtual training\\day8_function.py" , "r") as r_object:
    out = r_object.readlines()
    for lines in out:
        if 'def' in lines:
        #if lines.startswith('def'):
            s = lines[3:]
            #print(s)
            s1 = s.split('(')
            print(s1[0])

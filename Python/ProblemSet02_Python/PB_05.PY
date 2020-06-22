def sumDigit(s):
    x=0
    for i in s:
        if i.isdigit():
            i=int(i)
            x = x+i
    print("The sum of num is " ,x)
s = str(input("Enter any string: "))
sumDigit(s)  
#USING MATH FUNCTION
import math  
a = int(input("Enter any number: "))
b = int(input("Enter another number: "))
print (math.gcd(a,b))

#ALTERNATE CODE:
def GCD(a,b):
    if b<=a:
        rem = a%b
        if rem == 0:
            return "GCD is {}".format(b)  
        else:
            gcd = 1
            return "gcd is {}" .format(gcd)
    else:
        rem = a%b
        return GCD(b,rem)
a = int(input("Enter any number: "))
b = int(input("Enter another number: "))
print(GCD(a,b))

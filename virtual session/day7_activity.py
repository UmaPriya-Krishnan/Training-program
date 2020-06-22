def sumDigit(s):
    ''' This gunction returns the sum of the digits present in the string'''
    x=0
    for i in s:
        if i.isdigit():
            i=int(i)
            x = x+i
    print("The sum of num is " ,x)
s = str(input("Enter any string: "))
sumDigit(s)  




def isPalindrome(s):
    '''This function checks whether the entered string is palindrome(even if spelled backwards the word remains the same) or not '''
    if s == s[::-1]:
        print("The given string is a palindrome")
    else:
        print("The given string is not a Palindrome")
s = str(input("\nEnter any string: "))
isPalindrome(s)


def binToDec(binary):
    '''this function converts the input binary number to decimal'''
    my_string = str(binary)
    y = my_string.count('0')
    x = my_string.count('1')
    if  x+y == len(my_string):
        #print('True')    
        dec, i, n = 0, 0, 0
        while(binary):
            rem = binary%10
            dec = dec+(rem*pow(2, i))
            binary = (binary//10)
            i+=1
        print("\nThe decimal equivalent is: " ,dec)

binary = int(input("\nEnter the binary number: "))
binToDec(binary)




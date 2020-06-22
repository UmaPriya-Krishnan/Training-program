def isPalindrome(s):
    if s == s[::-1]:
        print("The given string is a palindrome")
    else:
        print("The given string is not a Palindrome")
s = str(input("Enter any string: "))
isPalindrome(s)
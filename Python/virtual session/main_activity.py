#To download a page from web and print particular lines:

import requests
def get_method(url):
    ''' This function gets the url and checks whether the status code is 200 which means that the request has succeeded '''
    print(get_method.__doc__)
    resp = requests.get(url, verify = False)
    if resp.status_code in [200, '200']:
        return (resp.content) 

def write_file(filename, data):
    ''' Creates a new file with the given filename and writes the data found in the url in the new file'''
    print(write_file.__doc__)
    with open(filename,'wb') as w_obj:
        w_obj.write(data)
    return False
    
def open_file(fn):
    ''' This function opens the file mentioned in the path and checks for the conditions given and returns the line which satisfies the conditions'''
    print(open_file.__doc__)
    list1 = []
    with open(fn, "rb") as r_object:
        out = r_object.readlines()
        for line in out:
            if b"<li>" in line and len(line)> 25 and len(line)<=45 :
                list1.append(line)
                s1 = line.lstrip(b'<li>')
                s2 = s1.lstrip(b'ul><li>')
                s3 = s2.rstrip(b'</li>\n')
                s4 = s3.rstrip(b'</li></u')
                s5= s4.decode('utf-8')
                print(s5)
                
fn = "C:\\Users\\mohan\\Desktop\\Virtual training\\Python_guide.html"               
data = get_method("https://en.wikipedia.org/wiki/Python_(programming_language)")
status = write_file("Python_guide.html", data)
open_file(fn)
__________________________________________________________________________________________________________________________________________________________________

#1. To check the values of two inputs given to a function

def check(input1,input2):
    '''This function checks whether the two inputs are present and the values of the input and prints the output accordingly'''
    if input1 != '':
        print("Input1: Mandatory input is present")
        if input2 == '':
            input2 = 1
            print("Input2: Not present/Null/n The value of 2nd input is updated to : ",input2)
        elif input2 in [0 or '0']:
            print("Input2: Error(The value is 0)")
        else:
            print("Input2: The value of second input is neither 1 nor 0")
    else:
        print("Input1: Mandatory input is missing")
input1 = input("Enter any value: ")
input2 = input("Enter any value: ")
print("\ncheck:",check.__doc__)
check(input1,input2)

            
__________________________________________________________________________________________________________________________________________________________________

#2. To perform swapcase in a string without using built-in functions

def upperCase(i):
    ''' This function swaps the case of the input from lower to upper case'''
    a = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for x in i:
        swapped = a[a.index(x)+26]
    return swapped

def lowerCase(i):
    ''' This function swaps the case of the input from upper to lower case'''
    a = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for x in i:
        swapped= a[a.index(x)-26]
    return swapped

def swapCase(name):
    '''This function swaps the cases of the letters in the given string using the "upperCase" and "lowerCase" functions'''
    if name.isalpha():
        for i in name:
            if i in alpha:
                x = upperCase(i)
                print(x)
            else:
                x = lowerCase(i)
                print(x)
    else:
        print("The entered string has non alphaetical characters.\nPlease enter a valid string")

name = str(input("Enter a string: "))
alpha = 'abcdefghijklmnopqrstuvwxyz'
print("upperCase:",upperCase.__doc__)
print("lowerCase:",lowerCase.__doc__)
print("swapCase:",swapCase.__doc__)
swapCase(name)

___________________________________________________________________________________________________________________________________________

#3. To check whether the letters in a string are in alphabetical order 

def is_abcedarian(string):
    ''' This function is to check whether the given string has the letters in aplhabetical order'''
    string = string.lower()
    i = 0
    if string.isalpha():
        while i < len(string)-1:
            if string[i] > string[i+1]:
                return False
            i+=1
        return True
    else:
        print("Warning!!!\nPlease enter a valid string with alphabetial characters only")
import string
string = str(input("Enter any string: "))
print("is_abcedarian:",is_abcedarian.__doc__)
print(is_abcedarian(string))

_________________________________________________________________________________________________________________________________________

#4. To convert Celsius to Fahrenheit and vice versa

def celToFahr(cel):
    '''This function converts the temperature value entered in celcius to degree fahrenheit
    The formula for this conversion is  (x°C × 9/5) + 32 =  y°F'''

    fahr = (cel*(9/5))+32
    return fahr
    
def fahrToCel(fahr):
    '''This function converts the temperature value entered in celcius to degree fahrenheit
    The formula for this conversion is  (y°F − 32) × 5/9 = x°C'''

    cel = (5/9) * (converted_f - 32)
    return cel
    
cel = float(input("Enter the value in Celsius: "))
converted_f = celToFahr(cel)
converted_c = fahrToCel(converted_f)
print("celToFahr:",celToFahr.__doc__)
print("\nThe equivalent value for {}°C in Fahrenheit is {:.2f}°F\n" .format(cel,converted_f))
print("fahrToCel:",fahrToCel.__doc__)
print("\nThe equivalent value for {:.2f}°F in Celcius is {:.2f}°C\n" .format(converted_f,converted_c))

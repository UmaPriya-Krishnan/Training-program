#To check whether the word 'coffee' is present in the string 'I drink coffee every morning'

string = "I drink coffee every morning"
print("PROBLEM_01")
print('coffee' in string)    #Returns true or false
print(string.find('coffee')) #Returns the index of the substring (if not present returns -1)

#Print the alphabet after the first occurence of ',' from the below string 'I like python,Perl scripting'

string1 = 'I like python,Perl scripting'
sub = string1.split(',')
alpha = sub[1]
print("\nPROBLEM_02")
print(alpha[0:1:])



#Get your fullname and convert the first and middle name as abbreviations 

name = 'uma priya krishnan'
name_abb = name[0].upper() + "." + name[4].upper() + "." + name[10:].capitalize()
print("\nPROBLEM_03")
print(name_abb)

#----------alternate way---------

name = 'Uma Priya Krishnan'
sub2 = list(name.split(" "))
fname = sub2[0][0]
sname = sub2[1][0]
print("\nPROBLEM_03")
print(fname + "." + sname + "." + sub2[2])


#Count the no. of whitespaces 'Vect1 and Vect2 are lists of equal length of numbers'
string2 = 'Vect1 and Vect2 are lists of equal length of numbers'
print("\nPROBLEM_04")
print(string2.count(' '))


#i have a string -> str1 = "PYnative" - Use slicing to get the op like this: Yna PYnat tive PYnativ PYnativ
str1="PYnative" 
#sliced_string = str1[1:4] + " " + str1[0:5] + " " + str1[4:] + " " + str1[0:7]*2
sliced_string = str1[1:4] + " " + str1[0:5] + " " + str1[4:] + " " + str1[0:7] + " " + str1[0:7] 
print("\nPROBLEM_05")
print(sliced_string)


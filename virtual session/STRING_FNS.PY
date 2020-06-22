'''
#1. TO CAPITALIZE THE FIRST CHAR IN A STRING:
# -returns only a copy of the string with first char capitalized
my_string = "hey, I am from Vellore"
print("\n---------------------------CAPITALIZE FUNCTION----------------------")
print(my_string.capitalize())


#2. centered in a string of length width -copy only
#default filler is "space"
string = 'hello'
print("\n-----------------------------CENTER FUNCTION------------------------")
print(string.center(20,'U'))
print(string)
'''
#3. TO COUNT THE NUMBER OF OCCURENCES OF A SUB STRING IN A STRING:
#str.count('<substring>',starting index,ending index)----to find the total count, without indices give just the substring
#default value for start index is 0 and end index is last index of the string
my_string = "hey, I am from Vellore"
sub = 'll'
print("\n--------------------------------COUNT--------------------------------")
print(my_string.count(sub, 3,16))
'''
#4. TO CHECK WHETHER THE SLICED STRING ENDS WITH PARTICULAR SUBSTRING
#(IF no indices are given it will always returns false other than the last word in the string!7!!
string1 = "Hey, How are you doing?"
print("\n-------------------------------ENDSWITH------------------------------")
print(string1.endswith('are',3,12))
print(string1.endswith('doing'))
print(string1.endswith('doing?'))


#5. TO FIND THE INDEX OF THE SUBSTRING IN A GIVEN STRING:
#Returns the index value if the string is found, else returns -1
string2 = "Hey, How's life?"
sub = "life"
print("\n---------------------------------FIND--------------------------------")
print(string2.find(sub,0))         #only start index value given
print(string2.find('Heyy',0,12))   #substing is given directly
print(string2.find(sub,0,7))       #both start and end index are given
print(string2.find('Ho'))          #Neither start and end index are given

#6. TO FIND THE INDEX OF THE SUBSTRING IN A GIVEN STRING:(Raises an exception when the given substring is not found):
string2 = "Hey, How's life?"
sub = "life"
print("\n----------------------------------INDEX------------------------------")
print(string2.index(sub,0))         #only start index value given
#print(string2.index('Heyy',0,12))   #substring is given directly

#7. TO CHECK WHETHER THE STRING CONSISTS OF ALPHANUMERIC CHARACTERS ONLY:
string3 = "WelcomeToTheFutureTheDateIs24thdec2040"
string4 = '24thDec2040'          #Due to the spaces inbetween, the result will be False
print("\n-----------------------------IS ALPHANUMERIC-------------------------")
print(string3.isalnum())
print(string4.isalnum())

#8. TO CHECK WHETHER THE STRING CONSISTS OF ALPHABETIC CHARACTERS ONLY:
string3 = "WelcomeToTheFuture"
string4 = 'december'
print("\n---------------------------------IS ALPHA----------------------------")          
print(string3.isalpha())
print(string4.isalpha())

#9. TO CHECK WHETHER THE STRING CONSISTS OF NUMERIC VALUES ONLY:
string3 = "27052020"
string4 = 'december20' 
print("\n---------------------------------IS DIGIT----------------------------")         
print(string3.isdigit())
print(string4.isdigit())

#10. TO CHECK WHETHER ALL THE LETTERS IN THE STRING ARE IN LOWER CASE:
string3 = " This is not the correct format!!!"
string4 = "it's too sunny here!!" 
print("\n--------------------------------IS LOWERCASE-------------------------")         
print(string3.islower())
print(string4.islower())

#11. TO CHECK WHETHER ALL THE LETTERS IN THE STRING ARE IN LOWER CASE:
string3 = " SURPRISE!!!"
string4 = "It's too sunny here!!" 
print("\n-------------------------------IS UPPER CASE-------------------------")         
print(string3.isupper())
print(string4.isupper())

#12. TO CHECK WHETHER THE STRING CONSISTS OF WHITESPACE CHARACTERS ONLY:
string3 = " This is not the correct format!!!"
string4 = ""
string5 = "            "
print("\n------------------------------IS WHITESPACE--------------------------")
print(string3.isspace())
print(string4.isspace())
print(string5.isspace())

#13. TO CHECK WHETHER THE STRING CONSISTS OF TITLE CASE CHARACTERS(only the first letter of each word should be in upper case) ONLY:
string3 = " This Is The Correct Format!!!"
string4 = "And this is not"
string5 = "I AM UMA"
print("\n-------------------------------IS TITLE CASE--------------------------")
print(string3.istitle())
print(string4.istitle())
print(string5.istitle())


#14. TO JOIN A SEQUENCE OF STRINGS USING THE GIVEN SEPARATOR:
vowels = ('a','e','i','o','u')
sep = ','
print("\n-----------------------------------JOIN-------------------------------")
print(sep.join(vowels))

#15. To FIND THE LENGTH OF A STRING:
string1 = 'Hey there'
print("\n---------------------------------LENGTH-------------------------------")
print(len(string1))

#16. TO CONVERT ALL THE CHARACTERS IN STRING TO LOWER CASE:
string1 = 'Hey THERE'
print("\n-----------------------------TO LOWER CASE----------------------------")
print(string1.lower())

#17. TO CONVERT ALL THE CHARACTERS IN STRING TO UPPER CASE:
string1 = 'ansii'
print("\n------------------------------TO UPPER CASE---------------------------")
print(string1.upper())

#18. TO CONVERT ALL THE CHARACTERS IN STRING TO TITLE CASE:
string1 = 'united kingdom'
print("\n-----------------------------TO TITLE CASE----------------------------")
print(string1.title())

#19. TO SWAP THE CASES IN A STRING:
string1 = 'i wORK IN aCCENTURE - chennai'
print("\n------------------------------TO SWAPCASE-----------------------------")
print(string1.title())

#20. TO FIND THE MAXIMUM(largest) ALPHABET IN A STRING
string1 = 'umapriya'
string2 = 'UMAPRIYa'
print("\n--------------------------------MAXIMUM-------------------------------")
print(max(string1))
print(max(string2))

#21. TO FIND THE MINIMUM(smallest) ALPHABET IN A STRING:
string1 = 'umapriya'
string2 = 'UMAPRIYa'
print("\n--------------------------------MINIMUM-------------------------------")
print(min(string1))
print(min(string2))


'''
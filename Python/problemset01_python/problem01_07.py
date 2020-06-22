def isIn(string1,string2):
    if((string1 in string2) or (string2 in string1)):
        return True
    else:
        return False
string1 = str(input("Enter any string: "))
string2 = str(input("Enter another string: "))
isIn(string1,string2)

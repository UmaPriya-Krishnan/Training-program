class fun:
    def upperCase(self,string):
        '''This function checks whether the characters in the string are in upper case. 
        If not it converts them to upper case'''
        print("upperCase:\n" ,f.upperCase.__doc__)
        try:      
            for i in string:
                if i.isupper():
                    print(i)
                else:
                    print(i.upper())
        except Exception as E:
            print(E)           
                
    def lowerCase(self, string):
        '''This function checks whether the characters in the string are in lower case. 
        If not, it converts them to lower case'''
        print("\nlowerCase:\n" ,f.lowerCase.__doc__)
        try:
            for i in string:
                if i.islower():
                    print(i)
                else:
                    print(i.lower())
        except Exception as E:
            print(E)       
            
    def splitString(self, string):
        '''This function splits the given string based on the separator mentioned'''
        print("\nsplitString:\n" ,f.splitString.__doc__)
        try:
            s = string.split(" ")
            print(s)
        except Exception as E:
            print("error:" ,E)
            
    def checkVowels(self, string, vowels = 'aeiou'):
        '''This function checks whether the given string has any vowel in it. 
        If yes, It returns the vowels present in the string'''
        print("\ncheckVowels:\n", f.checkVowels.__doc__)
        app = []
        try:
            for i in string:
                if i in vowels:
                    app.append(i)
            print(app)
        except Exception as E:
            print(E)
            
f = fun()
string = "Hey, How are you?"
f.upperCase(string)
f.lowerCase(string)
f.splitString(string)
f.checkVowels(string)


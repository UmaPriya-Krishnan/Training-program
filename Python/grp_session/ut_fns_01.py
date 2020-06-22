def count(string):
    ''' to print the count of each characters in a string'''
    d = {}
    string = string.lower()
    for i in string:
        d[i] = string.count(i)
    return d
count('I am doing well')

def is_numeric(s):
    '''to print the numbers in the given string'''
    list_str = list(s)
    s = ''
    for i in list_str:
        if i.isnumeric():
            s = s+i
    return s
is_numeric('12str345ing')

def consonant(s):
    '''to print the larger set of consonants in a given string'''
    s = s.lower()
    for i in 'aeiou':
        s =s.replace(i,'-')                   #replacing the vowels with a delimiter
        s1 = s.split('-')                     # spliting the string using the same delimiter(removes the vowels from the string)
    len_list = []
    for i in range(len(s1)):
        x = len(s1[i])
        len_list.append(x)                    #Finding the list of the elements withtin the splitted list
    max_index = len_list.index(max(len_list)) #finding the index of the element with maximum length
    return s1[max_index]                      #printing the element with maximum length 

s = 'mango' 
consonant(s)

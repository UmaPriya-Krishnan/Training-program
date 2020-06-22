#To return separate lists for float, int and string from the single list which has values of all datatype
list_all = [1,2,'hey', 'hi', 1.234, -9,'lang', -2.9876,4,9.087,'123']
int_list = []
str_list = []
float_list = []
for i in list_all:
    if type(i) == int:
        int_list.append(i)
    elif type(i) == str:
        str_list.append(i)
    else:
        float_list.append(i)
print("List with integer values: " ,int_list)
print("List with string values: " ,str_list)
print("List with float values: " ,float_list)
print(3**3)


##using function:
def list_typ(list1):
    int_list = []
    str_list = []
    float_list = []
    for i in list1:
        if type(i) == int:
            int_list.append(i)
        elif type(i) == str:
            str_list.append(i)
        else:
            float_list.append(i)
    print("List with integer values: " ,int_list)
    print("List with string values: " ,str_list)
    print("List with float values: " ,float_list)
list_typ([1,2,'hey', 'hi', 1.234, -9,'lang', -2.9876,4,9.087,'123'])




#Take integer inputs from user until he/she presses q ( Ask to press q to quit after every integer input ). Print the cube of the number
#value = int(input("Enter any value: "))
quitt = str(input("Press q to exit: "))
while quitt!= 'q':
    value = int(input("Enter any value: "))
    quitt = str(input("Press q to exit: "))
    print(value)
    x = value**3
print(x)
print(value*value*value)


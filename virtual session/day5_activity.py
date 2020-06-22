#Write a program to find multiplication table of a number 7
print("---------PROBLEM_01---------")
n = int(input("Enter any integer: "))
print("------{} Table------ ".format(n)) 
for i in range(1,10):
    x = i*n
    print(" {0} * {1} = {2}" .format(n,i,x))
    
#with function
def table(n):
    for i in range(1,10):
        x = i*n
        print(" {0} * {1} = {2}" .format(n,i,x))
n = int(input("Enter any integer: "))
table(n)


#2. Declare the list [-4,3,1,6,-7,0,-9,-1,5]
#Write a script to get to the count of negative, positive values from list:
   
list_one = [-4,3,1,6,-7,0,-9,-1,5]
neg_count = 0
pos_count = 0
zero_count = 0
print("\n---------PROBLEM_02---------")
for i in list_one:
    if i <0:
        neg_count+=1
    elif i ==0:
        zero_count+=1
    else:
        pos_count+=1
print ( "Count of negative values: " ,neg_count)
print ( "Count of positive values: " ,pos_count)
print ( "Count of zero(0) : " ,zero_count)

#with function:
def count(list_one):
    neg_count = 0
    pos_count = 0
    zero_count = 0
    for i in list_one:
        if i <0:
            neg_count+=1
        elif i ==0:
            zero_count+=1
        else:
            pos_count+=1
    print ( "Count of negative values: " ,neg_count)
    print ( "Count of positive values: " ,pos_count)
    print ( "Count of zero(0) : " ,zero_count)

list_one = [-4,3,1,6,-7,0,-9,-1,5]
count(list_one)




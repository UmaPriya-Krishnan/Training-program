#1) Print numbers in a particular pattern:
n=5,4,3,2,1
print("----PROBLEM_01----")
for i in n :
    print(str(i) * i)

n = 1,2,3,4,5
x=n[::-1]
print("----PROBLEM_01----")
for i in x :
	print(str(i) * i)    

#with function:
def pattern(n):
    x=n[::-1] 
    for i in x :
        print(str(i) * i)
n = 1,2,3,4,5
pattern(n)


 
#2) declare a list range(533,875)
#Try to count the number of odd and even numbers between the above range
count_even = 0
count_odd = 0
list1 = range(533,875)
print("\n6----PROBLEM_02----")
for i in list1:
    if i%2==0:
        count_even += 1
    else: 
       count_odd +=1
print ("The count of even numbers in the given range is:  " ,count_even)
print ("The count of odd numbers in the given range is:   " ,count_odd)

#with function:
def count(list1):
    count_even = 0
    count_odd = 0
    for i in list1:
        if i%2==0:
            count_even += 1
        else: 
            count_odd +=1
    print ("\nThe count of even numbers in the given range is:  " ,count_even)
    print ("The count of odd numbers in the given range is:   " ,count_odd)
list1 = range(533,875)
count(list1)
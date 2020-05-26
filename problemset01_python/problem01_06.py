s = str(input("Enter any string: "))
values = s.split(",")
print("The comma separated values are:" ,values)
sum = 0
for i in values:
    sum += float(i)
print ('The total sum of comma separated values in the string {} is {}:' .format(s,sum))

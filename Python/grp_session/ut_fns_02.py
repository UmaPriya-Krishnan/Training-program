def btd(str1,str2):
    num = str1+str2
    num = int(num)
    rem, binn, power, i = 0,0,0,0
    while(num):
        rem = num%10
        power = power+rem*(2**i)
        num = num//10
        i+=1
    return power
    
str1 = '01'
str2 = '10'

def isPal(string):
    for i in range(0, len(string)//2):
        if string[i] != string[len(string)-i-1]:
            return False
    return True
    
string = 'malayalam'
    
def date(year):
    yr = abs(int(year) - 1970)
    if (yr%4 == 0 and yr%100 !=0) or yr%400 == 0 :
        days = yr*366
    else: 
        days = yr*365
    hours = days*24
    minutes = hours*60
    seconds = minutes*60
    return (yr, days, hours, minutes, seconds)

year = 2000

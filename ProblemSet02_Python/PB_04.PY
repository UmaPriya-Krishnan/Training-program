def binToDec(binary):
    dec, i, n = 0, 0, 0
    while(binary!=0):
        rem = binary%10
        dec = dec+(rem*pow(2, i))
        binary = (binary//10)
        i+=1
    print("The decimal equivalent is: " ,dec)
binary = int(input("Enter the binary number: "))
binToDec(binary)


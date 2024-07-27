#Write a program to check whether the given number is a perfect number or not.
#A perfect number is the one whose divisors' sum except the number itself is equal to the number itself.
n = int(input("Enter any number: "))
sum1 = 0
if(n==1):
    print("The number is a perfect number")
else:
    for i in range(1, n):
        if(n % i == 0):
            sum1 = sum1 + i
    if (sum1 == n):
        print("The number is a Perfect number!")
    elif(sum1!=n):
        print("The number is not a Perfect number!")
    else:
        print("Invalid number!Input the number that is greater than 0 ")
    
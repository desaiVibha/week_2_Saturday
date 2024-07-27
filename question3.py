#Write a program to check whether the package is dream package or not.
# Note: If the salary is more than 5 lakh then return 'Dream', otherwise return 'NotDream'.
n = int(input("Enter the salary in lakhs without any commas or any symbols: "))
if(n>500000):
    print("Dream")
else:
    print("NotDream")
#Write a program to find out whether the given year is a leap year or not.
""" If a year is divisible by 4, it is a leap year.
However, if that year is divisible by 100, it is not a leap year, unless,
it is also divisible by 400, in which case, it is a leap year. """

def is_leap_year_modulo(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) #The function `is_leap_year_modulo` checks if a given year is a leap year using the modulo operator to verify divisibility by 4, excluding years divisible by 100 unless divisible by 400. 
year_to_check = 2024
result_modulo = is_leap_year_modulo(year_to_check)
print(f"{year_to_check} is a leap year: {result_modulo}")
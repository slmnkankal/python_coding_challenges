# year = int(input("Enter a positive number: "))
def is_leap_year(year):
    if ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
        return f"{year} is a leap year!"
    else:
        return f"{year} is not a leap year!"

print(is_leap_year(2000))
print(is_leap_year(2100))
print(is_leap_year(2004))
print(is_leap_year(2006))

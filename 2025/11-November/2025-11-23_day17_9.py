#leap year using filter and lambda function
years = [int(i) for i in input("Enter years : ").split(",")]
leap_year = list(filter(lambda x: x%4 == 0 and x%100 !=0 or x%400 == 0,years))
print(leap_year)

#leap year

years = [int(i) for i in input("Enter years : ").split(",")]
leap_year = list(filter(lambda x: x%4 == 0 ,years))
print(leap_year)

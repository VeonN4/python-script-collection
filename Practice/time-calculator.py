second = int(input("Second: "))

minute = second / 60
hour = second / 3600
day = second / 86400
week = second / 604800
month = second / 2628000000
year = month / 12
decade = year / 10
century = decade / 10

print("\nHasil")
print(minute, "Minute")
print(hour, "Hour")
print(day, "Day")
print(week, "Week")
print(month, "Month")
print(year, "Year")
print(decade, "Decade")
print(century, "Century")
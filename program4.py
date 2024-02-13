# Write a Python program to extract year, month, date and time using Lambda. 

# Sample Output: 

# 2020-01-15 09:03:32.744178 

# 2020 

# 1 

# 15 

from datetime import datetime
year = lambda dt: datetime.strptime(dt, '%Y-%m-%d %H:%M:%S.%f').year
month = lambda dt: datetime.strptime(dt, '%Y-%m-%d %H:%M:%S.%f').month
date = lambda dt: datetime.strptime(dt, '%Y-%m-%d %H:%M:%S.%f').day
time = lambda dt: datetime.strptime(dt, '%Y-%m-%d %H:%M:%S.%f').time()

date_input = input("Enter the date (YYYY-MM-DD HH:MM:SS.SSSSSS): ")

year = year(date_input)
month = month(date_input)
date = date(date_input)
time = time(date_input)

# Print the extracted components
print("Year:", year)
print("Month:", month)
print("Date:", date)
print("Time:", time)

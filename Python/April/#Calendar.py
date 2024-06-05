"""
Create a calendar using Python
Date : 24.04.2024
"""
import calendar, os

os.system('clear')
print(help(calendar))
print("Calendar for the year 2024:\n")
print(calendar.calendar(2024))
print(calendar.month(2024, 4))
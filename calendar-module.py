#https://www.hackerrank.com/challenges/calendar-module/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
from datetime import datetime
import calendar
datetime_is = datetime.strptime(input(), '%m %d %Y')
print(calendar.day_name[datetime_is.weekday()].upper())

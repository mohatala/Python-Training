from datetime import date
from datetime import datetime,timedelta

my_date = date(2021, 11, 25)
print("La date est:", my_date)


today = date.today()
print("Today's date is", today)


a = datetime(1999, 12, 12) 
print(a) 
a = datetime(1999, 12, 10, 11, 12, 12, 342380) 
print(a)

today = datetime.now() 
print("Current date and time is", today)


ini_time_for_now = datetime.now() 
print ("initial_date", str(ini_time_for_now)) 
future_date_after_2yrs = ini_time_for_now + timedelta(days = 730) 
future_date_after_2days = ini_time_for_now + timedelta(days = 2) 
print('future_date_after_2yrs:', str(future_date_after_2yrs)) 
print('future_date_after_2days:', str(future_date_after_2days)) 

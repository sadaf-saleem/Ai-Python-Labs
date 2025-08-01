# III. a Python program to extract year, month, date and time using Lambda. 

from datetime import datetime  

 
now = datetime.now()  

  
foryear = lambda dt: dt.year  
formonth = lambda dt: dt.month  
forday = lambda dt: dt.day  
fortime = lambda dt: dt.strftime("%H:%M:%S") 

 
print("Current Date & Time:", now)  
print("Year:", foryear(now))  
print("Month:", formonth(now))  
print("Day:", forday(now))  
print("Time:", fortime(now))  

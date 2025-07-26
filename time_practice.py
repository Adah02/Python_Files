from datetime import datetime
time = datetime.now()
hour = 16
if hour > 12:
    hour = hour % 12
date_and_time = time.strftime(f"%d %m %Y   {hour}:%M:%S %p")
print(date_and_time)
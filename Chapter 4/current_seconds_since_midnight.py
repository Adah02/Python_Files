def seconds_since_midnight(hour, minute, seconds):
	hour_in_seconds = 60 * 60 * hour;
	minute_in_seconds = 60 * minute;
	totoalSeconds = hour_in_seconds + minute_in_seconds + seconds;
	return totoalSeconds;



hour = input('Enter the hour of the day based on 24 hour clock: ')
minute = input('Enter the minutes of current time: ')
seconds = input('Enter the minutes of current time: ')

print(seconds_since_midnight(hour, minute, seconds))
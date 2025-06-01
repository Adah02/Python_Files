def seconds_since_midnight(hour, minute, seconds):
	hour_in_seconds = 60 * 60 * hour;
	minute_in_seconds = 60 * minute;
	totoalSeconds = hour_in_seconds + minute_in_seconds + seconds;
	return totoalSeconds;

hour = int(input('Enter the hour of the day based on 24 hour clock: '))
minute = int(input('Enter the minutes of current time: '))
seconds = int(input('Enter the seconds of current time: '))

print('The current seconds since midnight is ',seconds_since_midnight(hour, minute, seconds))
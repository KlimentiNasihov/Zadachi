seconds_in_day = 86400
seconds_in_hour = 3600
seconds_in_minute = 60
seconds = int(input())
days = seconds // seconds_in_day
seconds = seconds - (days * seconds_in_day)
hours = seconds // seconds_in_hour
seconds = seconds - (hours * seconds_in_hour)
minutes = seconds // seconds_in_minute
seconds = seconds - (minutes * seconds_in_minute)
print("{0:.0f} days, {1:.0f} hours, {2:.0f} minutes, {3:.0f} seconds.".format(
days, hours, minutes, seconds))

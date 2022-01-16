
duration = int(input("Введите промежуток времени: "))

seconds_in_minute = 60
seconds_in_hour = 60 * 60
seconds_in_day = 24 * 60 * 60

days = duration // seconds_in_day
seconds = duration - (days * seconds_in_day)
hours = seconds // seconds_in_hour
seconds = seconds - (hours * seconds_in_hour)
minutes = seconds // seconds_in_minute
seconds = seconds - (minutes * seconds_in_minute)

print(f"{days} дн {hours} час {minutes} мин {seconds} сек.")

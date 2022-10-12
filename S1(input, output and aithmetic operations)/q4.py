n = int(input())

seconds = n%60
minutes = n//60

hours = minutes//60
minutes = minutes%60

days = hours // 24
hours = hours%24

print(days, "days", hours, "hours", minutes, "minutes", seconds, "seconds")

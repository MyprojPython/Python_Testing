#Conversting minutes to hours and minutes
total_minutes = int(input("Enter total minutes: "))
hours = total_minutes // 60
minutes = total_minutes % 60

print(f"{total_minutes} minutes = {hours} hour(s) and {minutes} minute(s)")
#Many people keep time using a 24-hour clock (11 is 11am and 23 is 11pm, 0 is midnight). 
# If it is currently 13 and you set your alarm to go off in 50 hours, it will be 15 (3pm). 
# Write a Python program to solve the general version of the above problem. 
# Ask the user for the time now (in hours) and then ask for the number of hours to wait for the alarm. 
# Your program should output what the time will be on a 24-hour clock when the alarm goes off.
def calculate_alarm_time(now: str, wait: int):
    time_parts = now.split(':')
    hours = int(time_parts[0])
    minutes = int(time_parts[1]) if len(time_parts) > 1 else 0
    new_hours = (hours + wait) % 24
    print(f"The time will be {new_hours:02}:{minutes:02} on a 24-hour clock when the alarm goes off.")

now = input("Enter the time now (HH or HH:MM): ")
wait = int(input("Enter the number of hours to wait: "))
calculate_alarm_time(now, wait)
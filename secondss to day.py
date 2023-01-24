print("write time in second")
second= float(input("enter seconds:" ))
day=second/86400
day2=second//86400
decimal=day-day2
hour=decimal*24
hour2=int(hour)
decimal2=hour-hour2
minute=decimal2*60
minute2= int(minute)
decimal3=minute-minute2
second=decimal3*60
second2=round(second, 0)
print(day2, hour2, minute2, second2)

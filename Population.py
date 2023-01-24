import datetime

# January 1, 2022 at 00:00:00
start_date = datetime.datetime(2022, 1, 1, 0, 0, 0)

# January 20, 2022 at 12:15:20
end_date = datetime.datetime(2022, 1, 20, 12, 15, 20)

# Calculate the difference in time
delta = end_date - start_date

# Number of births per day
births_per_day = int(60*60*24/7)

# Number of deaths per day
deaths_per_day = int(60*60*24/13)

# Number of immigrants per day
immigrants_per_day = int(60*60*24/35)

# Calculate the estimated population
estimated_population = 334205120 + (delta.days * (births_per_day - deaths_per_day + immigrants_per_day))

print("Estimated population on January 20, 2022 at 12:15:20: ", estimated_population)

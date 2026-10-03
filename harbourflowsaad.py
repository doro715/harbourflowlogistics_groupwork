Promised_time = int(input("Enter Promised time: "))

Actual_time = int(input("Enter Actual time: "))

Delay = Actual_time - Promised_time

Damaged_parcels= int(input("Enter Damaged parcels: "))

if Damaged_parcels > 0:
    print("SERVICE FAILURE:")
elif Damaged_parcels <= 0:
    Delay <= 0
    print("ON TIME")
elif Delay >=15:
    print("minor delay")
else:
    print("major delay")

#calculate the number of deliveries

Deliveries = []
for x in range(1, 8):
    input_value = int(input(f"Enter Deliveries for Day {x}: "))
    Deliveries.append(input_value)
    print(Deliveries)
total = 0
for delivery in Deliveries:
    total += delivery

#calculate the average deliveries in a week
average = total / 7
print(f"Average Deliveries per Day: {average:.2f}")

#calculate the highest deliveries in a day

highest = Deliveries[0]
for delivery in Deliveries:
    if delivery > highest:
        highest = delivery
print(f"Highest Deliveries in a Day: {highest}")

#calculate the lowest deliveries in a day

lowest = Deliveries[0]
for delivery in Deliveries:
    if delivery < lowest:
        lowest = delivery
print(f"Lowest Deliveries in a Day: {lowest}")

#calcualting days that met the target

days_met_target = 0
for delivery in Deliveries:
    if delivery >= 10:
        days_met_target += 1
print(f"Days that Met Target: {days_met_target}")

#calculate days that had high deliveries and low deliveries

days =  ["monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

highest = Deliveries[0]
highest_day = 0
for x in range(7):
    if Deliveries[x] > highest:
        highest = Deliveries[x]
        highest_day = x
print(f"Day with Highest Deliveries: {days[highest_day]}")

lowest = Deliveries[0]
lowest_day = 0
for x in range(7):
    if Deliveries[x] < lowest:
        lowest = Deliveries[x]
        lowest_day = x
print(f"Day with Lowest Deliveries: {days[lowest_day]}")

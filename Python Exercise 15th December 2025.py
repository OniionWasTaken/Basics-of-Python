#Question 1
inventory = {
    "Tomatoes": {"stock":150, "price_per_unit": 5.0},
    "Onions": {"stock":80, "price_per_unit": 3.5},
    "Garden Eggs": {"stock":200, "price_per_unit": 1.0}
}

while True:
    print("Welcome to Makola Market Online.")
    print("Our Inventory.")
    print("1. Tomatoes")
    print("2. Onions")
    print("3. Garden Eggs")
    print("4. Exit")
    option = input("Enter item name to purchase or 'Exit': ")

    if option == "Exit":
        print("Closing sales. Total transactions completed.")
        break
    elif option in inventory :
        amount = int(input("Enter quantity to buy: "))
        total_cost = amount * inventory[option]["price_per_unit"]
        total_cost = round(total_cost, 2)
        if amount > inventory[option]["stock"]:
            print(f"Sorry, only {inventory[option]['stock']} units of {option} remaining. ")
        else:
            inventory[option]["stock"] -= amount
            print(f"Sale successful! Cost: GHS {total_cost}. \n{inventory[option]['stock']} units of {option} remaining. ")
            break
    else:
        print("Item not found in stock. Check spelling.")




#Question 2
monthly_charge = 15.00

print("Welcome to the GWCL Bill Calculator")
consumption_input = int(input(f"Enter water consumption for the month ((in cubic meters)): "))
rate = {}

if consumption_input >= 0 and consumption_input <= 15:
    rate = 0.90
elif consumption_input >= 16 and consumption_input <= 30:
    rate = 1.20
elif consumption_input >= 30 :
    rate = 1.80
else :
    print("Invalid input.")

total_bill = monthly_charge + consumption_input * rate
total_cost = round(total_bill, 2)

print("--- Monthly Water Bill Summary ---")
print(f"Consumption: {consumption_input} cubic meters")
print("Service Charge: GHS15.00")
print(f"Consumption Cost: GHS{consumption_input * rate}")
print(f"Total cost: GHS{total_cost}")


#Question 3
recorded_speeds = [95, 110, 100, 85, 125, 90, 105, 115, 70, 130, 99, 101, 88]
speed_limit = 100
speed_violations = []

for speed in recorded_speeds:
    if speed > speed_limit:
        print(f"WARNING: Vehicle recorded at {speed} km/h. Exceeded limit of {speed_limit} km/h." )
        speed_violations.append(speed)

print("Total number of vehicles: ", len(recorded_speeds))
print("Number of speed violations: ", len(speed_violations))
print("Percentage of speeding vehicles: ", round((len(speed_violations) / len(recorded_speeds)) * 100, 2),"%")
print("Average speed: ", sum(recorded_speeds) / len(recorded_speeds))

print(f"Speeds for focused inspection segment(3rd to 8th vehicle): {recorded_speeds[2:8]}")









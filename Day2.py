print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
total_person = int(input("How many people to split the bill? "))

bill = (total_bill + (total_bill * tip_percentage * 0.01))/total_person
print(f"Each person should pay: ${round(bill,2)}")
#creating a CALORIE CALCULATOR:
#Name:PARAG
#SECTION:B

print("WELCOME TO THE CALORIE CALCULATOR:")
# ADDING MEALS INFO:
meal_names = []
meal_calories = []

num_meals = int(input("How many meals do you want to enter today? "))

for i in range(num_meals):
    print(f"\nMeal {i+1}:")
    meal = input("Enter meal name: ")
    calories = float(input("Enter calorie amount: "))
    
    meal_names.append(meal)
    meal_calories.append(calories)

#CALCULATING CALORIE
total_calories = sum(meal_calories)
average_calories = total_calories / len(meal_calories)

daily_limit = float(input("\nEnter your daily calorie limit: "))

#OUTPUT OF THE CODE
if total_calories > daily_limit:
    status_message = "WARNING: You have exceeded your daily calorie limit!"
else:
    status_message = "SUCCESS: Great job! You are within your daily calorie limit."


print("\n------------------------------------------------------------")
print("                   Daily Calorie Summary")
print("------------------------------------------------------------")
print(f"{'Meal Name':<20}\t{'Calories'}")
print("------------------------------------------------------------")

for i in range(len(meal_names)):
    print(f"{meal_names[i]:<20}\t{meal_calories[i]}")

print("------------------------------------------------------------")
print(f"Total:\t\t\t{total_calories}")
print(f"Average per meal:\t{average_calories:.2f}")
print("------------------------------------------------------------")
print(status_message)
print("------------------------------------------------------------\n")

#SAVING FILE
save_option = input("Do you want to save this session report? (yes/no): ").lower()

if save_option == "yes":
    import datetime
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # with open("calorie_report.txt", "w") as file:
    with open("calorie_report.txt", "w", encoding="utf-8") as file:

        file.write("------------------------------------------------------------\n")
        file.write("                 Daily Calorie Tracker Report\n")
        file.write("------------------------------------------------------------\n")
        file.write(f"Date & Time: {timestamp}\n\n")
        file.write(f"{'Meal Name':<20}\t{'Calories'}\n")
        file.write("------------------------------------------------------------\n")
        
        for i in range(len(meal_names)):
            file.write(f"{meal_names[i]:<20}\t{meal_calories[i]}\n")
        
        file.write("------------------------------------------------------------\n")
        file.write(f"Total Calories:\t\t{total_calories}\n")
        file.write(f"Average per Meal:\t{average_calories:.2f}\n")
        file.write(f"Status:\t\t\t{status_message}\n")
        file.write("------------------------------------------------------------\n")
    
    print("\n✅ Report saved successfully as 'calorie_report.txt'")
else:
    print("\nReport not saved. Goodbye!")

from datetime import datetime

date_input = input("Enter date (DD-MM-YYYY): ")
date_obj = datetime.strptime(date_input, "%d-%m-%Y")

print("Day:", date_obj.strftime("%A"))

# output:-

# Enter date (DD-MM-YYYY): 22-12-2025
# Day: Monday

# Enter date (DD-MM-YYYY): 08-06-2007
# Day: Friday
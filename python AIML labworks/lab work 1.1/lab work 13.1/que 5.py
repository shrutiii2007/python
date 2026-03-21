from datetime import datetime

date_string = "2024-01-01"
date_obj = datetime.strptime(date_string, "%Y-%m-%d")
print("Datetime object:", date_obj)

formatted_string = date_obj.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted string:", formatted_string)

# output:-

# Datetime object: 2024-01-01 00:00:00
# Formatted string: 2024-01-01 00:00:00
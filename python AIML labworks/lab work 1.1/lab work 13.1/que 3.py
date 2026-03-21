import datetime

now = datetime.datetime.now()

print("DD-MM-YYYY:", now.strftime("%d-%m-%Y"))
print("MM/DD/YYYY:", now.strftime("%m/%d/%Y"))

print("24-hour format:", now.strftime("%H:%M:%S"))
print("12-hour format:", now.strftime("%I:%M:%S %p"))


# output:-

# DD-MM-YYYY: 28-12-2025
# MM/DD/YYYY: 12/28/2025
# 24-hour format: 12:01:23
# 12-hour format: 12:01:23 PM
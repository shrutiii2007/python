from datetime import datetime, timedelta

date1 = datetime(2024, 1, 1)
date2 = datetime(2024, 1, 10)

difference = date2 - date1
print("Days between dates:", difference.days)

today = datetime.now()
new_date = today + timedelta(days=7)
print("Date after 7 days:", new_date)


# output:-

# Days between dates: 9
# Date after 7 days: 2026-01-04 12:02:07.937389
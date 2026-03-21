from utilities.file_utils import write_file
from utilities.date_utils import days_between
from datetime import date

write_file("test.txt", "Hello Student")
print(days_between(date(2024,1,1), date(2024,1,10)))


# output:-

9
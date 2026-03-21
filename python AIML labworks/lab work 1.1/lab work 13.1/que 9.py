import time

seconds = int(input("Enter seconds: "))

while seconds > 0:
    print("Time left:", seconds)
    time.sleep(1)
    seconds -= 1

print("Countdown finished!")


# output:-

# Enter seconds: 5
# Time left: 5
# Time left: 4
# Time left: 3
# Time left: 2
# Time left: 1
# Countdown finished!
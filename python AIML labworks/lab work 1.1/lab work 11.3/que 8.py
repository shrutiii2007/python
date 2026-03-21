class HighTemperatureError(Exception):
    pass

temp = input("Enter temperature in Celsius: ")

try:
    if not temp.replace('.', '', 1).isdigit():
        raise TypeError("Temperature must be numeric")

    temp = float(temp)

    assert -273 <= temp <= 10000, "Temperature out of range"

    if temp > 1000:
        raise HighTemperatureError("Temperature too high")

    print("Valid temperature:", temp)

except (TypeError, AssertionError, HighTemperatureError) as e:
    print("Error:", e)


# output:-

# Enter temperature in Celsius: 25
# Valid temperature: 25.0

# Enter temperature in Celsius: abc
# Error: Temperature must be numeric

# Enter temperature in Celsius: -300
# Error: Temperature out of range

# Enter temperature in Celsius: 1500
# Error: Temperature too high

# Enter temperature in Celsius: 1000
# Valid temperature: 1000.0

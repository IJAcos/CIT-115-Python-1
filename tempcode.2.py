# Ivy's Temp Converter

# Ask for the temperature
temp = float(input("Enter temperature: "))

# Ask if it's F or C
unit = input("Is it in F or C? ").upper()

# Check the unit
if unit == "F":
    if temp > 212:
        print("Too hot! Must be 212 or less.")
    else:
        c = (5 / 9) * (temp - 32)
        print("In Celsius:", round(c, 1))

elif unit == "C":
    if temp > 100:
        print("Too hot! Must be 100 or less.")
    else:
        f = (9 / 5) * temp + 32
        print("In Fahrenheit:", round(f, 1))

else:
    print("Type F or C only.")

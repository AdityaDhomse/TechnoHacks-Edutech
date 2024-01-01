def cel_to_fahren():
    cel = float(input("\nEnter your temperature (in °C): "))
    fahren = float((cel * 1.8) + 32)
    print(cel, "°C =", fahren, "°F")


def fahren_to_cel():
    fahren = float(input("\nEnter your temperature (in °F): "))
    cel = float((fahren - 32) * 0.55555555)
    print(fahren, "°F =", cel, "°C")

print("Temperature Conversion")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = int(input("\nEnter your choice: "))

print("-----------------------------------")

if (choice == 1):
    cel_to_fahren()
elif (choice == 2):
    fahren_to_cel()
else:
    print("Invalid Choice")

print("-----------------------------------")
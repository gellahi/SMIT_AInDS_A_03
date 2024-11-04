temperature=float(input("Enter the temperature in Celsius: "))
if temperature<0:
    print("Temperature is Freezing")
elif temperature>=0 and temperature<24:
    print("Temperature is Moderate")
else:
    print("Temperature is Hot")
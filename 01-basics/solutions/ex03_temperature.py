celsius = float(input("Temperature in Celsius: "))
fahrenheit = celsius * 9 / 5 + 32
print(f"{celsius:.1f}°C is {fahrenheit:.1f}°F")

fahrenheit = float(input("Temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) * 5 / 9
print(f"{fahrenheit:.1f}°F is {celsius:.1f}°C")

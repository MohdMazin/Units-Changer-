while True:
    unit = input("Enter any valid Unit To Proceed (F/C): ").upper()
    if unit == "F" or unit == "C":
        break
    else:
        print("Please Enter a Valid Unit Like (F/C)!")

temp = float(input("Enter temperature to convert: "))

if unit == "F":
    celsius = (temp - 32) * 5/9
    print(f"When {temp} Fahrenheit is converted to Celsius, it will be {celsius} Celsius.")
elif unit == "C":
    fahrenheit = (temp * 9/5) + 32
    print(f"When {temp} Celsius is converted to Fahrenheit, it will be {fahrenheit} Fahrenheit.")

def convert_temperature():
    # the user have to enter the temperature value
    temp = float(input("Enter the temperature value: "))
    
    # the user have to enter the unit of measurement
    unit = input("Enter the unit of measurement (C for Celsius, F for Fahrenheit): ").upper()
    
    # Convert the temperature based on the unit
    if unit == 'C':
        # Convert Celsius to Fahrenheit
        converted_temp = (temp * 9/5) + 32
        print(f"{temp}°C is equal to {converted_temp:.2f}°F")
    elif unit == 'F':
        # Convert Fahrenheit to Celsius
        converted_temp = (temp - 32) * 5/9
        print(f"{temp}°F is equal to {converted_temp:.2f}°C")
    else:
        print("Invalid unit of measurement. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

# Call the function
convert_temperature()

    
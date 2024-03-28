def main():
    intro()
    main_loop()


def intro():
    print("Welcome to the Converter App!")
    print("Convert Temperatures and Measurements to different Units of Measure!")


def main_loop():
    input_data = ""
    while input_data != 'q':
        input_data = input("Select 't' for Temperature Converter or 'm' for Measurement Converter")
        select_converter(input_data)


def select_converter(selection):
    if selection == 't':
        temperature_converter()
    elif selection == 'm':
        measurement_converter()
    else:
        print("Please enter either 't' for Temperature Converter or 'm' for Measurement Converter")

def temperature_converter():
    while 'temperature_number' not in locals():
        temperature = input("Please enter temperature: ")

        try:
            temperature_number = float(temperature)
        except ValueError:
            print("Enter a number, please.")

    temperature_unit = ''
    while temperature_unit not in ['f','c','k']:
        temperature_unit = input("Please enter temperature unit (f,c,k): ")

        if temperature_unit not in ['f','c','k']:
            print("Enter f,c, or k, please")
    temperature_unit_final = ''
    while temperature_unit_final not in ['f','c','k']:
        temperature_unit_final = input("Please enter temperature unit (f,c,k): ")

        if temperature_unit_final not in ['f','c','k']:
            print("Enter f,c, or k, please")

    if temperature_unit == 'f':
        if temperature_unit_final == 'c':
            temperature_final = (temperature_number - 32) * (5/9)
        elif temperature_unit_final == 'k':
            temperature_final = (temperature_number - 32) * (5/9) + 273.15
        else:
            temperature_final = temperature_number

    print(f"{temperature_final} {temperature_unit_final}")

if __name__ == "__main__":
    main()

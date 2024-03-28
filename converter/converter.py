def main():
    intro()
    main_loop()


def intro():
    print("Welcome to the Converter App!")
    print("Convert Temperatures and Measurements to different Units of Measure!")


def main_loop():
    input_data = ""
    while input_data != "q":
        input_data = input(
            "Select 't' for Temperature Converter or 'm' for Measurement Converter: "
        )
        select_converter(input_data)


def select_converter(selection):
    if selection == "t":
        temperature_converter()
    elif selection == "m":
        measurement_converter()
    elif selection != "q":
        print(
            "Please enter either 't' for Temperature Converter or 'm' for Measurement Converter"
        )


def measurement_converter():
    measurement_number = get_user_input("measurement")
    measurement_unit = get_user_input("measurement_unit")
    measurement_unit_final = get_user_input("measurement_unit")

    if measurement_unit == "ft":
        measurement_final = measurement_number * 0.3048
    else:
        measurement_final = measurement_number / 0.3048

    print(f"{measurement_final} {measurement_unit_final}")


def temperature_converter():

    temperature_number = get_user_input("temperature")
    temperature_unit = get_user_input("temperature_unit")
    temperature_unit_final = get_user_input("temperature_unit")

    if temperature_unit == "f":
        if temperature_unit_final == "c":
            temperature_final = (temperature_number - 32) * (5 / 9)
        elif temperature_unit_final == "k":
            temperature_final = (temperature_number - 32) * (5 / 9) + 273.15
        else:
            temperature_final = temperature_number

    print(f"{temperature_final} {temperature_unit_final}")


def get_user_input(input_type):
    if input_type == "temperature" or input_type == "measurement":
        while True:
            user_input = input(f"Please enter {input_type} value: ")

            if user_input.strip():
                try:
                    number_input = float(user_input)
                    return number_input
                except ValueError:
                    print("Not a number value. Please try again.")
            else:
                print("Invalid input. Please try again.")

    elif input_type == "temperature_unit":
        while True:
            user_input = input("Please enter temperature unit (f,c,k): ")
            user_input = user_input.strip()
            if user_input:
                if user_input in ["f", "c", "k"]:
                    return user_input
                else:
                    print("Not a valid unit. Please try again.")
            else:
                print("Invalid input. Please try again.")

    elif input_type == "measurement_unit":
        while True:
            user_input = input("Please enter measurement unit (ft,m): ")
            user_input = user_input.strip()
            if user_input:
                if user_input in ["ft", "m"]:
                    return user_input
                else:
                    print("Not a valid unit. Please try again.")
            else:
                print("Invalid input. Please try again.")


if __name__ == "__main__":
    main()

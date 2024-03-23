def main():
    intro()

def intro():
    print("Hello and welcome to sorter!")
    print("Enter a common seperated list of letters and numbers and we will sort it for you :)")


def get_list():
    while True:
        input_data = input("Enter list of items here: ")
        if "," in input_data:
            input_list = input_data.split(",")
            return input_list
        else:
            print("Please enter a comma seperated list of letters")

def sort_list(list_data):
    length = len(list_data)

    if length <= 0:
        return None
    if length == 1:
        return list_data


if __name__ == "__main__":
    main()

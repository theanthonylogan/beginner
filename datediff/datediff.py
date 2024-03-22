from datetime import datetime
from datetime import date
import sys


def main():
    intro()
    print("First Date")
    first_date = get_date()
    print("Second Date")
    second_date = get_date()
    get_date_difference(first_date, second_date)


def intro():
    print("Welcome to the Date Diffence App.")
    print(
        "This App will Tell you the Date Difference between any Two Dates you want to know"
    )
    print("Enter the letter q to quit")


def get_date():
    invalid_date = True
    while invalid_date:
        input_from_user = input("Please Enter Date (YYYY-MM-DD): ")
        if input_from_user == "q":
            sys.exit()
        if input_from_user and input_from_user[4] == input_from_user[7] == "-":
            return date.fromisoformat(input_from_user)

        print("Please be sure to enter the date in the proper format.")


def get_date_difference(first_date, second_date):
    result = first_date - second_date
    print(f"Days: {result.days}")


if __name__ == "__main__":
    main()

import string
import random


def main():
    intro()
    data = get_data_to_encode()
    print(encode_data(data))


def intro():
    print(
        "Welcome to the coder application. Please enter the phrase you want to encode and we will send back to you the encoded value."
    )


def get_data_to_encode():
    return input("Please enter data to encode: ")


def encode_data(data):
    encoded_data = ""
    for x in data:
        encoded_data += random.choice(string.ascii_letters)
    return encoded_data


if __name__ == "__main__":
    main()

def main():
    intro()
    game()


def intro():
    print("\n --------Welcome to the Number Adventure!--------")
    print("\n All you need for this adventure is the numbers 1-10")
    print("\n Press 'q' to quit at anytime.")


def game():

    is_alive = True
    position = 1
    adventure = {
        1: {
            "question": "\n Your adventure starts, choose your weapon. \n 2 Nunchucks, or 3 Ninja Stars",
            "answers": [2, 3],
            "is_alive": True,
        },
        2: {
            "question": "\n Close combat fighter eh!? Well we shall see how that goes. You hear sirens blaring just outside your window. Do you 4-sss open the door, or take the 5 flights of stairs up to the roof?",
            "answers": [4, 5],
            "is_alive": True,
        },
        3: {
            "question": "\n Good idea! Ninja Stars from Afar! There is a knock at your door... You aren't expecting visitors. Do you take your secret elevator in the closet to the roof 5 stories up, or escape out the fire escape 6 ladders down?",
            "answers": [5, 6],
            "is_alive": True,
        },
        4: {
            "question": "\n A little boy with red curly hair and broken glasses that are taped in the middle is standing there and asks you a riddle. 'Who ate 9? 7 or 8?'",
            "answers": [7, 8],
            "is_alive": False,
        },
        5: {
            "question": "\n A helicopter lands and a group of bunnies jump out dressed in ninja gear. They hop towards you slowly with their beady red eyes shining bright in the night. One bunny asks for the code? Do you say 'I 8 my carrots' or '9-er'?",
            "answers": [8, 9],
            "is_alive": False,
        },
        6: {
            "question": "\n After sliding down the ladders, a green alien pops out from behind the trash can and says, 'Who did 7 eat? was it 9 or 10?'",
            "answers": [9, 10],
            "is_alive": False,
        },
    }

    while is_alive:
        is_alive = adventure[position]["is_alive"]
        position = get_user_input(adventure[position])
        if position == "q":
            is_alive = False

    if position == 7:
        print("\nThe little boy gives you a jolly rancher. Its grape your favorite!")
    elif position == 8:
        print("\nWrong! He dumps a bucket of carrot mush on your head!")
    elif position == 9:
        print("\nCorrect! You are so smart!")
    elif position == 10:
        print(
            "\nThe alien gets larger and larger and lets out a HUGE!!!! sneeze and covers you in green booger goo! Ewwww...."
        )
    print("--------The End--------")

def get_user_input(position):
    while True:
        input_data = input(position["question"] + ": ")
        if input_data == "q":
            return input_data

        try:
            input_number = int(input_data)
            if input_number in position["answers"]:
                return input_number
            else:
                print("Please enter " + position["answers"].split(", "))
        except ValueError:
            print("Please enter " + position["answers"].split(", "))
            continue


if __name__ == "__main__":
    main()

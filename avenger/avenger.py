def main():
    intro()


def intro():
    print("Welcome to the Avenger Quiz!")
    print(
        "We will analyze your personality and tell you which avenger you are most like"
    )
    print("Enter 'q' to quit at anytime")
    quiz()

def quiz():
    questions = [
        {
            "question": "What is your favorite color?",
            "answers": {"A - red": 1, "B - blue": 100, "C - green": 10000},
        },
        {
            "question": "Are you sneaky?",
            "answers": {
                "A - Like a kid stealing candy from the candy jar": 1,
                "B - Like a kid waking up early to play video games": 100,
                "C - WHAT YOU SAY!!!": 10000,
            },
        },
        {
            "question": "Are you strong?",
            "answers": {
                "A - I float more like a butterly": 1,
                "B - I lift bro": 100,
                "C - Like Paul Bunyan": 10000,
            },
        },
    ]
    score = 0
    valid_input = False
    for question in questions:

        while not valid_input:
            format_question(question)
            input_data = input("Make your Selection (A, B, or C): ")
            if input_data == "q":
                return
            if input_data.upper() in ["A", "B", "C"]:
                if input_data.upper() == "A":
                    score += 1
                elif input_data.upper() == "B":
                    score += 100
                else:
                    score += 10000
                valid_input = True
            else:
                print("Enter A, B, or C. Or 'q' to quit.")
        valid_input = False
    avenger = evaluate_score(score)

    print(f"Your personality matches: {avenger}")


def format_question(question):
    print(question["question"])
    for answer, value in question["answers"].items():
        print(answer)


def evaluate_score(score):
    score_sheet = {
        3: "Mantis",
        300: "Hawkeye",
        30000: "Hulk",
        102: "Spiderman",
        10101: "Vision",
        20100: "Thor",
    }

    if score in score_sheet.keys():
        return score_sheet[score]
    else:
        return "Beast"


if __name__ == "__main__":
    main()

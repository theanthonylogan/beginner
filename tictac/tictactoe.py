def main():
    intro()
    game()


def intro():
    print("Welcome to the Tic Tac Toe Game")
    print("Using the numbers 1-9 select your spot. X goes first")


def game():
    o_turn = False
    input_data = ""
    board_state = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
    winner = False
    in_board = False
    while input_data != "q" and not winner:
        board(board_state)
        if o_turn:
            input_data = input("O Player enter selection: ")
        else:
            input_data = input("X Player enter selection: ")

        if input_data not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            print("Please enter only a valid number")
        else:
            for row in range(3):
                for value in range(3):
                    if input_data == board_state[row][value]:
                        if o_turn:
                            board_state[row][value] = "O"
                        else:
                            board_state[row][value] = "X"
                        in_board = True
                    if in_board:
                        break
                if in_board:
                    break
        if in_board:
            o_turn = not o_turn
            in_board = False
            if check_winner(board_state):
                if not o_turn:
                    print("\n ---- O Wins!!!! ----")
                else:
                    print("\n ---- X Wins!!!! ----")
                board(board_state)
                return


def board(board_state):
    print("")
    for row in board_state:
        print(f"| {row[0]} | {row[1]} | {row[2]} |")

    print("")


def check_winner(board_state):
    winning_states = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)],
    ]
    winning = False
    for winning_state in winning_states:
        if (
            board_state[winning_state[0][0]][winning_state[0][1]]
            == board_state[winning_state[1][0]][winning_state[1][1]]
            == board_state[winning_state[2][0]][winning_state[2][1]]
        ):
            winning = True
    return winning


if __name__ == "__main__":
    main()

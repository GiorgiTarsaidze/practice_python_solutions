def draw_board(game):
    row_size = len(game)
    column_size = len(game[0])

    row = " ---"
    column = "| "

    for i in range(row_size):
        print(row * column_size)
        for j in range(column_size):
            print(f"{column}{game[i][j]} ", end="")
        print(column)
    print(row * column_size)

def main():
    player = 1
    while True:
        draw_board(game)
        play_game(player)
        winner = check_winner(game)

        if winner:
            draw_board(game)
            print(winner)
            break

        if not has_empty_squares():
            draw_board(game)
            print("Its a DRAW!")
            break
        player = 3 - player

def play_again():
    while True:
        try:
            ask = input("Play again? (*Any Key) - yes , (N) - no: ").strip().lower()
            return ask
        except ValueError:
            print("(*Any Key) - yes, (N) - no")

def play_game(player):
    while True:
        get_input = input(f"Player {player}, please enter (row,column): ")
        try:
            row,column = map(int, get_input.split(","))

            if game[row-1][column-1] == " ":
                if player == 1:
                    game[row-1][column-1] = "X"
                    break
                else:
                    game[row-1][column-1] = "O"
                    break
            else:
                print("This square is already taken")
                continue
        except ValueError:
            print("Invalid input, please enter row and column in 'row,column' format. ")
        except IndexError:
            print("Invalid input, Please enter numbers between 1 and 3. ")

def check_winner(game):
    for row in game:
        if set(row) == {"X"}:
            return "Player X wins!"
        elif set(row) == {"O"}:
            return "Player O wins!"

    for col in range(3):
        column = {game[i][col] for i in range(3)}
        if column == {"X"}:
            return "Player X wins!"
        elif column == {"O"}:
            return "Player O wins!"

    major_diagonal = {game[i][i] for i in range(3)}
    minor_diagonal = {game[i][2 - i] for i in range(3)}

    if major_diagonal == {"X"} or minor_diagonal == {"X"}:
        return "Player X wins!"
    elif major_diagonal == {"O"} or minor_diagonal == {"O"}:
        return "Player O wins!"

    return None
    
def print_game():
    for row in game:
        print(" ".join(str(cell) for cell in row))

def has_empty_squares():
    for row in game:
        if " " in row:
            return True
    return False
 
if __name__ == "__main__":
    while True:
        game = ([[" ", " ", " "] for _ in range(3)])
        main()
        response = play_again()
        if response == "n":
            break
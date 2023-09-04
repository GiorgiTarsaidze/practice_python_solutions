game = [
    [0, 0, 0],
	[0, 0, 0],
	[0, 0, 0]]

def main():
    player = 1
    while True:
        play_game(player)
        if not has_empty_squares():
            print("No more empty squares")
            break
        player = 3 - player

def play_game(player):
    while True:
        get_input = input(f"Player {player}, please enter (row,column): ")
        try:
            row,column = map(int, get_input.split(","))

            if game[row-1][column-1] == 0:
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

    print_game()

def print_game():
    for row in game:
        print(" ".join(str(cell) for cell in row))

def has_empty_squares():
    for row in game:
        if 0 in row:
            return True
    return False
    
if __name__ == "__main__":
    main()
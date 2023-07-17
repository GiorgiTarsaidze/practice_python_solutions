def main():
    player_one_name = get_name(1)
    player_two_name = get_name(2)
    while True:
        player_one_choice = get_choice(player_one_name)
        player_two_choice = get_choice(player_two_name)
        print(get_winner(player_one_choice,player_two_choice,player_one_name,player_two_name))
        if not continue_game():
            break

def get_name(number):
    return input(f"Name for Player {number}: ")

def get_choice(player_name):
    while True:
        choice = input(f"{player_name} choose: Rock, Paper, Scissors ").lower().strip()
        if choice in ["rock","paper","scissors"]:
            return choice
        else:
            print("Invalid input! Please choose Rock, Paper or Scissors!")

def get_winner(player_one_choice,player_two_choice,player_one_name,player_two_name):
    if player_one_choice == player_two_choice:
        return "It's a draw!"
    elif ((player_one_choice == "rock" and player_two_choice == "scissors") or
         (player_one_choice == "paper" and player_two_choice == "rock") or
         (player_one_choice == "scissors" and player_two_choice == "paper")
         ):
        
        return f"{player_one_name} Wins! {player_one_choice} beats {player_two_choice}"
    else:
        return f"{player_two_name} Wins! {player_two_choice} beats {player_one_choice}"

def continue_game():
    while True:
        choose = input("Another round? (yes/no) ").lower().strip()
        if choose == "yes":
            return True
        elif choose == "no":
            return False
        else:
            print("Invalid input. Please choose (yes/no) ")

if __name__ == "__main__":
    main()
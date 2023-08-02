import random

def main():
    random_list = random.sample((range(9)),4)
    joined_number = "".join(map(str, random_list))
    if play_game(random_list) is True:
        print(f"Congrats!, The number was {joined_number}, good job!")

def get_input():
    while True:
        ask = input("Enter your 4 digit number: ").strip()
        if len(ask) != 4:
            print("Please enter 4 digit number! ")
        elif not ask.isdigit():
            print("Your input must be a number! ")
        else:
            return ask
        
def play_game(random_list):
    while True:
        cows = 0
        bulls = 0
        ask = get_input()
        for index, digit in enumerate(ask):
            if int(digit) in random_list:
                if index == random_list.index(int(digit)):
                    cows += 1
                else:
                    bulls += 1

        print(f"You have {cows} cows and {bulls} bulls. ")
        
        if cows == 4:
            return True

if __name__ == "__main__":
    main()
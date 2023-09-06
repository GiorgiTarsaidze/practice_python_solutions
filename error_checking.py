import random

def main():
    count = 0
    random_number = random.randint(1,9)
    while True:
        ask = get_input()
        if ask is None:
            break
        if compare_input(ask, random_number):
            print(f"You are CORRECT! The number was {random_number}")
            break
        else:
            count += 1
            print("Too high!" if ask > random_number else "Too low!")
    print(f"It took you {count} guesses!")

def get_input():
    while True:
        try:
            ask = input("Number between 1 and 9 or 'exit' to exit: ")
            if ask.lower() == "exit":
                return None
            ask = int(ask)
            if ask > 9 or ask < 1:
                print("Invalid input, your number must be between 1 and 9.")
            else:
                return ask
        except ValueError:
            print("Not a vaid input, please enter a number!")

def compare_input(ask, random_number):
    return ask == random_number

if __name__ == "__main__":
    main()
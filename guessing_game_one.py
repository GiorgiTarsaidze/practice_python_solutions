import random

def main():
    count = 0 
    while True:
        random_number = random.randint(1,9)
        ask = get_input()
        if ask is None:
            break
        if compare_input(ask, random_number):
            count += 1
            print(f"You are CORRECT! The number was {random_number}")
        else:
            print("Too high!" if ask > random_number else "Too low!")
    print("Your score:",count)

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
            print("Invalid input! Try again.")

def compare_input(ask, random_number):
    return ask == random_number

if __name__ == "__main__":
    main()
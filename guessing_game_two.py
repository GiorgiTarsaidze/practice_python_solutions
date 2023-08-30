def main():
    lowest = 0
    highest = 100
    guess = 0
    guess_number(lowest,highest,guess)

def guess_number(lowest,highest,guess):
    counter = 0 
    while lowest <= highest:
        guess = (lowest + highest) //2
        ask = input(f"I think you number is {guess}. (L) too low, (C) correct, (H) too high ").lower()
        counter += 1

        if ask == "h":
            highest = guess - 1
        elif ask == "l":
            lowest = guess + 1
        elif ask == "c":
            print(f"Good game! It took me {counter} guesses to find your number!")
            break
        else:
            print("Please enter a valid number between 1 ad 100!")

if __name__ == "__main__":
    main()
def main():
    number = get_number()
    number_odd_or_even = odd_or_even(number)
    print(f"Number {number} is {number_odd_or_even}")

def get_number():
    while True:
        try:
            number = int(input("Enter your number: "))
            return number
        except ValueError:
            print("Your input is not a number!")

def odd_or_even(number):
    if number == 0:
        return "Even"
    elif number % 4 == 0:
        return "Even and multiple of 4"
    elif number % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
if __name__ == "__main__":
    main()
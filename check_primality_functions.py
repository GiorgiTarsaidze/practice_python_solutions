def main():
    number = get_input()
    divisors_list = get_divisors_list(number)
    print(prime_or_not(divisors_list))
    
def get_input():
    while True:
        try:
            number = int(input("Tell me a number: "))
            if number <= 0:
                print("Please enter a positive number!")
            else:
                return number
        except ValueError:
            print("Please enter a valid number!")

def get_divisors_list(number):
    return [element for element in range(1,number+1) if number % element == 0]

def prime_or_not(divisors_list):
    if len(divisors_list) <= 2:
        return("This number is prime!")
    else:
        return("This number is NOT prime!")

if __name__ == "__main__":
    main()
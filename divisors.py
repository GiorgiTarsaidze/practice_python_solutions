def main():
    number = get_input("Number: ")
    divisors_list = get_divisors(number)
    if divisors_list:
        for element in divisors_list:
            print(element)
    else:
        print("Nothing found.")

def get_divisors(number):
    divisor_list = [element for element in list(range(1, number + 1)) if number % element == 0]
    return divisor_list
    
def get_input(prompt):
    while True:
        try:
            asked_number = int(input(prompt))
            return asked_number
        except ValueError:
            print("Number is not valid.")

if __name__ == "__main__":
    main()
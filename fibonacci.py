def main():
    numbers = get_input()
    print(get_sequence(numbers))

def get_input():
    while True:
        try:
            numbers = int(input("How many fibonacci numbers you would like to generate? "))
            if numbers <= 0:
                print("Please enter positive numbers!")
            else:
                return numbers
        except ValueError:
            print("Please enter valid number!")

def get_sequence(numbers):
    sequence = [0,1]
    for _ in range(1,numbers):
        next_num = sequence[-1] + sequence[-2]
        sequence.append(next_num)
    return sequence

if __name__ == "__main__":
    main()
def main():
    variables = get_input()
    print(f"Largest number is {find_largest(variables)}")

def get_input():
    variables = []
    while True:
        try:
            number = int(input("Enter your number: "))
            variables.append(number)
            if len(variables) == 3:
                break
        except ValueError:
            print("Please enter a number!")
    return variables

def find_largest(variables):
    return sorted(variables)[-1]

# def find_largest(variables):
#     a,b,c, = variables

#     if a > b and a > c:
#         return(f"{a} is the biggest")
#     elif b > a and b > c:
#         return(f"{b} is the biggest")
#     else:
#         return(f"{c} is the biggest")

if __name__ == "__main__":
    main()
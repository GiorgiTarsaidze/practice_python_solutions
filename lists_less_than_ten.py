my_list = [1, 1, 2, 3, 5, 8, 0, 13, 21, 34, 55, 89]

def main():
    number = get_input()
    modified_list = filter_list(number)
    sorted_list = sort_list(modified_list)
    if sorted_list:
        for element in sorted_list:
            print(element)
    else:
        print("Nothing found.")

def get_input():
    while True:
        try:
            asked_number = int(input("Give me a number: "))
            return asked_number
        except ValueError:
            print("Number is not valid.")

def sort_list(modified_list):
    return sorted(modified_list)
    
def filter_list(number):
    return [element for element in my_list if element < number]

if __name__ == "__main__":
    main()
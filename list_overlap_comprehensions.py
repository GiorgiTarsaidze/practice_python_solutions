import random

def main():
    length_1 = get_length()
    length_2 = get_length()

    list_1 = generate_list(length_1)
    list_2 = generate_list(length_2)

    print(f"List 1: {list_1} \nList 2: {list_2} \nOverlap: {find_overlap(list_1,list_2)}")


def get_length():
    while True:
        try:
            list_length = int(input("Choose list length between 1 and 50: "))
            if list_length > 50 or list_length < 1:
                print("Invalid list range!")
            else:
                return list_length
        except ValueError:
            print("Invalid input")


def generate_list(length):
    return random.sample(range(1,50),length)

def find_overlap(list_1, list_2):
    return list(set([element for element in list_1 if element in list_2]))

if __name__ == "__main__":
    main()
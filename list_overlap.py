import random

def main():
    len_1, len_2 = get_input()
    list_1 = list_generator(len_1)
    list_2 = list_generator(len_2)
    intersection = get_intersection(list_1,list_2)
    print("First list:", list_1)
    print("Second list:", list_2)
    print("Intersection:", intersection)

def get_input():
    while True:
        try:
            input_1 = int(input("Length or first list: "))
            input_2 = int(input("Length of second list: "))

            if input_1 <= 0 or input_2 <= 0 or input_1 > 40 or input_2 > 40:
                print("Enter list length between 1 and 40.") 
            else:
                return input_1,input_2
        except ValueError:
            print("Please, enter valid input.")

def list_generator(length):
    return [random.randint(1, 100) for _ in range(length)]

def get_intersection(list_1,list_2):
    intersected_list = [element for element in list_1 if element in list_2]
    return list(set(intersected_list))

if __name__ == "__main__":
    main()
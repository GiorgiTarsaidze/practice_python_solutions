import random

def main():
    random_list = get_list()
    new_list = first_and_last(random_list)
    print(f"Generated list: {random_list}\nFirst and last elements: {new_list}")

def get_list():
    return random.sample(range(30),10)

def first_and_last(random_list):
    return [random_list[0],random_list[-1]]

if __name__ == "__main__":
    main()
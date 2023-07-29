import random
import string
letters, numbers, special_symbols = string.ascii_letters, string.digits, string.punctuation

def main():
    ask = get_input()
    password_list = generate_password(ask)
    print("Your password: "+ join_list(password_list))

def get_input():
    options = ["easy","medium","strong"]
    while True:
        ask = input("Please select strength of your pasword (Easy/Medium/Strong): ").lower().strip()
        if ask not in options:
            print("Please choose between (Easy, Medium, Strong)")
        else:
            return ask

def generate_easy_password():
    easy_list = random.sample(letters,8)
    random.shuffle(easy_list)
    return easy_list

def generate_medium_password():
    medium_list = random.sample(letters,8) + random.sample(numbers,8)
    random.shuffle(medium_list)
    return medium_list

def generate_strong_password():
    strong_list = random.sample(letters,8) + random.sample(numbers,8) + random.sample(special_symbols,8)
    random.shuffle(strong_list)
    return strong_list

def generate_password(option):
    if option == "easy":
        return generate_easy_password()
    elif option == "medium":
        return generate_medium_password()
    elif option == "strong":
        return generate_strong_password()
    else:
        print("Please enter valid input!")

def join_list(password_list):
    return "".join(password_list)

if __name__ == "__main__":
    main()
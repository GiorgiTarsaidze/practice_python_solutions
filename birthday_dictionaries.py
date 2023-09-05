birthdays = {
    "Albert Einstein": "14/03/1879",
    "Benjamin Franklin": "17/01/1706",
    "Ada Lovelace": "10/12/1875"
}

def main():
    name = get_input()
    print(f"{name}'s birthday is {birthdays[name]}!")

def get_input():
    while True:
        ask = input("Who's birthday do you want to look up? ").title()
        if ask in birthdays:
            return ask
        else:
            print("We dont know their birthday yet.")

if __name__ == "__main__":
    main()

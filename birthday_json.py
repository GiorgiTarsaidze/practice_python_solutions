import json
import re

with open("text_files/birthdays.json", "r") as f:
    birthdays = json.load(f)

def main():
    while True:
        choose = input('What do you want to do? Add (A), Find (F), Quit (Q) ').capitalize()
        if choose == 'Q':
            print("---")
            break
        elif choose == 'A':
            add_input()
        elif choose == 'F':
            name = get_input()
            print(f"{name}'s birthday is {birthdays[name]}!")
        else:
            print("Please choose (A) for Adding, (F) for Finding, (Q) - Quit ")

def add_input():
    while True:
        name = input("Whose name you want to add? ").title()
        if name.isalpha() and name:
            break
        else:
            print("Invalid name. Please enter a valid name.")

    while True:
        date = input(f"When was {name} born? (DD/MM/YYYY) ")
        date_pattern = r'\d{2}/\d{2}/\d{4}'
        if re.match(date_pattern, date):
            birthdays[name] = date
            with open("text_files/birthdays.json", "w") as f:
                json.dump(birthdays, f)
            print("Successfully added")
            break
        else:
            print("Invalid date format. Please enter a date in the format DD/MM/YYYY.")

def get_input():
    while True:
        ask = input("Who's birthday do you want to look up? ").title()
        if ask in birthdays:
            return ask
        else:
            print("We dont know their birthday yet.")

if __name__ == "__main__":
    main()
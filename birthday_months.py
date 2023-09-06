from collections import Counter
import json

month_numbers = {
	1: "January",
	2: "February",
	3: "March", 
	4: "April",
	5: "May",
	6: "June",
	7: "July",
	8: "August",
	9: "September",
	10: "October",
	11: "November",
	12: "December"
}

def main():
    birthdays = file_loader()
    months = get_months_list(birthdays)
    c = Counter(months)
    print(c)

def file_loader():
    with open('text_files/birthdays.json', 'r') as file:
        return json.load(file)

def get_months_list(birthdays):
    months = []
    for value in birthdays.values():
        splitted = value.split("/")
        month = int(splitted[1])
        months.append(month_numbers[month])
    return months

if __name__ == "__main__":
    main()
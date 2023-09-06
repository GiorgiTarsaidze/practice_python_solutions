import json
from collections import Counter
from bokeh.plotting import figure, show, output_file

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

    months_display = list(c.keys())
    counts = list(c.values())

    display_histograph(months_display,counts)

def file_loader():
    with open("text_files/birthdays.json", "r") as file:
        return json.load(file)

def get_months_list(birthdays):
    months = []
    for value in birthdays.values():
        splitted = value.split("/")
        month = int(splitted[1])
        months.append(month_numbers[month])
    return(months)

def display_histograph(months_display,counts):
    output_file("plot.html")

    categories = list(month_numbers.values())
    p = figure(x_range=categories, title="Birthday Months")
    p.vbar(x=months_display, top=counts, line_color="black", line_width=2)
    p.xaxis.major_label_orientation = "vertical"
    show(p)

if __name__ == "__main__":
    main()
def main():
    row_size = get_input("row")
    column_size = get_input("column")
    board(row_size,column_size)

def get_input(size):
    while True:
        try:
            dimension = int(input(f"{size} size: "))
            if dimension > 50 or dimension <= 0:
                print("Please enter a number between 0 and 50")
            else:
                return dimension
        except ValueError:
            print("Please enter a valid number")

def board(row_size,column_size):
    row = " ---"
    column = "|   "
    
    for _ in range(row_size):
        print(row*column_size)
        print(column*(column_size+1))
    print(row*column_size)

if __name__ == "__main__":
    main()
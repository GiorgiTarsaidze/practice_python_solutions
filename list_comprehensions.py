my_list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

def main():
    print("Even numbers in given list:", even_filter())

def even_filter():
    return [number for number in my_list if number % 2 == 0]

if __name__ == "__main__":
    main()

def main():
    happy_numbers = file_to_list("text_files/happynumbers.txt")
    prime_numbers = file_to_list("text_files/primenumbers.txt")
    print("Overlap:", get_overlap(happy_numbers, prime_numbers))

def file_to_list(filename):
    with open(filename, "r") as file:
        to_list = file.read().split()
    return to_list

def get_overlap(happy_list, prime_list):
    return [int(number) for number in prime_list if number in happy_list]

if __name__ == "__main__":
    main()

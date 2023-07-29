def main():
    ask_sentence = get_input()
    print(reverse_order(ask_sentence))

def get_input():
    sentence = input("Enter your sentence: ")
    return sentence

def reverse_order(ask):
    splitted_sentence = ask.split()
    splitted_sentence.reverse()
    return " ".join(splitted_sentence)

if __name__ == "__main__":
    main()
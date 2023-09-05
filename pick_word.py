import random as r

def main():
    print(word_picker(), end='')

def word_picker():
    with open('text_files/sowpods.txt','r') as file:
        return r.choice(file.readlines())

if __name__ == "__main__":
    main()
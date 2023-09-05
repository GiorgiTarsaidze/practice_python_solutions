import random as r

def main():
    word = word_picker()
    print(word)
    print("Welcome to Hangman!")
    listed_word, listed_spaces = initialize_game(word)

    print(" ".join(listed_spaces))

    play_game(listed_word,listed_spaces)

def word_picker():
    with open('text_files/sowpods.txt','r') as file:
        return r.choice(file.readlines()).strip()

def initialize_game(word):
    spaces = "_" * len(word)
    return list(word), list(spaces)

def play_game(listed_word,listed_spaces):
    tries = 6
    guessed_letters = set()
    while True:
        print(f"You have {tries} remaining!")
        ask = input("Guess your letter: ").upper()

        if ask in guessed_letters:
            print("Already guessed!")
        elif ask in listed_word:
            for i in range(len(listed_word)):
                if listed_word[i] == ask:
                    listed_spaces[i] = ask
            print(" ".join(listed_spaces))
        else:
            if ask != '' and len(ask) == 1 and ask.isalpha():
                guessed_letters.add(ask)
                tries -=1
            
        if "_" not in listed_spaces:
            print("Congratulations! You Guessed the word! ")
            break

        if tries == 0:
            print(f"Out of tries! The word was: {''.join(listed_word)}")
            break

if __name__ == "__main__":
    main()
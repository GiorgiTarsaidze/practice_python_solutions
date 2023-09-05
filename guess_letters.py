def main():
    word = "EVAPORATE"
    print("Welcome to Hangman!")
    listed_word, listed_spaces = initialize_game(word)

    print(" ".join(listed_spaces))

    play_game(listed_word,listed_spaces)

def initialize_game(word):
    spaces = "_" * len(word)
    return list(word), list(spaces)

def play_game(listed_word,listed_spaces):
    guessed_letters = []
    while True:
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
                guessed_letters.append(ask)
            
        if "_" not in listed_spaces:
            print("Congratulations! You Guessed the word! ")
            break

if __name__ == "__main__":
    main()
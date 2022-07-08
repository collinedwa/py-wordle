import random as r
import sys
import wordle_word_list

def game():
    available_letters = {'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd', 'e': 'e', 'f': 'f',
                        'g': 'g', 'h': 'h', 'i': 'i', 'j': 'j', 'k': 'k', 'l': 'l', 
                        'm': 'm', 'n': 'n', 'o': 'o', 'p': 'p', 'q': 'q', 'r': 'r', 
                        's': 's', 't': 't', 'u': 'u', 'v': 'v', 'w': 'w', 'x': 'x', 
                        'y': 'y', 'z': 'z'}
                        
    word = wordle_word_list.answer_list[r.randint(0,2314)]
    word_index = [letter for letter in word]
    message = {5: "first", 4: "second", 3: "third", 2: "fourth", 1: "fifth"}
    tries = 5
    guesses = []
    print("Welcome to PyWordle! Try to guess the 5-letter word in 5 tries or less!")
    print("Letter in correct spot is denoted by parentheses (e.g PO(W)DER)")
    print("Letter in word, but incorrect spot is denoted by square brackets (e.g. PO[W]DER)\n")

    while tries != 0:
        print(f"You have {tries} tries remaining.\n")
        if len(guesses)>0:
            print("Guesses:")
            for i in range(len(guesses)):
                print(guesses[i])
        print(f"Available Letters: {list(available_letters.values())}\n")
        guess = input('Type your guess, or "exit" to quit: ')
        try:
            int(guess)
            print("Guess must only contain letters!\n")
            continue
        except:
            pass
        if guess.lower() == 'exit':
            sys.exit()
        elif len(guess) != 5:
            print("Word length must equal 5!\n")
            continue
        elif guess.lower() not in wordle_word_list.word_list:
            print("Not an accepted word!\n")
            continue
        elif guess.lower() != word:
            print("\n******")
            print("Wrong!")
            print("******\n")

            # For loop to iterate through each letter in the user submitted word and determine whether it matches the answer
            # encapsulates letters with () or [] depending on whether they are in the correct spot/in the word
            # additionally alters the overall list of letters to reflect what you have submitted

            word_dummy = list(guess.lower())
            for i in range(5):
                if word_dummy[i] in word_index and word_dummy[i] == word_index[i]:
                    if word_dummy[i] in list(available_letters.values()):
                        available_letters[word_dummy[i]] = (f"({word_dummy[i]})")
                    elif (f"[{word_dummy[i]}]") in list(available_letters.values()):
                        available_letters[word_dummy[i]] = (f"({word_dummy[i]})")
                    word_dummy[i] = (f"({word_dummy[i]})")
                elif word_dummy[i] in word_index and word_dummy[i] != word_index[i]:
                    if word_dummy[i] in list(available_letters.values()):
                        available_letters[word_dummy[i]] = (f"[{word_dummy[i]}]")
                    word_dummy[i] = (f"[{word_dummy[i]}]")
                else:
                    available_letters[word_dummy[i]] = '_'
            guesses.append(''.join(word_dummy))
            tries -= 1
        elif guess.lower() == word:
            print("\nThat's correct! You win!")
            print(f"You got it on your {message[tries]} try\n")
            break

    if tries == 0:
        print(f"You lose! The word was '{word}'\n")

    choice = False
    while choice == False:
        selection = input("Play again? (Y/N): ")
        if selection.lower() == 'y':
            choice = True
            print("\n")
            game()
        elif selection.lower() == 'n':
            choice = True
            sys.exit()
        else:
            print("Invalid response! Please type 'Y' or 'N': ")
            continue   
game()
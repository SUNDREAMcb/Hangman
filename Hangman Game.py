"""
JULY 2024 = Package
"""
import randomword
from PyDictionary import PyDictionary
import tkinter as tk
from tkinter import ttk

# window = tk.Tk()
# window.geometry('600x400')
# window.title('Hangman Game ')

#root will be the start of the game, asking user name, and difficulty

root = tk.Tk()
root.title("Welcome to Hangman!")
root.geometry("300x100")
root.maxsize(300, 100)
root.attributes('-topmost', True)
root.minsize(299, 99)

name_var = tk.StringVar()
difficulty_var = tk.StringVar()


class Player:
    playing = True
    difficulty_dict = {
        'test': 100,
        'easy': 5,
        'medium': 4,
        'hard': 3,
        'expert': 2}
    difficulty_list = list(difficulty_dict.keys())

    def __init__(self, lives, playing=True, win_streak=0):
        self.lives = lives
        self.playing = playing
        self.win_streak = win_streak


def set_difficulty():
    """set amt of lives based off choice in GUI"""
    print(difficulty_var.get())  # displays difficulty chosen
    choice = difficulty_var.get().lower()
    try:
        if choice.lower() in Player.difficulty_list:
            lives = Player.difficulty_dict[choice]
            print(f"You have {lives} mistakes available!")
            return lives
        else:
            print(f"Sorry, {choice} mode not available.")
            return set_difficulty()
    except Exception as err:
        print(err)


def create_player():
    player = Player(set_difficulty())
    return player


def get_word():
    """7.25 - i got the word to be defined, but sometimes the game pulls a different word to use than is defined.
    this most likely happens due to the exception not being handled properly, i will work on this again next time
    I think another issue is I am having this function do two seperate things, so pulling them apart will make tesitng
    easier and more clear. """

    word = randomword.get_random_word()
    try:
        meaning = PyDictionary.meaning(word, disable_errors=True)
        for i in meaning:
            print(i)
            print(meaning[i])
            print(word)
    except Exception as e:
        get_word()
    return word


def hangman():  # main loop,
    """create hangman game ruleset"""
    user = create_player()
    hangman_word = get_word()
    word = hangman_word
    max_attempts = user.lives
    incorrect_guesses = 0
    guessed_letters = []
    display_word = ['_' if letter.isalpha() else letter for letter in word]
    print(" ".join(display_word))
    print("You can enter a letter to guess, or type 'help' to view status, or 'quit' to quit.")
    while '_' in display_word and incorrect_guesses < max_attempts:
        guess = input(": ").lower()
        if guess.isalpha() and guess not in guessed_letters and len(guess) == 1:
            guessed_letters.append(guess)
            if guess in word:
                for index, letter in enumerate(word):
                    if letter == guess:
                        display_word[index] = guess
                        print("Good Job!")
                        print(" ".join(display_word))
            else:
                incorrect_guesses += 1
                print(f"Incorrect. You've made {incorrect_guesses} out of {max_attempts} remaining attempts. ")
        elif guess.isalpha() and guess == 'quit':
            print("Oh, you want to Quit. Okay. ")
            break
        elif guess.isalpha() and guess == 'help':
            print(" ".join(display_word))
            print(guessed_letters, " are the letters you have guessed.")
        else:
            print("That is not a valid input.")
    if '_' not in display_word:
        print("Congratulations! ")
        winnersays = input("Do you want to play again?: ( Yes / No ) ")
        if winnersays.lower() == 'yes':
            user.win_streak += 1
            print(f"You have won {user.win_streak} games so far!")
            hangman()
        elif winnersays.lower() == 'no':
            Player.playing = False
            return
        else:
            print("That is not a valid input")
    else:
        print("GAME OVER!")
        print(word)
        losersays = input("New Game?: ( Yes / No ) ")
        if losersays.lower() == 'yes':
            user.win_streak = 0
            hangman()
        elif losersays.lower() == 'no':
            Player.playing = False
            return
        else:
            print("That is not a valid input")


def main():
    run = True

    root.mainloop()
    while run:
        print("Welcome to Hangman Game. ")
        hangman()
        run = False
        print("Goodbye! Thank you. ")

#
name_label = ttk.Label(root, text='Username: ', font=('calibre', 10, 'bold'))
name_entry = ttk.Entry(root, textvariable=name_var, font=('calibre', 10, 'normal'))

diff_label = ttk.Label(root, text='Difficulty: ', font=('calibre', 10, 'bold'))
diff_dropdown = ttk.Combobox(root, values=["Test", "Easy", "Medium", "Hard", "Expert"], textvariable=difficulty_var)

sub_btn = ttk.Button(root, text='Submit', command=hangman)

name_label.grid(row=0, column=0)
name_entry.grid(row=0, column=1)
diff_label.grid(row=1, column=0)
diff_dropdown.grid(row=1, column=1)
sub_btn.grid(row=2, column=1)

# body of the code


if __name__ == "__main__":
    main()

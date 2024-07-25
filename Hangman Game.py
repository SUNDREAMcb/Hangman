"""
JULY 2024 = Package
"""
import randomword
import sys 
import tkinter as tk 
from tkinter import ttk
import user_popup

print(sys.prefix)
window = tk.Tk()
window.geometry('600x400')
window.title('Hangman Game ')

root=tk.Tk()
 
# setting the windows size
root.title("Welcome to Hangman!")
root.geometry("300x100")
root.maxsize(300,100)
root.attributes('-topmost', True)
root.minsize(299,99)

name_var=tk.StringVar()
difficulty_var=tk.StringVar()
 
class Player:
    playing = True
    difficulty_dict = {'test': 100, 'easy': 5, 'normal': 4, 'hard': 3, 'expert': 2}
    difficulty_list = list(difficulty_dict.keys())

    def __init__(self, lives, playing=True, win_streak=0):
        self.lives = lives
        self.playing = playing
        self.win_streak = win_streak


def set_difficulty():
    """set amt of lives"""
    print(*Player.difficulty_list)
    choice = input("Which difficulty do you choose? ").lower()
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
    "randomly generate word using randomword module, determine difficulty of word based off length"
    word = randomword.get_random_word()
    if len(word) <= 3:
        print("This one should be easy")
        return word
    if 8 >= len(word) > 3:
        print("This one is somewhat difficult")
        return word
    if len(word) > 8:
        print("This word is longer, therefore harder. Good Luck")
        return word


def hangman():  # main loop,
    """create hangman game ruleset"""
    user = create_player()
    hangman_word = get_word()
    max_attempts = user.lives
    incorrect_guesses = 0
    guessed_letters = []
    display_word = ['_' if letter.isalpha() else letter for letter in hangman_word]
    print(" ".join(display_word))
    print("You can enter a letter to guess, or type 'help' to view status, or 'quit' to quit.")
    while '_' in display_word and incorrect_guesses < max_attempts:
        guess = input(": ").lower()
        if guess.isalpha() and guess not in guessed_letters and len(guess) == 1:
            guessed_letters.append(guess)
            if guess in hangman_word:
                for index, letter in enumerate(hangman_word):
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
            print(guessed_letters," are the letters you have guessed.")
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
        losersays = input("New Game?: ( Yes / No )")
        if losersays.lower() == 'yes':
            user.win_streak = 0
            hangman()
        elif losersays.lower() == 'no':
            Player.playing = False
            return
        else:
            print("That is not a valid input")

def submit():
 
    name=name_var.get()
    difficulty=difficulty_var.get()
     
    print("The name is : " + name)
    print("Difficulty Chosen : " + difficulty)
     
    name_var.set("")
    difficulty_var.set("")
    
    return name, difficulty

def main():
    run = True
    
    root.mainloop()

    window.mainloop()
    while run:
        print("Welcome to Hangman Game. ")
        hangman()
        run = False
        print("Goodbye! Thank you. ")


name_label = ttk.Label(root, text = 'Username: ', font=('calibre',10, 'bold'))
name_entry = ttk.Entry(root,textvariable = name_var, font=('calibre',10,'normal'))

diff_label = ttk.Label(root, text = 'Difficulty: ', font = ('calibre',10,'bold'))
diff_dropdown = ttk.Combobox(root, values = ["Test","Easy","Medium","Hard","Expert"], textvariable= difficulty_var)

sub_btn=ttk.Button(root,text = 'Submit', command = main)
  
name_label.grid(row=0,column=0)
name_entry.grid(row=0,column=1)
diff_label.grid(row=1,column=0)
diff_dropdown.grid(row=1,column=1)
sub_btn.grid(row=2,column=1)
  
# body of the code



if __name__ == "__main__":
    main()


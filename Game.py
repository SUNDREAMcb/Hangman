"""
At the end of the month; present a hard mode: Hard mode should take player and cut their max tries in half
Consistently, I work anywhere from an hour or two up to 3 hours every day. I get home at 3PM, try to be off computer 7PM.

this project is an exercise in 'thinking' pythonic, what solutions are at my fingertips
I think my biggest hurdle is surrounding the filesystem management,understanding of the virtual environment/IDE and
the difference between the terminal and the command window...?

3.10.24 : I think the hard mode would be a fun idea
    ---- here are the concepts we need to tackle to do so. -----
    - scope
    - function calling
    - import module
    - control flow
3.10.(Night)  - words are now longer and strange. It's going to be very easy to expand each difficulty's list.
3.11 - This was a slower day.
3.12 - I've found a simple, not complicated way to choose difficulty based off user input.
3.13 - Class for players. able to give each specific difficulty lives counter
3.14 - Win Streak is not increasing beyond 1.
3.15 - Player class should handle win streak, current difficulty, name.
I feel stumped. Need to simplify some things and be sure i know how i want each object to be called.
3.16 - afraid i wouldn't be able to get back to where i was -  I solved most of the
problems I was shooting for. Class handles player lives, difficulty(indirect) and tracks win streak.
3.17 - I didnt have any ideas.
3.18 - I want to add an input so user can quit altogether, choose a different difficulty "Quit" should quit the game,
"Choose Difficulty" should exit current loop and go to former loop. Right now we have each Part of the game, but how we
make it a functioning system is to build out the body.
3.24 -
Alright, i improved it and then broke it. lives  pull from a dict of keys, using that
key list to display difficulty. I think the getword is also broken as a result. Something in the create player function.
3.27 - exceptionhandling. Game functions again! I'm able to focus on working on details. Now i want to select a difficulty mid game.
"""
import random


class Player:
    playing = True
    difficulty_dict = {'test': 100, 'easy': 20, 'normal': 10, 'hard': 5}
    difficulty_list = list(difficulty_dict.keys())

    def __init__(self, lives, playing=True, win_streak=0):
        self.lives = lives
        self.playing = playing
        self.win_streak = win_streak


username = input("What is your name?: ")


def set_difficulty():
    """set amt of lives, which determines what word list to pull from  """
    print(Player.difficulty_list[::])
    choice = input("Which difficulty do you choose? ").lower()
    try:
        if choice.lower() in Player.difficulty_list:
            lives = Player.difficulty_dict[choice]
            print(f"{username}, You have {lives} mistakes available!")
            return lives
        else:
            print(f"Sorry, {choice} not available.")
            return set_difficulty()
    except Exception as err:
        print(err)


user = Player(set_difficulty())


def getword():
    """This function returns a word chosen from one of several lists"""
    hard_list = ["onomatopoeia", "xylophone", "bureaucracy", "mnemonic", "gobbledygook", "quixotic",
                 "serendipity", "ephemeral", "cynosure", "sesquipedalian", "antidisestablishmentarianism",
                 "sesquicentennial", "perspicacious", "labyrinthine", "syzygy", "soliloquy", "antediluvian",
                 "perfidious", "plethora", "ubiquitous", "vicissitude", "juxtaposition", "idiosyncrasy",
                 "circumlocution", "paradigm", "vexatious", "quagmire", "ebullient", "exacerbate",
                 "apocryphal", "indubitable", "zeitgeist", "quixotically", "esoteric", "anachronistic",
                 "mellifluous", "obfuscate", "cacophony", "chiaroscuro", "sesquicentennial", "platitude",
                 "proclivity", "quintessential", "serendipitous", "ubiquitously", "voluminous", "euphemism",
                 "incendiary", "penultimate", "incongruous", "obstreperous"
                 ]
    normal_list = ["elephant", "umbrella", "guitar", "mountain", "ocean", "fireplace", "bicycle", "telescope",
                   "piano", "butterfly", "helicopter", "volcano", "microscope", "astronaut", "dinosaur",
                   "tornado", "dragon", "carousel", "cathedral", "submarine", "mermaid", "whale", "robot",
                   "squirrel", "rainbow", "zeppelin", "canyon", "jungle", "tiger", "peacock", "waterfall",
                   "giraffe", "octopus", "rocket", "snorkel", "avalanche", "kangaroo", "spaceship", "whirlwind",
                   "monument", "galaxy", "mushroom", "sandcastle", "vampire", "sphinx", "unicorn", "centaur",
                   "yeti", "narwhal"
                   ]
    easy_list = ["apple", "banana", "cat", "dog", "house", "car", "tree", "sun", "moon", "flower",
                 "chair", "table", "book", "pen", "computer", "phone", "bird", "fish", "ball", "cup",
                 "door", "window", "bed", "lamp", "shirt", "shoe", "sock", "hat", "bag", "cookie",
                 "pizza", "cake", "juice", "milk", "egg", "key", "clock", "star", "smile", "friend",
                 "love", "happy", "sad", "funny", "fast", "slow", "big", "small", "hot", "cold"
                 ]
    test_list = ["test", "list"]
    while user.playing:
        if user.lives == 100:
            word = random.choice(test_list)
            return word
        if user.lives == 20:
            word = random.choice(easy_list)
            return word
        if user.lives == 10:
            word = random.choice(normal_list)
            return word
        if user.lives == 5:
            word = random.choice(hard_list)
            return word


def hangman():  # main loop,
    """We are choosing to play the game"""
    hangman_word = getword()
    max_attempts = user.lives
    incorrect_guesses = 0
    guessed_letters = []
    display_word = ['_' if letter.isalpha() else letter for letter in hangman_word]
    print(" ".join(display_word))
    while '_' in display_word and incorrect_guesses < max_attempts:
        guess = input("Enter a letter: ").lower()
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
        else:
            print("invalid input, please try again.")
    if '_' not in display_word:
        print("Congratulations! ")
        winnersays = input("Do you want to play again?: ").lower()
        if winnersays == 'yes':
            user.win_streak += 1
            print(f"You have won {user.win_streak} games so far!")
            hangman()
        else:
            Player.playing = False
            return
    else:
        print("GAME OVER!")
        losersays = input("New Game?: ").lower
        if losersays == 'yes':
            user.win_streak = 0
            hangman()
        else:
            Player.playing = False
            return


# body of the code
while Player.playing:
    hangman()

print("Goodbye")

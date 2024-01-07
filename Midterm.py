import random
#need to import rarndom list of numbers
def choose_word():
    """
    It needs to choose a random word from the list.
    Returns:
        str: randm word from list.
    """
    words = ["kayak", "kiosk", "zippy", "Yacht", "squak", "phlegm", "pajama", "ostracize"]
    return random.choice(words)
#need to store words then have a random one selected
def display_word(word, guessed_letters):
    """
    I need it to display the letters that have been guessed and the blank space for the letters that still need to be defined
    Args:
        word (str): word to be guessed.
        guessed_letters - List of letters that is guessed by the player.
    Returns:
        str: the displayed word with underscores
    """
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display
#need to display the blank spaces as well as the underscores for the viewer
def print_hangman(attempts):
    """
    ASCII art needs to be printed based on the amount of failed attempts by the user
    Args:
        attempts (int): the numbers of attemps that were chosen
    """
    stages = [
        """
           --------
           |      |
           |      O
           |
           |
           |
           -
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |
           -
        """,
        """
           --------
           |      |
           |      O
           |     /|
           |      |
           |
           -
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |      |
           |
           -
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |      |
           |     /
           -
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |      |
           |     / \\
           -
        """
    ]
#used outside rescources to help me create the "art" for the hangman.
    if attempts < len(stages):
        print(stages[attempts])
    else:
        print("Sorry, somthing went wrong. Unable to display Hangman.")
#in case the code does not display properly
def hangman():
    """
    functions that are main that are required to execute the game
    """
    word_to_guess = choose_word()
    guessed_letters = []
    max_attempts = 6
    attempts = 0
#display different values to the user as well as keep track of them for the code
    print("Welcome to Hangman!")
    print(display_word(word_to_guess, guessed_letters))
#so the player sees what is happening 
    while True:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invald input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue
#so that the user can have feedback
        guessed_letters.append(guess)

        if guess not in word_to_guess:
            attempts += 1
            print_hangman(attempts)
            print(f"Wrong guess! {max_attempts - attempts} attempts left.")
            print(display_word(word_to_guess, guessed_letters))
        else:
            print("Good guess!")
            display = display_word(word_to_guess, guessed_letters)
            print(display)
#to print and five the user feedback on if he got the letter correct
        if set(word_to_guess) <= set(guessed_letters):
            print("Congratulations! You guessed the word!")
            break

        if attempts == max_attempts:
            print("Sourry, you ran out of attempts. The word was:", word_to_guess)
            break
#when the user loses, let him down gently and say "sorry" becasue you know he gonna be hurting (these words are hard)
if __name__ == "__main__":
    hangman()

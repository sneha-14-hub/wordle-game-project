from rich.prompt import Prompt
from rich.console import Console
from random import choice

# Define square characters for the Wordle game
SQUARES = {
    'correct_place': '🟩',
    'correct_letter': '🟨',
    'incorrect_letter': '⬛'
}

# Welcome message and instructions
WELCOME_MESSAGE = f'\n[white on blue] WELCOME TO WORDLE [/]\n'
PLAYER_INSTRUCTIONS = "You may start guessing\n"
GUESS_STATEMENT = "\nEnter your guess"
ALLOWED_GUESSES = 6

# Words list for the Wordle game
word_list = ['APPLE', 'BERRY', 'CHART', 'DAILY', 'EAGER']

# Define functions for each type of feedback
def correct_place(letter):
    return f'[black on green]{letter}[/]'

def correct_letter(letter):
    return f'[black on yellow]{letter}[/]'

def incorrect_letter(letter):
    return f'[black on white]{letter}[/]'

# Function to check the player's guess and return the result
def check_guess(guess, answer):
    guessed = []
    wordle_pattern = []
    for i, letter in enumerate(guess):
        if answer[i] == guess[i]:
            guessed.append(correct_place(letter))
            wordle_pattern.append(SQUARES['correct_place'])
        elif letter in answer:
            guessed.append(correct_letter(letter))
            wordle_pattern.append(SQUARES['correct_letter'])
        else:
            guessed.append(incorrect_letter(letter))
            wordle_pattern.append(SQUARES['incorrect_letter'])
    return ''.join(guessed), ''.join(wordle_pattern)

# Function to run the game
def game(console, chosen_word):
    end_of_game = False
    already_guessed = []
    full_wordle_pattern = []
    all_words_guessed = []

    while not end_of_game:
        guess = Prompt.ask(GUESS_STATEMENT).upper()
        while len(guess) != 5 or guess in already_guessed:
            if guess in already_guessed:
                console.print("[red]You've already guessed this word!!\n[/]")
            else:
                console.print('[red]Please enter a 5-letter word!!\n[/]')
            guess = Prompt.ask(GUESS_STATEMENT).upper()
        already_guessed.append(guess)
        guessed, pattern = check_guess(guess, chosen_word)
        all_words_guessed.append(guessed)
        full_wordle_pattern.append(pattern)

        # Display all guesses with their patterns
        console.print(*all_words_guessed, sep="\n")
        
        # End game conditions
        if guess == chosen_word or len(already_guessed) == ALLOWED_GUESSES:
            end_of_game = True
    
    # After game finishes, print result
    if len(already_guessed) == ALLOWED_GUESSES and guess != chosen_word:
        console.print(f"\n[red]WORDLE X/{ALLOWED_GUESSES}[/]")
        console.print(f'\n[green]Correct Word: {chosen_word}[/]')
    else:
        console.print(f"\n[green]WORDLE {len(already_guessed)}/{ALLOWED_GUESSES}[/]\n")
    
    console.print(*full_wordle_pattern, sep="\n")

# ✅ Correct main function call
if __name__ == "__main__":
    console = Console()
    chosen_word = choice(word_list)
    console.print(WELCOME_MESSAGE)
    console.print(PLAYER_INSTRUCTIONS)
    game(console, chosen_word)



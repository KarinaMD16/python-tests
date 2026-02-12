from termcolor import colored
import random

# this file contains functions for a wordle game, where the player has to guess a 5-letter word.

# palabra de 5 letras. 
# si una letra es correcta y está en la posición correcta, se muestra en verde.
# si una letra es correcta pero está en la posición incorrecta, se muestra en amarillo.
# si una letra no está en la palabra, se muestra en rojo. 

def read_words ():
    try:
        with open('wordleWord.txt', 'r') as file:
            words = file.read().splitlines()
        return words
    except FileNotFoundError:
        print('wordleWord.txt does not exist.')
        return []

def score_guess(secret_word, guess):
    color = ['red'] * len(guess)
    remaining = list(secret_word)  # letras pendientes

    # verdes
    for i, letter in enumerate(guess):
        if letter == secret_word[i]:
            color[i] = 'green'
            remaining[i] = None

    # amarillas
    for i, letter in enumerate(guess):
        if color[i] == 'red' and letter in remaining:
            color[i] = 'yellow'
            remaining[remaining.index(letter)] = None

    return color

def render_guess(guess, color):
    output = []
    for letter, state in zip(guess, color):
        output.append(colored(letter, state))
    print(' '.join(output))


def get_guess():
    """Prompts the user for a word guess and validates the input."""
    while True:
        guess = input('Enter a word: ').lower()
        if len(guess) != 5:
            print('Please enter a 5-letter word.')
        elif not guess.isalpha():
            print('Please enter a valid word (a-z).')
        else:
            return guess
        
def play_game(words):
    secret_word = random.choice(words)
    attempts = 6

    while attempts > 0:
        guess = get_guess()

        if guess == secret_word:
            print(colored(' '.join(secret_word), 'green'))
            return

        states = score_guess(secret_word, guess)
        render_guess(guess, states)
        attempts -= 1

    print(f'Sorry, you ran out of attempts. The word was: {secret_word}')

def main():
    words = read_words()
    if not words:
        return
    play_game(words)

if __name__ == '__main__':
  main()
import re
import random
from termcolor import colored 

# This file contains functions for a wordle game, where the player has to guess a 5-letter word.


def read_words ():
    try:
        with open('words.txt', 'r') as file:
            words = file.read().splitlines()
        return words
    except FileNotFoundError:
        print('words.txt does not exist.')
        return []
    
def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter + ' '
        else:
            display += '_ '
    print(display.strip())

def get_guess(guessed_letters):
  while True:
    guess = input('Enter a letter: ').lower()
    if len(guess) != 1:
      print('Enter only one letter.')
    elif not re.search('[a-z]', guess):
      print('Enter only letters from a to z.')
    elif guess in guessed_letters:
      print('You already guessed that letter.')
    else:
      return guess

def is_word_guessed(word, guessed_letters):
    for letter in word:
        if letter not in guessed_letters:
            return False
    return True

def get_hint(word, guessed_letters):
    for letter in word:
        if letter not in guessed_letters:
            return random.choice([letter])
    return None


def play_game(words):
  secret_word = random.choice(words)

  attempts = 6
  guessed_letters = []
  while attempts > 0:
    display_word(secret_word, guessed_letters)

    guess = get_guess(guessed_letters)
    guessed_letters.append(guess)

    if guess in secret_word:
      print(colored('Correct guess!', 'green'))
      if is_word_guessed(secret_word, guessed_letters):
        print(colored('Congratulations! You guessed the word!', 'green'))
        print(colored(f'The word was: {secret_word}', 'green'))
        return True
    else:
      print(colored('Wrong guess!', 'red'))
      attempts -= 1
      if attempts == 0:
        print(colored(f'Game over! The word was {secret_word}', 'red'))
        return False
    if random.random() < 0.3:  # 30% 
      hint = get_hint(secret_word, guessed_letters)
      if hint:
        print(colored(f'Hint: The word contains the letter "{hint}"', 'yellow'))


def main():
  words = read_words()
  if not words:
    print('No words loaded.')
    return

  wins = 0
  losses = 0

  while True:
    won = play_game(words)
    if won:
      wins += 1
    else:
      losses += 1

    print(colored(f'Session record - Wins: {wins} | Losses: {losses}', 'cyan'))

    again = input('Play again? (y/n): ').strip().lower()
    if again != 'y':
      break

if __name__ == '__main__':
  main()
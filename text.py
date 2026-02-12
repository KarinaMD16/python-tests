import os
from termcolor import colored

def read_file(filename):
  with open(filename, 'r') as file:
    return file.read()
  
def write_file(filename, content):
  with open(filename, 'w') as file:
    file.write(content)

def update_file(filename, content):
    with open(filename, 'a') as file:
        file.write('\n' + content)

def search_and_replace(filename, old_sentence, new_sentence):
    file_content = read_file(filename)
    updated_content = file_content.replace(old_sentence, new_sentence)
    write_file(filename, updated_content)

def delete_file(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print(f'{filename} has been deleted.')
    else:
        print(f'{filename} does not exist.')

def print_note(text, theme):
  print(colored(text, theme))

def get_user_input():
  print('\nEnter your text (type SAVE on a new line to save and exist):')
  
  lines = []
  while True:
    line = input()
    if line == 'SAVE':
      break
    lines.append(line)
  
  return '\n'.join(lines)

def main():
  theme = input('Choose a theme (light_blue/light_magenta/light_cyan): ').strip().lower()
  filename = input('Enter the filename to open or create: ').strip()
  try:
    if os.path.exists(filename):
      print_note(read_file(filename), theme)
      action = input(f'What do you want to do with this note? (u: update, o: overwrite, d: delete, e: exit): ').strip().lower()
      
      if action == 'u':
        u = input('Would you like to append text or search for a sentence and replace it? (a: append, r: replace): ').strip().lower()
        if u == 'a':
          content = get_user_input()
          update_file(filename, '\n' + content)
        elif u == 'r':
            old_sentence = input('Enter the sentence you want to replace: ').strip()
            new_sentence = input('Enter the new sentence: ').strip()
            search_and_replace(filename, old_sentence, new_sentence)
        else:
          print('Invalid option. Exiting.')

      elif action == 'o':
        content = get_user_input()
        write_file(filename, content)

      elif action == 'd':
        delete_file(filename)
        return

      elif action == 'e':
        print('Exiting without changes.')
        return
      else:
        print('Invalid option. Exiting.')

    else:
        content = get_user_input()
        write_file(filename, content)
    print(f'{filename} saved.')
  except OSError:
    print(f'{filename} could not be opened.')

if __name__ == '__main__':
  main()
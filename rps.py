import random

opt_text = '''Select Rock, Paper or Scissors:
[0]: Rock
[1]: Paper
[2]: Scissors
Selection:'''
def option ():
  opt = None
  try:
    opt = int(input(opt_text))
  except ValueError:
    print('\nInvalid Number')
    return option()
  if opt < 0 or opt > 2:
    print('\nNumber must be between 0 and 2')
    return option()
  return opt

def start ():
  opponent = random.randint(0, 2)
  selection = option()
  if selection == opponent:
    return '\nYou tied\n'
  elif (opponent > selection and not (selection == 0 and opponent == 2)) or (selection == 2 and opponent == 0):
    return '\nYou lost\n'
  else:
    return '\nYou won\n'

while True:
  print(start())
  if input('Play again? Press [n] to stop.').lower() == 'n':
      break

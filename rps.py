import random
stop = False
print("Rock Paper Scissors Time!")
while stop == False:
  opponent = random.choice(["Rock","Paper","Scissors"])
  user = input('Put in your move! (Rock, Paper, or Scissors)').lower()
  if user == "rock" and opponent == "Scissors":
    print("The opponent picked Scissors! You win!")
  elif user == "rock" and opponent == "Paper":
    print("The opponent picked Paper! You lose!")
  elif user == "rock" and opponent == "Rock":
    print("The opponent picked Rock as well! You tie!")
  elif user == "paper" and opponent == "Scissors":
    print("The opponent picked Scissors! You lose!")
  elif user == "paper" and opponent =="Rock":
    print("The opponent picked Rock! You win!")
  elif user == "paper" and opponent == "Paper":
    print("The opponent picked Paper as well! You tie!")
  elif user == "scissors" and opponent == "Paper":
    print("The opponent picked Paper! You win!")
  elif user == "scissors" and opponent == "Rock":
    print("The opponent picked Rock! You win!")
  elif user =="scissors" and opponent == "Scissors":
    print("The opponent picked Scissors as well! You tie!")
  chk = input('Would you like to play again? (Yes, No)').lower()
  if chk == "yes":
    stop = False
  else:
    stop = True

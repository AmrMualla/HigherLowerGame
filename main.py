#AmrMualla Higher or Lower, Instagram Follower Edition.

from art import logo, vs
from game_data import data
import random

print(logo)
first_person = random.choice(data)

def HigherorLower(winner, score):
  newgame = random.choice(data)
  print(f"Compare A: {winner['name']}, a {winner['description']}, from {winner['country']}")

  print(vs)

  second_person = random.choice(data)
  print(f"Against B: {second_person['name']}, a {second_person['description']}, from {second_person['country']}")

  choice = input("Who has more followers? Type A or B: ")

  if choice == "A" and winner["follower_count"] > second_person["follower_count"]:
    score += 1
    HigherorLower(winner, score)
  elif choice == "B" and second_person["follower_count"] > winner["follower_count"]:
    score += 1
    HigherorLower(second_person, score)
  elif second_person["follower_count"] == winner["follower_count"]:
    score += 1
    HigherorLower(second_person, score)
  else:
    again = input(f"You lose! Your score was {score}. Would you like to play again? Press 'Y' for Yes and 'N' for No: ")

    if again == "Y":
      HigherorLower(newgame, 0)


HigherorLower(first_person, 0)

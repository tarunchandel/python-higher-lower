from replit import clear
from art import logo
from art import vs
from game_data import data
import random

def print_details(name, choice):
  print (f'Compare {name}: {choice["name"]}, a {choice["description"]}, from {choice["country"]}')

def check_answer(a, b, answer):
  """Takes the two choices, checks who has more followers and returns True if user answer matches the correct answer."""
  if a["follower_count"] >= b["follower_count"]:
    return answer == "a"
  else: 
    return answer == "b"
  

def game():
  game_continue_flag = True
  score = 0
  choice_a = random.choice(data)
  choice_b = random.choice(data)

  print (logo)

  while game_continue_flag:
    choice_a = choice_b

    while choice_a == choice_b:
      choice_b = random.choice(data)

    print_details("A", choice_a)
    print (vs)
    print_details("B", choice_b)

    user_answer = input("Who has more followers? Type 'A' or 'B': ").lower()

    clear()
    print(logo)
      
    if check_answer(choice_a, choice_b, user_answer):
      score += 1
      print (f"You're right! Current score: {score}.")
      
    else:
      print(f"Sorry, that's wrong. Final score: {score}")
      game_continue_flag = False

game()


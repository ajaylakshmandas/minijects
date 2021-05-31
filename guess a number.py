#we guess computer number

import random

def guess(x):
  random_number = random.randint(1,x)
  guess = 0 
  while guess != random_number:
    guess= int(input(f"select any nukmber between 1 to {x} :"))
    if guess > random_number:
      print("your gess is to high")
    elif guess < random_number:
      print("your guess is too low")

  print(f"yes you got the right answer {random_number} correctly")

guess(10)



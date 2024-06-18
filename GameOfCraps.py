import random

def play_dice_game():
  dice1 = random.randint(1, 6)
  dice2 = random.randint(1, 6)
  dice3 = dice1 + dice2

  print("Dice 1 =", dice1)
  print("Dice 2 =", dice2)
  print("You rolled a", dice3)

  if dice3 == 7 or dice3 == 11:
    print("You win!")
    return
  elif dice3 == 2 or dice3 == 3 or dice3 == 12:
    print("You lose!")
    return

  dice_point = dice3
  while True:
    print("Would you like to roll again? (y/n)")
    answer = input().lower()

    if answer == 'y':
      new_dice1 = random.randint(1, 6)
      new_dice2 = random.randint(1, 6)
      new_dice_sum = new_dice1 + new_dice2
      print("You rolled", new_dice1, "and", new_dice2, "for a sum of", new_dice_sum)

      if new_dice_sum == 7:
        print("Craps! You lose.")
        break
      elif new_dice_sum == dice_point:
        print("You rolled your point!", dice_point, ". You win!")
        break
    else:
      print("Thanks for playing!")
      break

play_dice_game()

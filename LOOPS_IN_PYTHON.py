# creating a tooser
#
# import random
#
# number = random.randint(0, 1)
#
# if number == 1:
#     print("heads")
# else:
#     print("tails")

# import random
# friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
#
# # random.randint(0, len(friends) - 1)
#
# print(friends[random.randint(0, len(friends) - 1)])

import random
from email.mime import image

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

images = [rock, paper, scissors]

computer_choice = random.choice(images)

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors: "))
print(computer_choice)
print("Computer choice")
user_image_choice = images[user_choice]

print(user_image_choice)
print("user_image_choice")
print()
if user_image_choice == rock and computer_choice == paper:
    print("you loose")
elif user_image_choice == paper and computer_choice == scissors:
    print("you loose")
elif user_image_choice == scissors and computer_choice == paper:
    print("you win")
elif user_image_choice == scissors and computer_choice == rock:
    print("you loose")
elif user_image_choice == rock and computer_choice == scissors:
    print("you win")
elif user_image_choice == paper and computer_choice == rock:
    print("you win")
else:
    print("Draw")
# fruits = ["apple", "banana", "cherry"]
#
# for fruit in fruits:
#     print(fruit)
#
#
# heights = [22,33, 53, 22, 66]
#
# sum_of_heights = 0
# for height in heights:
#     sum_of_heights += height
# print(sum_of_heights)
# total_person = 0
# for total_people in heights:
#     total_person += 1
# print(total_person)
#
# average_height = sum_of_heights / total_person
# print(average_height)
#
# student_scores = [150, 140, 156, 180, 96, 20]
#
# largest_score = student_scores[0]
# for score in student_scores:
#     if score > largest_score:
#         largest_score = score
#
# print(largest_score)
#
#
# total = 0
#
# for number in range(1, 101):
#     if number % 2 == 0:
#         total = total + number
# print(total)


# the fizz buzz problem

# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)


# building a password generator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the py password")

nr_letters = int(input("How many letters would you like? "))
nr_symbols = int(input("How many symbols would you like? "))
nr_numbers = int(input("How many numbers would you like? "))

password = []

for char in range(1,nr_letters+1):
    random_char = random.choice(letters)
    password.append(random_char)

for num in range(1,nr_numbers+1):
    random_num = random.choice(numbers)
    password.append(random_num)

for symbol in range(1,nr_symbols+1):
    random_symbol = random.choice(symbols)
    password.append(random_symbol)
print(password)
random.shuffle(password)
print(password)
password_string = "".join(password)
print(password_string)
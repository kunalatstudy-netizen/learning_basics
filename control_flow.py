# number = 3
#
# if number % 2 == 0:
#     print("even")
# else:
#     print("odd")

# upgrading the bmi

# height = float(input("Enter your height in m: "))
# weight = float(input("Enter your weight in kg: "))
#
# BMI = weight / (height ** 2)
#
# if BMI < 18.5:
#     print("You are underweight")
# elif BMI >=18.5 and BMI <25:
#     print("You are normal")
# elif BMI >=25 and BMI <30:
#     print("overweith")
# elif BMI >=30 and BMI <35:
#     print("obesity")
# else:
#     print("clinicaly obese")


# creating a leap year calculator

# year = 2026
#
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print(f"{year} is a leap year")
#         else:
#             print(f"{year} is not a leap year")
#     else:
#         print(f"{year} is a leap year")
# else:
#     print(f"{year} is not a leap year")

# piza prize calculator

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

total_bill = 0
if size == "S":
    total_bill += 15
elif size == "M":
    total_bill += 20
elif size == "L":
    total_bill += 25

if pepperoni == "Y":
    if size == "S":
        total_bill += 2
    else:
        total_bill += 3

if extra_cheese == "Y":
    total_bill += 1

print(f"Total bill: {total_bill}")
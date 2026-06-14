# write a program that adds the digit in a 2 digit number

# two_digit_number = input("What is your two digit number?")
# sum_of_two_digit = int(two_digit_number[0]) + int(two_digit_number[1])
# print(sum_of_two_digit)

# creating a bmi calculator

# weight = int(input("Enter your weight in kg: "))
# height = float(input("Enter your height in m: "))
#
# bmi = weight / (height ** 2)
# print(bmi)


# creating a tip calculator

print("Welcome to the tip calculator")
total_bill = float(input("Please enter the total bill: "))
tip = int(input("How much tip would you like to give 10, 12, or 15: "))
total_people = int(input("How many people to split the bill? "))

bill_after_tip_per = total_bill / 100 * tip
total_bill_after_tip = bill_after_tip_per + total_bill / total_people
print(f"Each person should pay ${total_bill_after_tip:.2f}")

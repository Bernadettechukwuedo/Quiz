import time

score = 0
# THE GAME STARTS HERE

print("Welcome To Maths Quiz \U0001F600 \n")
player = input("Enter your name: ").upper()
print(f"Welcome {player}")
time.sleep(2)
print(
    "We have 2 stages and each stage is made up of 3 questions making it a total of 6 questions.\n"
)
print(f"Are you ready {player} \n")
print("Just a minute")
time.sleep(4)

print("-------------------------------------------------\n")

# FIRST STAGE
print("STAGE ONE")

print("Find the value of X in the simple euation")

question1 = int(input("2x + 4 = 6 . The value of x is: "))
if question1 == 1:
    score += 1
    print(f"CORRECT!!, score = {score}")
else:
    score += 0
    print(f"WRONG!!, score = {score}")

print("NEXT QUESTION")
time.sleep(2)

question2 = int(input("3x-3=6 . The value of x is: "))
if question2 == 3:
    score += 1
    print(f"CORRECT!!, score = {score}")
else:
    score += 0
    print(f"WRONG!!, score = {score}")

print("NEXT QUESTION")
time.sleep(2)

question3 = int(input("3x = 6 . The value of x is: "))
if question3 == 2:
    score += 1
    print(f"CORRECT!!, score = {score}")
else:
    score += 0
    print(f"WRONG!!, score = {score}")


# SECOND STAGE
print("-------------------------------------------------\n")
time.sleep(2)
print("STAGE TWO")

print("Answer the following word problem")

time.sleep(2)

question4 = input(
    "The day after two days ago is wednesday, what is the day after tomorrow: "
).upper()
if question4 == "FRIDAY":
    score += 1
    print(f"CORRECT!!, score = {score}")
else:
    score += 0
    print(f"WRONG!!, score = {score}")


print("NEXT QUESTION")
time.sleep(2)

question5 = int(
    input("I was 7 years when my father was 42 now he is 60, how old am I: ")
)
if question5 == 25:
    score += 1
    print(f"CORRECT!!, score = {score}")
else:
    score += 0
    print(f"WRONG!!, score = {score}")


print("NEXT QUESTION")
time.sleep(2)

question6 = input("If the day before two days ago is Monday, What is today ").upper()
if question6 == "Thursday":
    score += 1
    print(f"CORRECT!!, score = {score}")
else:
    score += 0
    print(f"WRONG!!, score = {score}")


time.sleep(2)
# PRINTING SCORE
print(f"CONGRATULATIONS, YOUR TOTAL SCORE IS {score}")

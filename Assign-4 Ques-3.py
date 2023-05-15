import random

for i in range(10):
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    answer = num1 * num2
    user_answer = int(input("Question " + str(i+1) + ": " + str(num1) + " x " + str(num2) + " = "))
    if user_answer == answer:
        print("Right!")
    else:
        print("Wrong. The answer is", answer)

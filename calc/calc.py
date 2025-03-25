number0 = int(input("First number : "))
number1 = int(input("Second number : "))
print("A = Add , S = Subtract , M = Multiply , D = Divide")
question = input("What do you want to do? : ")
answerA = number0 + number1
answerS = number0 - number1
answerM = number0 * number1
answerD = number0 / number1
if question == "A":
    print(f"The answer is : {answerA}")
elif question == "a":
    print(f"The answer is : {answerA}")
elif question == "S":
    print(f"The answer is : {answerS}")
elif question == "s":
    print(f"The answer is : {answerS}")
elif question == "M":
    print(f"The answer is : {answerM}")
elif question == "m":
    print(f"The answer is : {answerM}")
elif question == "D":
    print(f"The answer is : {answerD}")
elif question == "d":
    print(f"The answer is : {answerD}")
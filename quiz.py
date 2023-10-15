def quiz():
    print("Answer as many questions as you can :)")
    question1_str = input("1. What year did Nigeria gain independence?:, A.1980, B.1730, C.1960 ")
    question1_str = str(question1_str)
    if question1_str == "B":
        print("Incorrect the answer is C")
        print("Next Question")
    elif question1_str == "A":
        print("Incorrect the answer is C")
        print("Next Question")
    elif question1_str == "C":
        print("Correct")
        print("Next Question")

    question2_str = input("2. Which Country is Obama from?:, A.USA, B.South Africa, C.Togo ")
    question2_str = str(question2_str)
    if question2_str == "B":
        print("Correct")
        print("Next Question")
    elif question2_str == "A":
        print("Incorrect the answer is B")
        print("Next Question")
    elif question2_str == "C":
        print("Incorrect the answer is B")
        print("Next Question")

    question3_str = input("3. Who is the most commonly referred as the 'GOAT'?:, A.Messi, B.Jesse, C.Ronaldo ")
    question3_str = str(question3_str)
    if question3_str == "B":
        print("Incorrect the answer is A")
        print("Next Question")
    elif question3_str == "A":
        print("Correct")
        print("Next Question")
    elif question3_str == "C":
        print("Incorrect the answer is A")
        print("Next Question")

    question4_str = input("4. What is Lucky's nick name:, A.Intelli J, B.Kulisevski, C.Echo ")
    question4_str = str(question4_str)
    if question4_str == "B":
        print("Correct")
        print("Next Question")
    elif question4_str == "A":
        print("Incorrect the answer is B")
        print("Next Question")
    elif question4_str == "C":
        print("Incorrect the answer is B")
        print("Next Question")

    question5_str = input("5. Which state is Mr Adam from?:, A.Edo, B.Cross River, C.Calabar ")
    question5_str = str(question5_str)
    if question5_str == "B":
        print("Incorrect the answer is C")
        print("This is the end of the quiz, Thanks of playing :)")
    elif question1_str == "A":
        print("Incorrect the answer is C")
        print("This is the end of the quiz, Thanks of playing :)")
    elif question1_str == "C":
        print("Correct")
        print("This is the end of the quiz, Thanks of playing :)")


print(quiz())
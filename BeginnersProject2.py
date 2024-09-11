import os, random, time
def GuessFruit(round=7):
    os.system('clear')
    print("✩░▒▓▆▅▃▂▁Welcome to Forest Treasure Hunt!▁▂▃▅▆▓▒░✩")
    time.sleep(1)
    print("\nYou enter a forest and have to play a series of games to survive.")
    time.sleep(2.5)
    print("\nBOOOOOOOM! A wild monkey appears.")
    time.sleep(2)
    print("\nMonkey: \"Do you know all of my favourite fruits?\"")
    time.sleep(2)
    print("\n\"You cannot pass until five fruits have been guessed!\"")
    time.sleep(2)
    print("\nGood luck!")
    time.sleep(2)
    os.system('clear')
    print("✩░▒▓▆▅▃▂▁Welcome to Forest Treasure Hunt!▁▂▃▅▆▓▒░✩")
    correct = set()
    print("Monkey: \"You cannot pass until five fruits have been guessed!\"")
    fruits = {"kiwi","mango","watermelon","cherry","peach"}
    times = 1
    while times <= round:
        guess = set()
        for a in range(5):
            userinput = input("Guess five fruits, one by one: ")
            while not userinput.isalpha() or len(userinput) <= 1:
                print("Invaild input. Please try again.")
                userinput = input("Guess five fruits, one by one: ")
            userinput = userinput.lower()
            guess.add(userinput)
        for i in guess:
            if i in fruits:
                correct.add(i)
        if len(correct) == 5:
            print(f"Well done! The five fruits were {", ".join(fruits)}. You've tried {times} times.")
            time.sleep(3)
            print("Monkey: \"You can pass now! :)\"")
            time.sleep(3)
            break
        os.system("clear")
        print("✩░▒▓▆▅▃▂▁Welcome to Forest Treasure Hunt!▁▂▃▅▆▓▒░✩")
        if len(correct) > 2:
            print("Your guess of "+", ".join(correct)+" are correct. Try to get five of them correct!")
        elif len(correct) == 1:
            print("Your guess of "+"".join(correct)+" is correct. Try to get five of them correct!")
        else:
            print("None of your guess is correct.")
        times += 1
    if times > round:
        time.sleep(1)
        print("Oh no... you've tried too many times.")
        time.sleep(2)
        print("Monkey: \"I'm so disappointed in you.\"")
        time.sleep(2)
        exit("\033[1;31mGAME OVER :(")

def tiger(min=160,max=180):
    os.system('clear')
    print("✩░▒▓▆▅▃▂▁Welcome to Forest Treasure Hunt!▁▂▃▅▆▓▒░✩")
    time.sleep(1)
    print("\nOMG!!! There is a hungry tiger!")
    time.sleep(2)
    print("\nThe only way out is the nearest that needs you to cross a river.")
    time.sleep(2.5)
    print("\nYou have to be tall enough to cross the river or you will drown.")
    time.sleep(3)
    print("\nGood luck!")
    time.sleep(2)
    os.system('clear')
    print("✩░▒▓▆▅▃▂▁Welcome to Forest Treasure Hunt!▁▂▃▅▆▓▒░✩")
    print("You have to be tall enough to cross the river!")
    height = input("Enter your height in centimeters: ")
    while not height.isnumeric():
        print("Invaild input. Please try again.")
        height = input("Enter your height in centimeters: ")
    height = float(height)
    if height <= min:
        print("OH NO! You drown because the river was too high.")
        time.sleep(1)
        exit("\033[1;31mGAME OVER :(")
    elif height > max:
        print("OH NO! You are hunted down by the hungry tiger because you are too easily spotted.")
        time.sleep(1)
        exit("\033[1;31mGAME OVER :(")
    else:
        print("Great! You passed the river!")
        time.sleep(2)
        
def GuessPassword(digit=4,round=10):    
    os.system("clear")
    print("✩░▒▓▆▅▃▂▁Welcome to Forest Treasure Hunt!▁▂▃▅▆▓▒░✩")
    time.sleep(1)
    print("\nLastly, there is a door that requires a password to unlock.")
    time.sleep(2)
    print("\nIt is a series of different numbers, and you'll have 10 chances to guess it!")
    time.sleep(2)
    print("\nGood luck!")
    time.sleep(2)
    os.system("clear")
    times = 0
    password = set()
    while len(password) < digit:
        password.add(random.randint(0,9))
    while times <= round:
        current = [int(i) for i in password]
        os.system("clear")
        print("✩░▒▓▆▅▃▂▁Welcome to Forest Treasure Hunt!▁▂▃▅▆▓▒░✩")
        print(f"The password is a series of {digit} different numbers, and you still have {f"{round-times} chances" if round-times > 1 else "one more chance"} to guess!")
        correct = 0
        check = set()
        ans = input("Enter the password: ")
        while not ans.isnumeric() or len(ans) != digit:
            print("Invaild input. Please try again.")
            ans = input("Enter the password: ")
        for n in ans:
            n = int(n)
            if n in password:
                check.add(n)
        for i in check:
            if i in password:
                correct += 1
                current.remove(i)
        if correct == digit:
            print("Congets!! The door is unlook for you!")
            time.sleep(2)
            break
        elif correct > 1:
            print(f"You guessed {correct} numbers correctly.")
        elif correct == 1:
            print(f"You guessed {correct} number correctly.")
        else:
            print("None of your guess is correct.")
        times += 1
        time.sleep(2)
    if correct != digit:
        time.sleep(1)
        print("Oh no... because you've tried too many times, the door is looked FOREVER.")
        time.sleep(1)
        print(f"The password was "+"".join(str(i) for i in password)+".")
        time.sleep(1)
        exit("\033[1;31mGAME OVER :(")

def quiz():
    os.system('clear')
    print("✩░▒▓▆▅▃▂▁Welcome to Python Quiz!▁▂▃▅▆▓▒░✩")  
    time.sleep(1)
    print("\nThere are some multichoice questions about Python.")
    time.sleep(2.5)
    print("\nYou have to try your best to answer all of them correctly!")
    time.sleep(2)
    print("\nGood luck!")
    time.sleep(2.5)
    os.system("clear")
    print("✩░▒▓▆▅▃▂▁Welcome to Python Quiz!▁▂▃▅▆▓▒░✩")
    multichioces = {"What symbol is used in python to assign values to a variable?\n    a) Asterisk * \n    b) Equals = \n    c) Plus + \n    d) Forward slash /":"b",
                    "What will be the output?\n 1| name = \"Dave\"\n 2| print (name)\n\n    a) Dave \n    b) (name) \n    c) name \n    d) \"Dave\"":"a",
                    "What will be the output?\n 1| x = 0\n 2| while (x < 5):\n 3|      print (x)\n\n    a) a bunch of 0's \n    b) 5, 4, 3, 2, 1 \n    c) x \n    d) potato":"a",
                    "When you have an error in your code, what is the term to summarise finding and fixing that error?\n    a) Error hopping \n    b) Syntax finder \n    c) Debugging \n    d) Error finder":"c",
                    "When was Python released?\n    a) February 20 1991 \n    b) September 6 1987 \n    c) June 4 2006 \n    d) April 27 2005":"a",
                    "What is Algorithm?\n    a) Identifying similarities between problems.\n    b) Depending on the condition the algorithm follows a choice between different alternatives.\n    c) A set of instructions given in a particular order.\n    d) A set of step-by-step instructions to achieve a purpose.":"d"}
    questionsList = [m for m in multichioces]
    correct = 0
    round = 1
    for i in multichioces:
        n = random.randint(0,len(questionsList)-1)
        i = questionsList[n]
        print(f"{round}. {i}")
        ans = input(">>")
        while ans.lower() not in ["a","b","c","d"]:
            print("Invaild input. Please try again.")
            ans = input(">>")
        if ans.lower() == multichioces[i]:
            print("Correct!")
            correct += 1
        else:
            print(f"Wrong. The answer was option {multichioces[i]}.")
        questionsList.remove(i)
        round += 1
        time.sleep(1.5)
        os.system("clear")
        print("✩░▒▓▆▅▃▂▁Welcome to Python Quiz!▁▂▃▅▆▓▒░✩")
    score = int(correct*100/len(multichioces))
    print(f"\nThat's the end of the quiz!")
    time.sleep(2)
    print(f"\nYou've got {correct} {"correct" if correct <= 1 else "corrects"} out of {len(multichioces)} {"question" if len(multichioces) <= 1 else "questions"}.\nScore: {score}%\n")
    time.sleep(2)
    if score == 100:
        print("\033[1;93mExcellent! You are the master of Python!")
    elif 80 <= score < 100:
        print("Awesome work! You got most of them correctly!")
    elif 50 <= score < 80:
        print("You're almost there! Keep going and you can do it!")
    else:
        print("You need more practice. Try to get all of them correct!")
    time.sleep(2.5)
    
def main():
    os.system('clear')
    print("\033[0;0m\nMenu:\n")
    time.sleep(1)
    print("1. Forest Treasure Hunt")
    time.sleep(1)
    print("\n2. Python Quiz")
    time.sleep(1)
    print("\n3. Exit")
    time.sleep(1.5)
    print("\nDo you want to try another game, restart or exit?")
    time.sleep(2)
    n = input("\nPlease select an option (1-3): ")
    while n not in ["1","2","3"]:
        print("Invalid choice. Please select a valid option.")
        n = input("Please select an option (1-3): ")
    n = int(n)
    if n == 1:
        GuessFruit()
        tiger()
        GuessPassword()
        os.system("clear")
        time.sleep(0.5)
        print("\033[1;93mCherrs! You survive from the dangerous forest and find a shiny treasure!")
        time.sleep(1)
    elif n == 2:
        quiz()
    else:
        exit("\033[1;93mThanks for playing! Hope to see you next time!\n")

vision = random.randint(1,2)
vision = 2
if vision == 1:
    GuessFruit()
    tiger()
    GuessPassword()
    os.system("clear")
    time.sleep(0.5)
    print("\033[1;93mCherrs! You survive from the dangerous forest and find a shiny treasure!")
    time.sleep(1)
elif vision == 2:
    quiz()

while __name__ == "__main__":    main()
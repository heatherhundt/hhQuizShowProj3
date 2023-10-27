#title
print(r"""
                 _________  ___  ___  _______           ________  ___  ___  ___  ________  ___       
                |\___   ___\\  \|\  \|\  ___ \         |\   __  \|\  \|\  \|\  \|\_____  \|\  \      
                \|___ \  \_\ \  \\\  \ \   __/|        \ \  \|\  \ \  \\\  \ \  \\|___/  /\ \  \     
                     \ \  \ \ \   __  \ \  \_|/__       \ \  \\\  \ \  \\\  \ \  \   /  / /\ \  \    
                      \ \  \ \ \  \ \  \ \  \_|\ \       \ \  \\\  \ \  \\\  \ \  \ /  /_/__\ \__\   
                       \ \__\ \ \__\ \__\ \_______\       \ \_____  \ \_______\ \__\\________\|__|   
                        \|__|  \|__|\|__|\|_______|        \|___| \__\|_______|\|__|\|_______|   ___ 
                                                                 \|__|                          |\__\
                                                                                                \|__|

""")

#The rules of the game
print("      Welcome to The Quiz! Where you will answer a few true and false questions.") 
print("      Please ONLY enter the letter 'T' for True answers OR the letter 'F' for False answers.") 
print("                          Good Luck!")

print()
print()

#Questions 3 true/false
questions = ("Q1. The planet Venus has no moons", "Q2. The Internet was created by a U.S. military research agency", "Q3. A firewall is a type of hardware" )
      
#Answers 3 true/false
answers = ("T", "T", "F")

#Calculate the number of questions
numberOfQuestions = len(questions)
count = 0

#ONE loop for each question
for index in range(numberOfQuestions):
    print(questions[index])
    answer = input("Enter your answer: ")
    if answer == answers[index]:
        print("Correct!")
      
        count += 1
    else:
        print("Incorrect!")
        print("The correct answer is: " + answers[index])
        print()

#The end of the program
print(f"you got {count} out of 3 correct! Great Job!")
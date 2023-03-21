from questions import *
from operations import *

quiz_obj = quiz()

class main:
    def execute(self):
        print("\n","1) Operators in Python","\n","2) Lists in Python","\n","3) File Handling","\n","4) Classes and Objects","\n","5) OOPs","\n")
        choice = int(input("Enter the number of quiz you want : "))
        if choice == 1:
            print("---------------------------------------------------------------------------------","\n")
            quiz_obj.opt_quiz()
            print("---------------------------------------------------------------------------------","\n")
            while True:
                option = int(input("Enter\n1. To Show your score\n2. To show the correct answers of all questions\n3. To Exit :\n"))
                print("---------------------------------------------------------------------------------","\n")
                if option == 1:
                    quiz_obj.score()
                elif option == 2:
                    quiz_obj.result()
                elif option == 3:
                    exit()
                else:
                    print("Option doesn't exist")
        elif choice == 2:
            print("---------------------------------------------------------------------------------","\n")
            quiz_obj.lists_quiz()
            print("---------------------------------------------------------------------------------","\n")
            while True:
                option = int(input("Enter\n1. To Show your score\n2. To show the correct answers of all questions\n3. To Exit :\n"))
                print("---------------------------------------------------------------------------------","\n")
                if option == 1:
                    quiz_obj.score()
                elif option == 2:
                    quiz_obj.result()
                elif option == 3:
                    exit()
                else:
                    print("Option doesn't exist")
        elif choice == 3:
            print("---------------------------------------------------------------------------------","\n")
            quiz_obj.file_handling_quiz()
            print("---------------------------------------------------------------------------------","\n")
            while True:
                option = int(input("Enter\n1. To Show your score\n2. To show the correct answers of all questions\n3. To Exit :\n"))
                print("---------------------------------------------------------------------------------","\n")
                if option == 1:
                    quiz_obj.score()
                elif option == 2:
                    quiz_obj.result()
                elif option == 3:
                    exit()
                else:
                    print("Option doesn't exist")
        elif choice == 4:
            print("---------------------------------------------------------------------------------","\n")
            quiz_obj.classes_and_objects_quiz()
            print("---------------------------------------------------------------------------------","\n")
            while True:
                option = int(input("Enter\n1. To Show your score\n2. To show the correct answers of all questions\n3. To Exit :\n"))
                print("---------------------------------------------------------------------------------","\n")
                if option == 1:
                    quiz_obj.score()
                elif option == 2:
                    quiz_obj.result()
                elif option == 3:
                    exit()
                else:
                    print("Option doesn't exist")
        elif choice == 5:
            print("---------------------------------------------------------------------------------","\n")
            quiz_obj.oops_quiz()
            print("---------------------------------------------------------------------------------","\n")
            while True:
                option = int(input("Enter\n1. To Show your score\n2. To show the correct answers of all questions\n3. To Exit :\n"))
                print("---------------------------------------------------------------------------------","\n")
                if option == 1:
                    quiz_obj.score()
                elif option == 2:
                    quiz_obj.result()
                elif option == 3:
                    exit()
                else:
                    print("Option doesn't exist")

        else:
            print("\nOption doesn't exist")

if __name__ == "__main__":
    main_obj = main()
    print("\n","---------------------------------------------------------------------------------","\n")
    print("********Welcome to Quiz application********")
    print("\nRules :\nThere are 5 quiz of different topics\nYou have to choose one quiz and then the quiz will start\nThere are 10 mcq in each quiz\nAll the questions are of single selection\nEach question consists of 10 marks\nTotal 100 marks\n Passing marks 70/100\n")
    while True:
        main_obj.execute()
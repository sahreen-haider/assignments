from questions import *

class quiz:
    ans_lst = []
    answers = []
    correct_ans = []
    ques_lst = []
    def opt_quiz(self):
        quiz.ques_lst = list(operators.keys())
        quiz.answers = operators_answers.copy()
        for i in operators.keys():
            print("\n" , i , "\n")
            for j in operators[i]:
                print(j , "\n")
            answer = input("Enter your answer : ")
            print("\n","---------------------------------------------------------------------------------","\n")
            quiz.ans_lst.append(answer)

    def lists_quiz(self):
        quiz.ques_lst = list(lists.keys())
        quiz.answers = lists_answers.copy()
        for i in lists.keys():
            print("\n" , i , "\n")
            for j in lists[i]:
                print(j , "\n")
            answer = input("Enter your answer : ")
            print("\n","---------------------------------------------------------------------------------","\n")
            quiz.ans_lst.append(answer)

    def file_handling_quiz(self):
        quiz.ques_lst = list(file_handling.keys())
        quiz.answers = file_handling_answers.copy()
        for i in file_handling.keys():
            print("\n" , i , "\n")
            for j in file_handling[i]:
                print(j , "\n")
            answer = input("Enter your answer : ")
            print("\n","---------------------------------------------------------------------------------","\n")
            quiz.ans_lst.append(answer)

    def classes_and_objects_quiz(self):
        quiz.ques_lst = list(classes_and_objects.keys())
        quiz.answers = classes_and_objects_answers.copy()
        for i in classes_and_objects.keys():
            print("\n" , i , "\n")
            for j in classes_and_objects[i]:
                print(j , "\n")
            answer = input("Enter your answer : ")
            print("\n","---------------------------------------------------------------------------------","\n")
            quiz.ans_lst.append(answer)

    def oops_quiz(self):
        quiz.ques_lst = list(oops.keys())
        quiz.answers = oops_answers.copy()
        for i in oops.keys():
            print("\n" , i , "\n")
            for j in oops[i]:
                print(j , "\n")
            answer = input("Enter your answer : ")
            print("\n","---------------------------------------------------------------------------------","\n")
            quiz.ans_lst.append(answer)

    def score(self):
        print("********RESULT********","\n")
        for i in range(10):
            if quiz.ans_lst[i] == quiz.answers[i]:
                quiz.correct_ans.append(quiz.ans_lst[i])
        score = len(quiz.correct_ans) * 10
        if score < 70:
            print("Failed!!!","\n","Better Luck next time","\n")
            print(len(quiz.correct_ans),"/10 answers are correct","\n")
            print("Total Marks : ",score,"/100","\n")
        else:
            print("Congraulations!!!","\n","You have passed in Quiz","\n")
            print(len(quiz.correct_ans),"/10 answers are correct","\n")
            print("Total Marks : ",score,"/100","\n")

    def result(self):
        sno = 0
        no = 0
        print("---------------------------------------------------------------------------------","\n")
        print("********Questions********","\n")
        for i in quiz.ques_lst:
            print(i)
        print("\n","Your Answers : ")
        for j in quiz.ans_lst:
            sno += 1
            print(sno,") ",j,"\n")
        print("\n","Correct Answers : ")
        for k in quiz.answers:
            no += 1
            print(no,") ",k,"\n")
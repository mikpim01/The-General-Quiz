#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generalQuiz/quiz.py
# by William Neild

from json import loads
from random import shuffle
from generalQuiz import db
from generalQuiz.helper import cprint, pline

class Quiz:
    def __init__(self, qid, user):
        quiz = db.Get.quiz(qid)
        questions = db.Get.questions(quiz[0])
        self.startPage(quiz, questions, user)

    def startPage(self, quiz, questions, user):
        cprint("Choose your level")
        pline("~")
        cprint("1. Easy (2 Options)")
        cprint("2. Medium (3 Options)")
        cprint("3. Hard (4 Options)")
        pline("=")
        difficulty = None
        while isinstance(difficulty, int) != True:
            try:
                difficulty = int(input("> "))
            except Exception:
                cprint("That was not a difficulty, please try again", "lightred")
        pline("=")
        print("\n")
        cprint("Starting " + quiz[1] + " Quiz")
        print("\n")
        self.startQuiz(quiz, questions, difficulty, user)

    def startQuiz(self, quiz, questions, difficulty, user):
        pline("=")
        shuffle(questions)
        currentQuestion = 0
        numOfOptions = difficulty + 1
        score = 0
        for question in questions:
            answerAccepted = False
            currentQuestion += 1
            cprint(str(currentQuestion) + ". " + str(question[2]))
            pline("~")
            correctAns = question[3]
            otherAns = loads(question[4])
            shuffle(otherAns)
            options = []
            for i in range(0, difficulty):
                options.append(otherAns[i])
            options.append(correctAns)
            shuffle(options)
            opt = 0
            for option in range(0, numOfOptions):
                opt += 1
                cprint(str(opt) + ". " + options[option])
            userAnswer = None
            while answerAccepted != True:
                try:
                    userAnswer = int(input("Answer > "))
                    if (userAnswer <= numOfOptions) != True:
                        raise
                    if (userAnswer >= 1) != True:
                        raise
                    answerAccepted = True
                except Exception:
                    cprint("That was not an Answer, please try again", "lightred")
            if options[userAnswer-1] == correctAns:
                score+=1
            pline("=")
        cprint("Quiz Finished")
        totalQuestions = len(questions)
        totalCorrect = score
        totalPercentage = (totalCorrect / totalQuestions) * 100

        if difficulty == 1:
            diff = "EASY"
        elif difficulty == 2:
            diff = "MEDIUM"
        elif difficulty == 3:
            diff = "HARD"
        else:
            print("Error, Difficulty somehow got messed up!")


        cprint("Total Questions: " + str(totalQuestions))
        cprint("Correct Answers: " + str(totalCorrect))
        cprint("Percent Correct: " + str("{0:.2f}".format(round(totalPercentage,2))) + "%")
        db.Add.result(quiz[0], quiz[1], user["id"], totalCorrect, totalPercentage, diff)
        pline("=")

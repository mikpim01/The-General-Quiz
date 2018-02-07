from tkinter import *
from generalQuiz import db


class questionGUI:
    def __init__(self, master):
        self.master = master
        master.title("Add Question")
        Label(master, text="Quiz Id", relief=RIDGE,width=10).grid(row=0,column=0)
        Label(master, text="Question", relief=RIDGE,width=50).grid(row=0,column=1)
        Label(master, text="Correct Answer", relief=RIDGE,width=30).grid(row=0,column=2)
        Label(master, text="Incorrect Answer A", relief=RIDGE,width=30).grid(row=0,column=3)
        Label(master, text="Incorrect Answer B", relief=RIDGE,width=30).grid(row=0,column=4)
        Label(master, text="Incorrect Answer C", relief=RIDGE,width=30).grid(row=0,column=5)

        self.quizId = StringVar()
        self.question = StringVar()
        self.correctAns = StringVar()
        self.ansA = StringVar()
        self.ansB = StringVar()
        self.ansC = StringVar()

        Entry(master, width=10, textvariable=self.quizId).grid(row=1, column=0)
        Entry(master, width=50, textvariable=self.question).grid(row=1, column=1)
        Entry(master, width=30, textvariable=self.correctAns).grid(row=1, column=2)
        Entry(master, width=30, textvariable=self.ansA).grid(row=1, column=3)
        Entry(master, width=30, textvariable=self.ansB).grid(row=1, column=4)
        Entry(master, width=30, textvariable=self.ansC).grid(row=1, column=5)

        Button(master, text="Quit", command=master.quit, width=9).grid(row=2, column=0)
        Button(master, text="Add Question", command=self.addQuestion, width=49).grid(row=2, column=1)


    def addQuestion(self):
        print("Adding Question: " + str(self.question.get()))
        quizId = self.quizId.get()
        question = self.question.get()
        correctAns = self.correctAns.get()
        ansA = self.ansA.get()
        ansB = self.ansB.get()
        ansC = self.ansC.get()

        self.quizId.set("")
        self.question.set("")
        self.correctAns.set("")
        self.ansA.set("")
        self.ansB.set("")
        self.ansC.set("")

        incorrectAns = [str(ansA), str(ansB), str(ansC)]

        db.Add.question(quizId, question, correctAns, incorrectAns)
        print(str(quizId), str(question), str(correctAns), str(incorrectAns))


root = Tk()
questionGUI = questionGUI(root)
root.mainloop()

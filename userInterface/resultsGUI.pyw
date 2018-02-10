from tkinter import *
from generalQuiz import db

root = Tk()

Label(text="Quiz Name", relief=RIDGE,width=30).grid(row=0,column=0)
Label(text="Percentage", relief=RIDGE,width=10).grid(row=0,column=1)
Label(text="Difficulty", relief=RIDGE,width=10).grid(row=0,column=2)
Label(text="Date Taken", relief=RIDGE,width=25).grid(row=0,column=3)
row = 1
data = db.Get.results(1)
for result in data:
    Label(text=result[3], relief=RIDGE,width=30).grid(row=row,column=0)
    Label(text=str(result[5])+"%", relief=RIDGE,width=10).grid(row=row,column=1)
    Label(text=result[6], relief=RIDGE,width=10).grid(row=row,column=2)
    Label(text=result[7], relief=RIDGE,width=25).grid(row=row,column=3)
    row+=1

root.title("Quiz Results")
root.mainloop()

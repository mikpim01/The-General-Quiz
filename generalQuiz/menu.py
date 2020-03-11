#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generalQuiz/menu.py
# by William Neild

from generalQuiz import security, db, config, quiz
from generalQuiz.helper import cprint, pline
from shutil import get_terminal_size

config.Create()
database = db.get_database()


class Main:
    def __init__(self):
        pline("=")
        cprint("Welcome to the GeneralQuiz")
        cprint("Created by William Neild")
        pline("=")
        cprint("Please choose an option from the following")
        pline("~")
        self.options()

    def options(self):
        cprint("1. Login or Register an Account")
        cprint("2. Quit Application")
        pline("=")
        option = input("> ")
        if option == "1":
            Account()
        elif option == "2":
            cprint("Cya Later!")
            database.close()
            exit()
        else:
            pline("=")
            cprint(" Not a valid option, Try again ", "lightred")
            pline("=")
            self.options()


class Account:
    def __init__(self):
        pline("=")
        cprint("Do you want to Login or Register?")
        pline("~")
        self.options()

    def options(self):
        cprint("1. Login")
        cprint("2. Register")
        cprint("3. Back to Main Menu")
        pline("=")
        option = input("> ")
        pline("=")
        if option == "1":
            self.login()
        elif option == "2":
            # security.Account.register()
            self.register()
        elif option == "3":
            Main()
        else:
            pline("=")
            cprint(" Not a valid option, Try again ", "lightred")
            pline("=")
            self.options()

    def login(self):
        cprint("Login to your account")
        pline("=")
        cprint("Enter Username")
        cprint("~~~~~~~~~~~~~~")
        username = input("> ")
        cprint("Enter Password")
        cprint("~~~~~~~~~~~~~~")
        password = input("> ")
        userLogin = security.Account.login(username, password)
        if userLogin != False:
            Home(userLogin)
        else:
            cprint(" Login details incorrect ", "lightred")
            self.login()

    def register(self):
        cprint("Register an account")
        pline("=")
        cprint("Enter your First Name")
        fname = input("> ")
        cprint("Enter your Last Name")
        lname = input("> ")
        cprint("Enter your Age")
        age = input("> ")
        cprint("Enter a password")
        password = input("> ")
        cprint("Confirm your password")
        confPassword = input("> ")
        cprint("Enter your year group")
        year = input("> ")
        account = security.Account.validateReg(
            fname, lname, password, confPassword, age, year)
        if account != []:
            pline("!", "lightred")
            for i in account:
                cprint(" " + i + " ", "lightred")
            pline("!", "lightred")
            pline(" ")
            self.register()
        else:
            username = str(fname[:3]) + str(age)
            security.Account.register(
                username, password, fname, lname, age, year)
            cprint("Account created. Your username is: " +
                   username, "lightgreen")
            self.login()


class Home:
    user = None

    def __init__(self, user):
        self.user = user
        pline("=")
        width = int(get_terminal_size()[0])+1
        if width >= 25:
            if width > 65:
                size = "big"
            else:
                size = "small"
            for line in open('generalQuiz/data/' + str(size) + '.txt', 'r'):
                cprint(line.rstrip('\n'), "lightgreen")
        cprint("General Quiz", "lightgreen")
        pline("=")
        cprint("Welcome Back " + self.user["fname"])
        pline("=")
        self.options(user)

    def options(self, user):
        cprint("Choose an option from the following")
        pline("~")
        cprint("1. Take a Quiz")
        cprint("2. Quiz results")
        cprint("3. Profile Options")
        cprint("4. Exit Application")
        pline("=")
        option = input("> ")
        pline("=")
        if option == "1":
            Quiz(user)
            self.options(user)
        elif option == "2":
            Results(user)
        elif option == "3":
            cprint("Profile Options Page")
        elif option == "4":
            database.close()
            exit()
        else:
            cprint("Option Doesn't Exist", "lightred")
            Home(user)


class Quiz:
    quizList = database.get_quizList()

    def __init__(self, user):
        self.list(self.quizList, user)

    def list(self, quizList, user):
        cprint("Quiz List")
        pline("~")
        options = []
        for q in quizList:
            cprint(str(q[0]) + ". " + q[1])
            options.append(int(q[0]))
        pline("=")
        cprint("Choose a quiz to take")
        pline("=")
        quizChoice = input("> ")
        pline("=")

        if isinstance(quizChoice, int) != True:
            try:
                quizChoice = int(quizChoice)
            except Exception:
                cprint("Option should be a number", "lightred")
                pline("=")
                self.list(self.quizList)

        if quizChoice in options:
            quiz.Quiz(quizChoice, user)
        else:
            cprint("Not a quiz", "lightred")
            pline("=")
            self.list(self.quizList)


class Results:
    def __init__(self, user):
        width = get_terminal_size()[0]-1
        data = database.get_results(user["id"])
        self.display(data, width, user)

    def display(self, data, width, user):
        size = int(width/5)
        print("\n{qName:^{sizeTwo}} {score:^{size}} {diff:^{size}} {date:^{size}}".format(size=str(
            size), sizeTwo=str(size*2), qName="Quiz Name", diff="Difficulty", score="Score", date="Date"))
        cprint("~"*(width-4), "lightcyan")
        for result in data:
            print("{qName:^{sizeTwo}} {score:^{size}} {diff:^{size}} {date:^{size}}".format(size=str(size), sizeTwo=str(
                size*2), qName=str(result[3]), diff=str(result[6]), score=str(result[5])+"%", date=str(result[7])))
        Home(user)

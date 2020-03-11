#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generalQuiz/db.py
# by William Neild

import sqlite3
from os import path
from json import dumps
from datetime import datetime


class Database:
    def __init__(self):
        exists = False
        self.connection = None
        self.cursor = None

        if path.exists('main.db'):
            exists = True

        self.connection = sqlite3.connect('main.db')
        self.cursor = self.connection.cursor()
        
        if (exists != True):
            self.connection = sqlite3.connect('main.db')
            self.cursor = self.connection.cursor()

            self.cursor.execute('''CREATE TABLE 'users' (
                'id' INTEGER UNIQUE PRIMARY KEY,
                'username' TEXT,
                'password' TEXT,
                'firstName' TEXT,
                'lastName' TEXT,
                'age' INTEGER,
                'year' TEXT
            );''')

            self.cursor.execute('''CREATE TABLE 'quizlist' (
                'id' INTEGER UNIQUE PRIMARY KEY,
                'name' TEXT
            );''')

            self.cursor.execute('''CREATE TABLE 'questions' (
                'id' INTEGER UNIQUE PRIMARY KEY,
                'quizId' INTEGER,
                'question' TEXT,
                'correctAns' TEXT,
                'otherAns' TEXT
            )''')

            self.cursor.execute('''CREATE TABLE 'results' (
                'id' INTEGER UNIQUE PRIMARY KEY,
                'userId' INTEGER,
                'quizId' INTEGER,
                'quizName' TEXT,
                'totalCorrect' INTEGER,
                'totalPercentage' REAL,
                'difficulty' TEXT,
                'date' TEXT
            )''')

            import populate

    def close(self):
        self.connection.commit()
        self.connection.close()

    def add_user(self, username, password, fname, lname, age, year):
        try:
            query = "INSERT INTO users(username, password, firstName, lastName, age, year) VALUES (?,?,?,?,?,?)"
            data = (str(username), str(password), str(
                fname), str(lname), int(age), str(year))
            self.cursor.execute(query, data)
            self.connection.commit()
        except Exception:
            print("Error with db, cannot import data")

    def add_question(self, quizId, question, correctAns, otherAns):
        try:
            query = "INSERT INTO questions(quizId, question, correctAns, otherAns) VALUES (?,?,?,?)"
            data = (int(quizId), str(question), str(
                correctAns), str(dumps(otherAns)))
            self.cursor.execute(query, data)
            self.connection.commit()
        except Exception:
            print("Error with db, couldnt add question")

    def add_quiz(self, name):
        try:
            query = "INSERT INTO quizlist(name) VALUES (?)"
            data = (str(name),)
            self.cursor.execute(query, data)
            self.connection.commit()
        except Exception as e:
            print("Error with db, cannot create quiz" + str(e))

    def add_result(self, qid, qname, uid, totalc, totalp, diff):
        try:
            date = datetime.now().strftime('%H:%M:%S %d/%m/%Y')
            query = "INSERT INTO results(userId, quizId, quizName, totalCorrect, totalPercentage, difficulty, date) VALUES (?,?,?,?,?,?,?)"
            data = (int(uid), int(qid), str(qname), int(
                totalc), float(totalp), str(diff), str(date))
            self.cursor.execute(query, data)
            self.connection.commit()
        except Exception as e:
            print("Error with db, cannot insert result")
            print(e)

    def get_password(self, username):
        try:
            query = "SELECT password FROM users WHERE username='{}'".format(
                username)
            self.cursor.execute(query)
            data = self.cursor.fetchone()
            return data[0]

        except Exception:
            print("User Doesn't Exist")

    def get_userData(self, username):
        try:
            query = "SELECT * FROM users WHERE username='{}'".format(
                username)
            self.cursor.execute(query)
            data = self.cursor.fetchone()
            userData = {'id': data[0], 'username': data[1], 'fname': data[3],
                        'lname': data[4], 'age': data[5], 'year': data[6]}
            return userData
        except Exception:
            print("User Doesn't Exist")

    def get_quiz(self, id):
        try:
            query = "SELECT * FROM quizlist WHERE id='{}'".format(id)
            self.cursor.execute(query)
            data = self.cursor.fetchone()
            return data
        except Exception:
            print("Error, cannot get quiz")

    def get_questions(self, quizId):
        try:
            questions = []
            query = "SELECT * FROM questions WHERE quizId='{}'".format(
                quizId)
            for question in self.cursor.execute(query):
                questions.append(question)
            return questions
        except Exception:
            print("Errors")

    def get_quizList(self):
        quizList = []
        try:
            query = "SELECT * FROM quizList"
            for row in self.cursor.execute(query):
                quizList.append(row)
        except Exception:
            print("Cannot get quiz list")
        return quizList

    def get_results(self, userId):
        try:
            query = "SELECT * FROM results WHERE userId={} ORDER BY totalPercentage DESC".format(
                userId)
            results = []
            for row in self.cursor.execute(query):
                results.append(row)
            return results
        except Exception:
            print("Error with db, cannot get results for specified user")

    def check_userexists(self, username):
        try:
            query = "SELECT * FROM users WHERE username='{}'".format(
                username)
            self.cursor.execute(query)
            data = self.cursor.fetchone()
            if data == None:
                return False
            else:
                return True
        except Exception:
            print("Error running query")

db = Database()

def get_database():
    return db
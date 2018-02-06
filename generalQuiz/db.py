#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generalQuiz/db.py
# by William Neild

import sqlite3
from os import path

class Database:
    def setup():
        if path.exists('main.db'):
            return True
        else:
            conn = sqlite3.connect('main.db')
            c = conn.cursor()
            c.execute('''CREATE TABLE users (
                id INTEGER PRIMARY KEY,
                username TEXT,
                password TEXT,
                firstName TEXT,
                lastName TEXT,
                age INTEGER,
                year TEXT
            );''')
            c.execute('''CREATE TABLE quizlist (
                id INTEGER PRIMARY KEY,
                name TEXT
            );''')
            c.execute('''CREATE TABLE questions (
                id INTEGER PRIMARY KEY,
                quizId INTEGER,
                question TEXT,
                correctAns TEXT,
                otherAns TEXT
            )''')
            c.execute('''CREATE TABLE results (
                id INTEGER PRIMARY KEY,
                userId INTEGER,
                quizId INTEGER,
                quizName TEXT,
                totalCorrect INTEGER,
                totalPercentage TEXT
            )''')
            conn.commit()
            conn.close()


class Add:
    def user(username, password, fname, lname, age, year):
        try:
            conn = sqlite3.connect('main.db')
            c = conn.cursor()
            query = "INSERT INTO users(username, password, firstName, lastName, age, year) VALUES (?,?,?,?,?,?)"
            data = (str(username), str(password), str(fname), str(lname), int(age), str(year))
            c.execute(query, data)
            conn.commit()
            conn.close()
        except Exception:
            print("Error with db, cannot import data")

    def question(quizId, question, correctAns, otherAns):
        try:
            conn = sqlite3.connect('main.db')
            c = conn.cursor()
            query = "INSERT INTO questions(quizId, question, correctAns, otherAns) VALUES (?,?,?,?)"
            data = (int(quizId), str(question), str(correctAns), str(otherAns))
            c.execute(query, data)
            conn.commit()
            conn.close()
        except Exception:
            print("Error with db, couldnt add question")


    def quiz(name):
        try:
            conn = sqlite3.connect('main.db')
            c = conn.cursor()
            query = "INSERT INTO quizlist(name) VALUES (?)"
            data = (str(name),)
            c.execute(query, data)
            conn.commit()
            conn.close()
        except Exception as e:
            print("Error with db, cannot create quiz" + str(e))

    def result(qid, qname, uid, totalc, totalp):
        try:
            conn = sqlite3.connect('main.db')
            c = conn.cursor()
            query = "INSERT INTO results(userId, quizId, quizName, totalCorrect, totalPercentage) VALUES (?,?,?,?,?)"
            data = (int(uid), int(qid), str(qname), int(totalc), str(totalp))
            c.execute(query, data)
            conn.commit()
            conn.close()
        except Exception as e:
            print("Error with db, cannot insert result")
            print(e)

class Get:
    def password(username):
        try:
            conn = sqlite3.connect('main.db')
            c = conn.cursor()
            query = "SELECT password FROM users WHERE username='{}'".format(username)
            c.execute(query)
            data = c.fetchone()
            conn.close()
            return data[0]
        except Exception:
            print("User Doesn't Exist")

    def userData(username):
        try:
            conn = sqlite3.connect('main.db')
            c = conn.cursor()
            query = "SELECT * FROM users WHERE username='{}'".format(username)
            c.execute(query)
            data = c.fetchone()
            conn.close()
            userData = {'id':data[0], 'username':data[1], 'fname':data[3], 'lname':data[4], 'age':data[5], 'year':data[6]}
            return userData
        except Exception:
            print("User Doesn't Exist")

    def quiz(id):
        try:
            conn = sqlite3.connect('main.db')
            c = conn.cursor()
            query = "SELECT * FROM quizlist WHERE id='{}'".format(id)
            c.execute(query)
            data = c.fetchone()
            conn.close()
            return data
        except Exception:
            print("Error, cannot get quiz")

    def questions(quizId):
        try:
            conn = sqlite3.connect('main.db')
            c = conn.cursor()
            questions = []
            query = "SELECT * FROM questions WHERE quizId='{}'".format(quizId)
            for question in c.execute(query):
                questions.append(question)
            conn.close()
            return questions
        except Exception:
            print("Errors")

    def quizList():
        quizList = []
        try:
            conn = sqlite3.connect('main.db')
            c = conn.cursor()
            query = "SELECT * FROM quizList"
            for row in c.execute(query):
                quizList.append(row)
            conn.close()
        except Exception:
            print("Cannot get quiz list")
        return quizList

    def results(userId):
        try:
            conn = sqlite3.connect('main.db')
            c = conn.cursor()
            query = "SELECT * FROM results WHERE userId={}".format(userId)
            results = []
            for row in c.execute(query):
                results.append(row)
            conn.close()
            return results
        except Exception:
            print("Error with db, cannot get results for specified user")

class Check:
    def userexists(username):
        try:
            conn = sqlite3.connect('main.db')
            c = conn.cursor()
            query = "SELECT * FROM users WHERE username='{}'".format(username)
            c.execute(query)
            data = c.fetchone()
            conn.close()
            if data == None:
                return False
            else:
                return True
        except Exception:
            print("Error running query")

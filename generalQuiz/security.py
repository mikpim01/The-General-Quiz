#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generalQuiz/security.py
# by William Neild

import hashlib
import uuid
from generalQuiz import db, menu, config
from generalQuiz.helper import cprint


class Account:
    def validateReg(fname, lname, password, confpassword, age, year):
        errors = []
        # Firstname Checks
        if (len(fname) > 3) != True:
            errors.append("First Name too short")

        if any(char.isdigit() for char in fname):
            errors.append("Your first name shouldn't contain Numbers")

        # Lastname checks
        if any(char.isdigit() for char in lname):
            errors.append("Your Last name shouldn't contain Numbers")

        # To-Be username checks
        username = fname[:3] + str(age)
        if db.Check.userexists(str(username)):
            errors.append("User already exists")

        # Password Checks
        if (len(password) > 6) != True:
            errors.append("Password too short")

        if (len(confpassword) > 6) != True:
            errors.append("Password confirm too short")

        if password != confpassword:
            errors.append("Passwords don't match")

        if (len(password) < 100) != True:
            errors.append("Password too long")

        # Age checks
        if isinstance(age, int) != True:
            try:
                age = int(age)
            except Exception:
                errors.append("Age should be an integer")

        return errors


    def register(username, password, fname, lname, age, year):
        hashedPassword = Hash.psk(password)
        db.Add.user(username, hashedPassword, fname, lname, age, year)


    def login(username, password):
        hashedPassword = str(db.Get.password(username))
        if Hash.pskCheck(hashedPassword, password):
            userData = db.Get.userData(username)
            return userData
        else:
            return False


class Hash:
    def psk(password):
        salt = config.Get.salt()
        return hashlib.sha512(salt.encode() + password.encode()).hexdigest()


    def pskCheck(hashedPassword, password):
        salt = config.Get.salt()
        return hashedPassword == hashlib.sha512(salt.encode() + password.encode()).hexdigest()

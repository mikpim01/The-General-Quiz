#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generalQuiz/config.py
# by William Neild
import configparser
from sys import modules
from os import path
from uuid import uuid4

class Create:
    def __init__(self):
        if path.exists('config.ini') != True:
            # if the config file doesnt exists, generate a new one
            # with a random salt
            config = configparser.ConfigParser()
            config['Security'] = {"salt":uuid4().hex}
            with open('config.ini', 'w') as cfg:
                config.write(cfg)

class Get:
    def salt():
        config = configparser.ConfigParser()
        config.read('config.ini')
        return str(config.get("Security", "salt"))

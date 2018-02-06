#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generalQuiz/helper.py
# by William Neild

from shutil import get_terminal_size
from time import sleep
from sys import modules

def color():
    textStyles = None
    if "idlelib" in modules:
        textStyles = {
                        'reset':'',
                        'clrScreen':'',
                        'bright':'',
                        'white':'',
                        'lightgreen':'',
                        'lightcyan':'',
                        'lightred':''
                      }
    else:
        from colorama import init, Fore, Back, Style
        init(autoreset=True)
        textStyles = {
                        'reset':Fore.RESET,
                        'clrScreen':'\033[2J',
                        'bright':Style.BRIGHT,
                        'white':Fore.WHITE,
                        'lightgreen':Fore.LIGHTGREEN_EX,
                        'lightcyan':Fore.LIGHTCYAN_EX,
                        'lightred':Fore.LIGHTRED_EX
                      }
    return textStyles

def cprint(string, txtc="bright"): # Center print function
    textStyles = color()
    width = int(get_terminal_size()[0])-1
    print(textStyles[txtc] + str(string).center(width, " ") + textStyles["reset"])
    # sleep(0.01)

def pline(char, txtc="lightcyan", extra=""): # Print line function
    textStyles = color()
    width = int(get_terminal_size()[0])-1
    print(textStyles[txtc] + str(char) * width + textStyles["reset"] + str(extra))
    # sleep(0.01)

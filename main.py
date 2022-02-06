#!/usr/bin/env python
# coding: utf8

"""
Codingame Python Code Shortener
Version - 1
Niikurasu :)
"""

import python_minifier
from colorama import Fore, Back, Style, init
init()

# print out 



# read code from text file
with open("code.txt") as file:
    lines = file.readlines()
SOURCE_CODE = "".join(i for i in lines)

# minify code
minified = python_minifier.minify(SOURCE_CODE)

# check code sizes
original_length = len(SOURCE_CODE)
minified_length = len(minified)


# use minified code if it's shorter
if minified_length < original_length:
    SOURCE_CODE = minified

# convert code to utf-16
try:
    t = bytes(SOURCE_CODE, 'utf8').decode('utf16')
except:
  index = SOURCE_CODE.index(')')
  SOURCE_CODE = SOURCE_CODE[:index] + ' ' + SOURCE_CODE[index:]
  t = bytes(SOURCE_CODE, 'utf8').decode('utf16')
u16_code = f"exec(bytes('{t}','u16')[2:])"
u16_length = len(u16_code)
# change code if it's shorter
if u16_length < len(SOURCE_CODE):
    SOURCE_CODE = u16_code

print(Fore.RED + Style.BRIGHT + "Starting length:" + Style.RESET_ALL, original_length)
print(Fore.RED + Style.BRIGHT + "Minified length:"+ Style.RESET_ALL, minified_length)
print(Fore.RED + Style.BRIGHT + "UTF-16 length:" + Style.RESET_ALL, u16_length)


# print result
print(Style.RESET_ALL + 'Shortest Code:\n')

print(SOURCE_CODE)

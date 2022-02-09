#!/usr/bin/env python

"""
    Name:       Codingame Python Code Shortener
    Version:    1.0
    Author:     Niikurasu :)
"""

import python_minifier
import click
from colorama import Fore, Style, init


# cli interface
@click.command()
@click.option('f', '--file', required=True, help='the file path of the Python script that gets shortened')


def main(f):
    # 
    print(Fore.GREEN + Style.BRIGHT + """
      /\_____/\\
     /  o   o  \\        CODINGAME  Python CODE SHORTENER
    ( ==  ^  == )       Version: 1.0
     )         (         Author: Niikurasu
    (           )
   ( (  )   (  ) )
  (__(__)___(__)__)
        """)
    
    # read code from text file
    with open(f) as codefile:
        lines = codefile.readlines()
    SOURCE_CODE = "".join(i for i in lines)

    # minify code
    minified = python_minifier.minify(SOURCE_CODE, remove_literal_statements=True, rename_globals=True)

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
    # print out different code lengths
    init()
    print(Fore.RED + Style.BRIGHT + "Starting length:" + Style.RESET_ALL, original_length)
    print(Fore.RED + Style.BRIGHT + "Minified length:"+ Style.RESET_ALL, minified_length)
    print(Fore.RED + Style.BRIGHT + "UTF-16 length:" + Style.RESET_ALL, u16_length)


    # print result
    print(Style.RESET_ALL + '\nShortest Code:')
    print(SOURCE_CODE)



if __name__ == '__main__':
    main()

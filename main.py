
"""
Codingame Python Code Shortener
Version - 1
Niikurasu :)

if you encounter errors try 'export PYTHONIOENCODING=utf8' in the shell
"""



import python_minifier
with open("code.txt") as file:
  lines = file.readlines()
SOURCE_CODE = "".join(i for i in lines)
original_length = len(SOURCE_CODE)
print("Starting length:", original_length)
minified = python_minifier.minify(SOURCE_CODE)
minified_length = len(minified)
print("Minified length:", minified_length)
# use minified code if it shortened it
if minified_length < original_length:
  SOURCE_CODE = minified
# convert code to utf-16 if it shortens it
print(SOURCE_CODE)
t = bytes(SOURCE_CODE, 'utf8').decode('utf16')
u16_code = f"exec(bytes('{t}','u16')[2:])"
u16_length = len(u16_code)
print("UTF-16 length:", u16_length)
if u16_length < len(SOURCE_CODE):
  SOURCE_CODE = u16_code
print('\n\n\n' + SOURCE_CODE)
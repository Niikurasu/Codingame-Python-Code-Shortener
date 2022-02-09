"""
This is just an example of how you can shorten your code
"""
string = input().lower().replace(" ", "")
x = ""
for i in string:
    if i not in x:x += i
print(" ".join(f"{i}:{string.count(i)}" for i in x))

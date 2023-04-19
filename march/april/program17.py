#Files Io Basics
"""
"r" - open file for reading
"w" - open file for writing
"x" - create if file not exsist
'a" - add more content to file
"t" - text more content to file
"b" - binary mode
"+" - read and write

"""
#f is a pointer
#open is a function
f = open("shivam.txt")
content = f.read()
print(content)

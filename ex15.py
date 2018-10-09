# Imports module argv from sys (library?)
from sys import argv
# assigns inputs from argv to variables
script, filename = argv
# opens the file the user told to
txt = open(filename)

print(f"Here's your file {filename}:")
# Uses the read function to read and then print the contents of the file
print(txt.read())

print("Type the filename again:")
file_again = input("🤖 ")

txt_again = open(file_again)

print(txt_again.read())
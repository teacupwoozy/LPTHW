# Imports the module/library argv from sys
from sys import argv
# Read the WYSS section for how to run this
# Tells the program to store the arguments into these variables, in order
script, first, second, third = argv

# Prints the variables in f strings
print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
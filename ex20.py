from sys import argv

script, input_file = argv
# Creates a function that will read whatever file/argument is passed indef print_all(f):
# Also "f" is the name for the file variable.
def print_all(f):
    print(f.read())
# Creates a function that will rewind whatever file/argument is passed in and sets 
# the start point to the line index set with seek()
def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    # Reads a line on the file and then places the "read head" to right after the \n
    print(line_count, f.readline())

current_file = open(input_file)

print("First let's print the whole line: \n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want to do that, hit CMND-C.")
print("If you do want to do that, hit RETURN.")

input("?")

print("Opening the file...")
# Where "w" is is the mode.In this case, w means write, which will erase the file with this name.
# There is also r: read, a: append, r+: reading and writing
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
# According to the intertubes, this is redundant bc we're writing thie file
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

# rewrites to the file
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
# closes the file
target.close()
from sys import argv

script, filename = argv

print(f"We're now going to look at the content of the file {filename} that you just overwrote! Funsies!")

target = open(filename, 'a')

new_line = input("Please enter a new line: ")

target.write(new_line)

print("And now we will close it")
target.close()
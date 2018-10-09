from sys import argv

script, filename = argv

print(f"We're now going to look at the content of the file {filename} that you just overwrote! Funsies!")

target = open(filename, 'r')
print(target.read())

print("And now we will close it")
target.close()
# the end= prevent a carriage return while awaiting user input.
print("How old are you?", end=' ')
# input stores the input from the user into the variable
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

# a different way to get an input from the user
hair = input("Is your hair long or short? ")
print(hair)
print(f"Your hair is {hair}.")

# How to collect an interger from a user
x = int(input("Type a number "))
print(x)
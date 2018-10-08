# Sets a variable and give it a value
types_of_people = 10
# assign the var x with a value that is a string formatted to also include another variable.
x = f"There are {types_of_people} types of people."

# Two variables set below
binary = "binary"
do_not = "don't"
# Sets a new variable string that references two other variables.
y = f"Those who know {binary} and those who {do_not}."

# prints two variables
print(x)
print(y)

# prints two strings that include references to variables.
print(f"I said: {x}")
print(f"I also said: '{y}'")

# Sets a boolean value? to false
hilarious = False
# Sets a variable tha includes an empty reference of some kind
joke_evaluation = "Isn't that joke so funny?! {}"

# Prints a variable and includes format reference to another variable (boolean?)
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

# concatinates two variable strings.
print(w + e)
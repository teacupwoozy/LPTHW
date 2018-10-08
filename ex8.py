formatter = "{} {} {} {}"

# Passes a function into the var formatter and fills the empty brackets w the value 
# of what's passed in via the function.
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
# passes into the format function the value of the var formatter, 
# which contains a string of 4 empty brackets, or maybe it's an array??
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
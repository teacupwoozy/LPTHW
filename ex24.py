print("Let's practice everything.")
# Use escapes oncharacters that would otherwise confuse the code that's running.
print('You\'d need to know \'bout escapes with \\ that do:')
print('\n newlines and \t tabs.')

# Inserts a tab with escape: \t
# The triple quotes 
poem = """
\tThe lovely world
with logic so firmly planted
cannot dicscern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\twhere there is none.
"""

print("-------------")
print(poem)
print("-------------")


five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
# Creates these three new variables and populates them with the resuts of the three variables in secret_formula
beans, jars, crates = secret_formula(start_point)

# Remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# It's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point)
# This is an easy way to apply a list to a format string
# IDK what the asterik is doing
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))
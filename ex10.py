# \t inserts a tab when the variable is printed
tabby_cat = "\tI'm tabbed in."
# \n inserts a line return when a var is printed
persian_cat = "I'm split\non a line."
# \\ inserts a slash when string is printed
backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

tom_cat = "hallo\"hallo"
print(tom_cat)
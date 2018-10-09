# Names the arguments that will be used in the function
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # When the function is called these things print
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("That's enough for a party!")
    print("Get a blanket.\n")

# Call the fuction, passing in numbers
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

# defines and sets a value to two new variables
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50
# Uses those two new variables as arguments in the function
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# obvs
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 +6)

# Obvs
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
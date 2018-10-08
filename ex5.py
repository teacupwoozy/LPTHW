name = 'Stacy Em'
age = 104 # not a lie
height = 99 # inches
weight = 407 # lbs
eyes = 'Purple'
teeth = 'White'
hair = 'Brown'
height_in_cm = height *  2.54
weight_in_kg = weight * 0.45359237

print(f"Let's talk about {name}.")
print(f"She's {height} inches tall.")
print(f"She's {weight} pounds heavy.")
print("Actually, that's not too heavy")
print(f"She's got {eyes} eyes and {hair} hair.")
print(f"Her teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")

# convert to metric
print(f"She is {height_in_cm} cm tall.")
print(f"She is {weight_in_kg} kilos.")

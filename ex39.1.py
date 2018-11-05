# Study drill - stuff I can do with dictionaries

regional_food = {
    "Oaxaca": "mole",
    "Veracruz": "mole",
    "Queretaro": "sopes",
    "Chiapas": "quesadilla",
    "DF": "kekas",
    "Baja": "pescado"
}

regional_drinks = {
    "Oaxaca": "mezcal",
    "Veracruz": "cerveza",
    "Queretaro": "vino tinto",
    "Chiapas": "pox",
    "DF": "tequilla",
    "Baja": "vino blanco"
}

print(regional_food)
print(regional_drinks)

print(regional_food["Oaxaca"])
print(regional_food["DF"])

print(regional_drinks["DF"])

# Print dictionary keys, values, key-value pairs
print(regional_drinks.keys())
print(regional_drinks.values())
print(regional_drinks.items())

# Loop through dictionary
print('-' * 10)
for place, drink in list(regional_drinks.items()):
    print(f"La gente drink {drink} in {place} todos los días.")
    print(f"{place} is running out of {drink}.")
print('-' * 10)

# Add another key-value pair to dictionary
print('-' * 10)
regional_food.update({"Guanajuato": "gorditas"})
print(regional_food)
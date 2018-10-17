# Try to write a function that calls the while loop
numbers = []

def add_on(number, increment):
    i = 0

    while i < number:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + increment
        print("Numbers now:", numbers)
        print(f"At the bottom i is {i}")

numero = int(input("Enter a number: "))
inc = int(input("What value would you like to increment by? "))
add_on(numero, inc)


print("The numbers: ")

for num in numbers:
    print(num)


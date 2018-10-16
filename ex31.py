# My attempt to make my first python function, without yet know how. What's the worst that could happen!
def eat_cake():
    print("The bear uses her snoot to nudge your hand holding the knife. Then, with adorbale eyes, she looks towards the cake.")
    print("You realize she's a bear and isn't able to cut a slice of cake. So you cut one slice and hold it out to her.")
    print("With surprisingly good manners, the bear carefully eats the slice of cake from your hand.")
    print("When she has finished she licks your cheek in gratitude and motions for you to cut yourself a slice.")
    print("After you've eaten your slice, you and the bear go outside and take a nap under the tree in the yard.")


print("""You enter a dark room wih two doors.
Do you go through door #1 or door #2?""")

door = input("> ")

if door == "1":
    print("There's a giant bear here standing next to a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")
    print("3. See a knife and pick it up.")


    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    elif bear == "3":
        print("Take a couple steps toward the bear. The bear stands up on her haunches and sniffs the air.")
        print("What do you do next?")
        print("1. Reach out both hands - including the one with the knife - and walk towards the bear.")
        print("2. Back away from the bear, towards the door.")

        direction = input("> ")

        if direction == "1":
            eat_cake()

        else:
            print("The bear roars mightily. This makes you freeze in your place.")
            print("The bear slowly walks towards you.")
            eat_cake()

    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")

elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling mellodies.")
    print("4. There is nothing good behind this door. It's best to walk back out and go into the other door.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by the mind of jello.")
        print("Good job!")
    elif insanity == "4":
        print("Good job! Go hang with the friendly bear.")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")

else:
    print("You stumble around and fall on a knife and die. Good job!")
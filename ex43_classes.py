from sys import exit
from random import randint
from textwrap import dedent


class Scene(object):

    def enter(self):
        print("Need to add lots more stuff here.")
        exit(1)


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene("pau")

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
        
        # current_scene.enter()

    
class Death(Scene):

    death_types = [
        "You are smothered to death by the floof of a million kittens.",
        "You die from the adorableness of all the puppy boops.",
        "You die from a dry throat after telling all the world's Very Good Dogs what Good Doggos they are.",
        "You die from the indifference of an indifferent cat."
    ]

    def enter(self):
        # print(f"So sad, you're dead via: {self.death}")
        print(Death.death_types[randint(0, len(self.death_types)-1)])
        exit(1)
    

class CentralCorridor(Scene):

    def enter(self):
        print(dedent("""
            The Gothons of Planet Percal #25 have invaded your ship and
            dog-napped your entire crew of adorable puppies.  You are their
            only hope.  Your mission is to get the wicker basket from the 
            Weapons Armory.  (Everyone knows that adorable puppies cannot
            resist a floofy wicker basket.)  Then, take the wicker basket
            to the bridge, and summons the puppies where you will all
            get into the escape pod.
  
            You're running down the central corridor to the Weapons
            Armory when a Gothon jumps out, red scaly skin, dark grimy
            teeth, and clown costume flowing around his hate
            filled body.  He's blocking the door to the Armory and
            about to pull a super soaker to blast you.
        """))

        action = input("> ")

        if action == "boop his clown nose!":
            print(dedent("""
                He is a mean, cold one and completely unaffected by boops.
                Gothon waves off your boop, completely unimpressed, and 
                in an instant you know you are doomed.
            """))
            return 'death'

        elif action == "dodge!":
            print(dedent("""
                Whoa, um, yeah. That seemed like such a good idea. But, alas,
                your shoelaces were untied and you trip on them. You are 
                doomed.
            """))
            return 'death'
        
        elif action == "tell a joke!":
            print(dedent("""
                You are the Mistress of Puns, so you got this. You ask Gothon,
                'What kind of dog does Dracula have?' He stares unknowingly so 
                you answer 'A bloodhound!' and Gothon starts laughing uncontrollably.
                While he's laughing, you hand him a handful of trailmix and he 
                begins to eat it. Turns out, he was just hangry, so he lets you
                pass while he continues eating his snack. You jump through the
                Armory door.
                """))
            return 'laser_weapon_armory'

        else:
            print("Does not compute!")
            return 'central_corridor'


class LaserWeaponArmory(Scene):

    def enter(self):
        print(dedent("""
            You do an overly dramatic, totally unnecessary but really fun, dive
            roll into the armory. You see the floofy basket, but it is in a 
            locked glass container with a keypad lock. If you get the code wrong 10 
            times then the lock closes forever and you can't get the basket of
            floof. The code is three digits.
        """))

        code = f"{randint(1,9) } {randint(1,9)} {randint(1,9)}"
        # test code generator below. Code will always be 1
        # code = f"{randint(1,1) }"
        guess = input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print("NOPE!") 
            guesses += 1
            guess = input("[keypad> ")

        if guess == code:
            print(dedent("""
                Woot woot! You're the Mistress of Code-Cracking! You grab the basket
                and run as fast as you can back to the Bridge where you place the
                floof basket in just the right spot.
            """))
            return 'the_bridge'
        
        else:
            print(dedent("""
                The lock gives you the NOPE message one last time. Gulp.
                You await your fate from the other hangry Gothons.
            """))
            return 'death'
            

class TheBridge(Scene):

    def enter(self):
        print(dedent("""
            You bust onto the Bridge with the floof basket under your arm. There
            are at least 12 hangry Gothons who are trying to take control of the ship.
            They haven't drawn their super soakers yet, as they see you have a floof
            basket under your arm and they don't want to draw attention to it because 
            then the adorable puppies will notice it too. 
        """))

        action = input("> ")

        if action == "throw the floof basket":
            print(dedent("""
                In a panic, you throw the floof basket to the floor where the hangriest
                Gothon picks it up and eats it. 
            """))
            return 'death'

        elif action == "gently place the floof basket":
            print(dedent("""
                You gently place the floof basket on the floor. Since all puppies can
                hear the gentle placement of a floof basket onto the floor from 2,000 kms
                away, the adorable puppies all break free from their captors and come running.
                They pile into the floof basket. You carefully pick up the floof basket 
                that is practically overflowing with adorable puppies. You slowly back
                out the door, throw an entire bag of trail mix towards the hangry Gothons 
                and then close the door behind you. Now you can run to the escape pod.
            """))
            return 'escape_pod'

        else:
            print("Does not compute!")


class EscapePod(Scene):

    def enter(self):
        print(dedent("""
            You rush through the ship desparate to reach the escape pod before the
            Gothons finish their bag of trail mix. You get to the champer with the
            escape pods. There are five of them, but any of them might be damaged.
            Which one do you take?
        """))

        good_pod = randint(1,5)
        # For testing. Delete when program finished.
        # good_pod = randint(1,1)
        guess = input("[pod #]> ")

        if int(guess) != good_pod:
            print(dedent(f"""
                You jump into pod {guess} with your floof basket of adorable puppies 
                and hit the eject button. The outer door opens, but your don't eject. Uh oh.
            """))
            return 'death'

        else:
            print(dedent(f"""
                You jump into pod {guess} with your floof basket of adorable puppies 
                and hit the eject button. The outer door opens and you blast out into space.
                You and the basket of adorable puppies will soon be home where you can also
                play with your gaggle of baby goats. You win life!
            """))
            return 'finished'


class Finished(Scene):

    def enter(self):
        print("You Won! You and the adorable puppies are the best!")


class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene
    
    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
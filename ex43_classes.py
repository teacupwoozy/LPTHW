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

    # def __init__(self, death):
    #     self.death = death

    death_types = [
        "You are smothered to death by the floof of a million kittens.",
        "You die from the adorableness of all the puupy boops.",
        "You die from a dry throat after telling all the world's Very Good Dogs what Good Doggos they are."
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
        pass

class TheBridge(Scene):

    def enter(self):
        pass

class EscapePod(Scene):

    def enter(self):
        pass


class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        # 'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene
    
    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

# Ways to die
# death_by_kittens = Death("You are smothered to death by the floof of a million kittens.")
# death_by_puppies = Death("You die from the adorableness of all the boops.")
# # death_by_kittens.enter()
# death_by_puppies.enter()


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()




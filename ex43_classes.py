from sys import exit
from random import randint
from textwrap import dedent


class Scene(object):

    def enter(self):
        print("Need to add lots more stuff here.")
        exit


class Engine(object):

    def __init__(self, scene_map):
        pass

    def play(self):
        print("Need to play a game here.")
        exit
    
class Death(Scene):

    def __init__(self, death):
        self.death = death

    def enter(self):
        print(f"So sad, you're dead via: {self.death}")
        exit

class CentralCorridor(Scene):

    def enter(self):
        pass

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

    def __init__(self, start_scene):
        pass
    
    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass

# Ways to die
death_by_kittens = Death("You are smothered to death by the floof of a million kittens.")
death_by_puppies = Death("You die from the adorableness of all the boops.")

# a_map = Map('central_corridor')
# a_game = Engine(a_map)
# a_game.play()



death_by_kittens.enter()
death_by_puppies.enter()

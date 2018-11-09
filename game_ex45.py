from sys import exit

class Scene(object):

    def enter(self):
        pass


class Engine(object):

    def __init__(self, scene_map):
        pass
    
    def play(self):
        pass


class RacistsRoom(Scene):

    def enter(self):
        pass


class KittensPuppies(Scene):

    def enter(self):
        pass


class MisogynistMeeting(Scene):

    def enter(self):
        pass


class CollaborationCenter(Scene):

    def enter(self):
        pass


class WashingtonDC(Scene):

    def enter(self):
        pass


class NationalParks(Scene):

    def enter(self):
        pass


class Recharge(Scene):

    def enter(self):
        pass


class ConvertEvilOnes(Scene):

    def enter(self):
        pass

    def read_book(self):
        pass

    def personal_connection(self):
        pass


class BeAnAlly(Scene):

    def enter(self):
        pass


class EmpathyMagicSpell(Scene):

    def enter(self):
        pass

class SetBack(Scene):

    def enter(self):
        pass
    
    def defeat(self):
        pass
    
    def reassess(self):
        pass
    
    def evil_ones_elected(self):
        pass
    
    def natural_resources_selloff(self):
        pass

class AlliesElected(Scene):

    def enter(self):
        pass


class YouWin(Scene):
    
    def enter(self):
        print("You won! We have defeated evil!")


class Map(object):
    scenes = {
        "racists_room": RacistsRoom(),
        "kittens_puppies": KittensPuppies(),
        "mysogynist_meeting": MisogynistMeeting(),
        "collaboration_center": CollaborationCenter(),
        "washington_dc": WashingtonDC(),
        "national_parks": NationalParks(),
        "recharge": Recharge(),
        "convert_evil_ones": ConvertEvilOnes(),
        "be_an_ally": BeAnAlly(),
        "empathy_magic_spell": EmpathyMagicSpell(),
        "setback": SetBack(),
        "allies_elected": AlliesElected(),
        "you_win": YouWin(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val
    
    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('collaboration_center')
a_game = Engine(a_map)
a_game.play()

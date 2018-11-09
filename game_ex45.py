from sys import exit

class Scene(object):

    def enter(self):
        pass


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map
    
    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene("pau")

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)



class RacistsRoom(Scene):

    def enter(self):
        pass


class KittensPuppies(Scene):

    def enter(self):
        pass


class MensRightsConference(Scene):

    def enter(self):
        pass


class CollaborationCenter(Scene):

    def enter(self):
        print("""
            You are living in the United States of America in the year 2018.
            The whole country is in shambles because a huge percentage of the
            population have been emboldened by a lying, self-serving, racist, 
            misogynist President. He feeds these people's fears with lies, 
            propaganda, and his relentless tirade of racist comments.

            As a level-headed, thinking, feeling human being, your mission is 
            to defeat these terrible inclinations of the Evil Ones and help 
            them to return to sense and abandon their hate-filled ways.

            By doing this, youl will save countless lives in the United States 
            and aroung the world. 

            You are currently in the Collaboration Center, surrounded by others
            who are also fighting the Evil Ones. Where do you want to go to 
            start your fight: Washington DC, an alt-right meeting, nearby 
            national park, or a men's rights conference?
        """)

        action = input("👩🏼‍🎤 >  ")

        if action == "Washington DC":
            print("DC")
        
        elif action == "alt-right":
            print("alt-right")

        elif action == "national park":
            print("national park")

        elif action == "conference":
            print("men's rights conference")

        else:
            print("That's not an option")
            return "collaboration_center"

    def repeat_entry(self):
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
        "mens_rights_conference": MensRightsConference(),
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

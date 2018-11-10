from sys import exit
from random import randint

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
        
        # current_scene.enter()


class RacistsRoom(Scene):

    def enter(self):
        print("Hallo rr")


class KittensPuppies(Scene):

    def enter(self):
        pass


class MensRightsConference(Scene):

    def enter(self):
        print("Hallo men's rights")


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

        # Change this into a method - along with the one in WhereNext
        action = input("👩🏼‍🎤 >  ")

        if action == "Washington DC":
            print("DC")
            # return "washington_dc"
            return "washington_dc"
        
        elif action == "alt-right":
            print("alt-right")
            return "racists_room"

        elif action == "national park":
            print("national park")
            return "national_parks"

        elif action == "conference":
            print("men's rights conference")
            return "mens_rights_conference"

        else:
            print("That's not an option")
            return "collaboration_center"

    def repeat_entry(self):
        pass

class WashingtonDC(Scene):

    def enter(self):
        print("""
            The President has demanded Congress pass legislation that will
            deport all citizens and residents who were not born in the United
            States and have less than $1 million in assets.

            Congress has rolled over to this terrible President and no longer
            serves as a separate branch of the government. So this request, 
            like all the others, they will do.

            The People of the United States are enraged about this, and have 
            been showing up to the capital for the past couple of days. You
            have also just arrived.

            What is the first thing you do:
                A. Check out the newest restaurants
                B. Attend an organizing meeting
                C. Find a hotel
                D. Go for a walk
            """)
        
        guess = input("👩🏼‍🎤> ").upper()

        if guess == "A":
            print("lame-o")
            dilly_dally = SetBack()
            return dilly_dally.dilly_dally()
        
        elif guess == "B":
            print("""
                More than 1 million people invade the hallways of the Congressional 
                Offices and surrounding streets. The spineless Congresspeople 
                who had refused to stand up to the President are now more
                afraid of winning their next elections than they are of the 
                racist President.
            """)
            convert = ConvertEvilOnes()
            return convert.convert_politicians()
        
        elif guess == "C":
            print("There are 1 million people protesting in DC right now.")
            print("Everything is booked solid. Why don't you do something productive?")
            return "washington_dc"

        else:
            print("That is not an option")
            return "washington_dc"


    def street_meeting(self):



class NationalParks(Scene):

    def enter(self):
        print("""
            The Administration has been busy leasing off National Parklands
            to private industry. These businesses are clearcutting the forests,
            drilling for oil and national gas in fragile ecosystems, and
            they've diverted water which is destroying critical watersheds.
            National Park employees have been pleading with the public to help
            them to save these critical lands.

            People are decending on Parks across the country, blocking the
            roads and preventing drilling and logging equipment from getting
            in or out. 

            There are massive boycotts of these major companies. Gasoline
            consumption has been cut in half, purchases of home electronics
            have collapsed, and people have revived Victory Gardens which has
            resulted in grocery store sales dropping by more than 30%.

            You have been part of the successful road bloqueos that are now
            impacting the transport of food and goods all over the country.

            In the fifth week of these protests, some of the companies leasing
            lands have moved to cancel their leases. And, politicians in DC
            are quickly pushing new legislation through that will halt the 
            President's ability to lease these lands. They have the votes to
            override a veto.
        """)

        convert = ConvertEvilOnes()
        return convert.convert_politicians()
        


class Recharge(Scene):

    recharge_types = [
        "You see Alicia Garza give a completely amazing and inspirational talk",
        "Rewatch a video of Maya Angelou's reciting her poem 'On the Pulse of Morning. For the hundredth time.",
        "moar inspo",
        "moar moar inspo",
        "yet moar inspo, inspo"
    ]

    def enter(self):
        print("""
            Fighting against hate is hard work and it's draining. You've got
            to take care of yourself and others. So it's smart that you've 
            come to recharge. We'll have you recharged and back in fighting 
            form so soon! While in the Recharge Room you:
        """)
        print(Recharge.recharge_types[randint(0, len(self.recharge_types)-1)])
        # This is not working and I don't know why. Oof.
        return "where_next"

class ConvertEvilOnes(Scene):

    def enter(self):
        pass

    def read_book(self):
        pass

    def personal_connection(self):
        pass
    
    def convert_politicians(self):
        print("they find their spines")
        return "where_next"


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

    def dilly_dally(self):
        print("dilly dally")

class AlliesElected(Scene):

    def enter(self):
        pass


class WhereNext(Scene):

    def where_to(self):
        print("""
            Now that you've finished with that. Where do you want to go to 
            next: Washington DC, an alt-right meeting, nearby national park, 
            or a men's rights conference?
        """)
        
        action = input("👩🏼‍🎤>  ")

        if action == "Washington DC":
            print("DC")
            return "washington_dc"
        
        elif action == "alt-right":
            print("alt-right")
            return "racists_room"

        elif action == "national park":
            print("national park")
            return "national_parks"

        elif action == "conference":
            print("men's rights conference")
            return "mens_rights_conference"

        else:
            print("That's not an option")
            return "where_next"


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
        "where_next": WhereNext(),
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
# test = Recharge()
# test.enter()
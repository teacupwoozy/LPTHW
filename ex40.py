class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                         "With pockets full of shells"])

bee_bop = Song(["Doo bee doo bee doo",
                "Boo bee boo bee boo",
                "Daa daa daa dee daa"])

# Pass in song as a variable
gwar = """rrrraaaaawwwwww.
gggrrrrraaaawwwww."""

gwar_song = Song([gwar])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

bee_bop.sing_me_a_song()

gwar_song.sing_me_a_song()
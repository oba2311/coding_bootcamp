class Song(object):
    """docstring."""

    def __init__(self, lyrics):
        """docstring."""
        self.lyrics = lyrics

    def sing_me_a_song(self):
        """docstring."""
        for line in self.lyrics:
            print(line)


happy_bday = Song(["happy birthday to you",
                   "I don't wanna get sued", "so let's stop"])

bulls_on_parade = Song(["They rally around the family",
                        "with pockets full of shells"])

happy_bday.sing_me_a_song()


bulls_on_parade.sing_me_a_song()

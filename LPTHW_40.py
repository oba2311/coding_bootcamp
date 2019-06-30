"""this is exercise num 40 from LPTHW."""


class Song(object):
    """docstring."""

    def __init__(self, lyrics):
        """docstring."""
        self.lyrics = lyrics

    def sing_me_a_song_and_add_one(self):
        """docstring."""
        for line in self.lyrics:
            print(line, "one")


the_bday_song = ["happy birthday to you",
                 "I don't wanna get sued", "so let's stop"]

happy_bday = Song(the_bday_song)

bulls_on_parade = Song(["They rally around the family",
                        "with pockets full of shells"])

happy_bday.sing_me_a_song_and_add_one()


bulls_on_parade.sing_me_a_song_and_add_one()

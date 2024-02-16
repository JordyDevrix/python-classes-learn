class String():

    def __init__(self, string):
        self.string = string

    def herzet(self, oud, nieuw):

        new_string = ""

        for character in self.string:
            if character == oud:
                new_string += nieuw
            else:
                new_string += character

        return new_string


from vehicle2_class import *

class Car2(Vehicle2):

    def __init__(self, wheels, capacity, color, make, model, plate):
        super().__init__(wheels, capacity, color)
        self.make = make
        self.model = model
        self.plate = plate

    def make_sound(self):
        return 'REVVING MY CAR! VROOM!'

    def play_music(self, song):
        return 'Banging song this is: ' + song
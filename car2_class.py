from vehicle2_class import *

class Car2(Vehicle2):

    def __init__(self, wheels, capacity, color, make, model, plate):
        super().__init__(wheels, capacity, color)
        self.make = make
        self.model = model
        self.plate = plate
        self._accidents = 0 # Visibility is limited
        self.__miles = 0 # Visibility and Access is restricted#

    def make_sound(self):
        return 'REVVING MY CAR! VROOM!'

    def accelerate(self): # Using encapsulated private method
        self.__increase_miles()
        return 'VROOOOMMMM'

    def play_music(self, song):
        return 'Banging song this is: ' + song

    def show_miles(self): # Getter
        return self.__miles

    def set_miles(self, miles): # Setter
        # Checking some crazy security stuff before setting
        self.__miles = miles
        return 'miles set to ' + miles

    def __increase_miles(self): # Encapsulated private method
        self.__miles += 100
from vehicle_class import *

class Bike(Vehicle):

    def __init__(self, capacity, color, year, gears, handle_type, basket, wheels_type, wheels_num = 2):
        super().__init__(wheels_num, capacity, color, year)
        self.gears = gears
        self.handle_type = handle_type
        self.basket = basket
        self.wheels_type = wheels_type

    def pedal(self):
        return 'LEFT RIGHT LEFT RIGHT!'

    def wheelie(self):
        return 'THEY SEE ME ROLLIN, THEY HATIN'

    def chain_it(self):
        return 'NOBODY IS GOING TO STEAL ME!'

    def flips(self):
        return '*FLIP*'
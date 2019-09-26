class Vehicle():

    # Characteristics
    def __init__(self, wheels_num, capacity, color, year):
        self.wheels_num = wheels_num
        self.capacity = capacity
        self.color = color
        self.year = year

    # Behaviours
    def accelerate(self, speed = ''):
        return "VROOM VROOM! " + speed

    def breake(self, breaking = ''):
        return "EEEEEK! " + breaking

    def turn(self, direction = ''):
        return 'SKRT SKRT!' + direction

    def make_sound(self, sound = ''):
        return '' + sound
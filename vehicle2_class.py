class Vehicle2():

    def __init__(self, wheels, capacity, color):
        self.wheels = wheels
        self.capacity = capacity
        self.color = color

    def accelerate(self):
        return 'VroooooOOoommmmm'

    def make_sound(self):
        return '##Making Noises##'

# print(Vehicle2(4, 5, 'Green').make_sound())
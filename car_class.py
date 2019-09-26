from vehicle_class import *

class Car(Vehicle):

    def __init__(self, capacity, color, year, brand, model, license_plate, airbag, wheels_num = 4):
        super().__init__(wheels_num, capacity, color, year)
        self.brand = brand
        self.model = model
        self.license_plate = license_plate
        self.airbag = airbag

    def play_music(self, song = ''):
        return song + ' DROP THE BASS *BOOM*'

    def horn(self, horn_reaction = ''):
        return 'BEEP BEEP!' + horn_reaction

    def lock(self, locking = ''):
        return 'CAR LOCKED *TICK*' + locking

    def air_condition(self, intensity = ''):
        return 'NICE AND COOL' + intensity

    def auto_pilot(self, active = ''):
        return 'I/M AND INDEPENDENT CAR' + active
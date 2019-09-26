from car2_class import *



print('Proof of Inheritance')
print(Car2(2, 4, 'Blue')) # Inheriting the __init__
print(Car2(2, 4, 'Blue').accelerate()) # Inheriting the .acclerate()

print('Proof of method polymorphismm with make_sound')
print(Vehicle2(2, 4, 'Blue').make_sound())
print(Car2(2, 4, 'Blue').make_sound())
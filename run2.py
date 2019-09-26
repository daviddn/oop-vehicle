from car2_class import *

# print('Creating a simple instance - hence I know how to write a Class and')
# vehicle_example = Vehicle2(2, 3, 'green')
#
# print('Proof of Inheritance')
# # Car inherits from Vehicle2
car_example = Car2(2, 4, 'Blue', 'Volvo', 'XC90', 'XOXOX')
# print(car_example) # Inheriting the __init__
# print(car_example.accelerate()) # Inheriting the .acclerate()
#
# print('Proof of method polymorphism with make_sound')
# print(vehicle_example.make_sound())
# print(car_example.make_sound())

print('Playing with encapsulation')
print(car_example.wheels)
car_example._accidents = 100
print(car_example._accidents)

# print(car_example.__miles()) # This will break - Because it's a private/encapsulation
print(car_example.show_miles())

# print(car_example.__increase_miles()) # This will break - Method encapsulation
print(car_example.accelerate())
print(car_example.show_miles())
class Car:
    def move(self):
        print("Car is driving.")


class Person:
    def move(self):
        print("Person is walking.")


class Robot:
    def move(self):
        print("Robot is moving.")


def make_it_move(thing):
    thing.move()


things = [Car(), Person(), Robot()]

for thing in things:
    make_it_move(thing)
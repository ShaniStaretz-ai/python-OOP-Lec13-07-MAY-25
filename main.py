import car
print(car.Car.speed)
from car import *
print(Car.speed)
from car import Car
print(Car.color)
from car import Car as Ca
print(Ca.type)
print(Car.__dict__)

from movie import  Movie
print(Movie.actor.name)

class Tv:
    pass
samsung=Tv()
lg=Tv()




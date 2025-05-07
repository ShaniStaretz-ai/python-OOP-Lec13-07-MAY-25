#Static class= object class
class Car:
    type='Toyota'
    model='RAV-4'
    color='Black'
    speed=180

if __name__ == '__main__':
    print(Car.type)
    print(Car.__dict__)
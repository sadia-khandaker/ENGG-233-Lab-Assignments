import random
import math 

class Point:
    def __init__(self):
        self.X = float()
        self.Y = float()
        self.Z = float()

def fill_point(point):
    point.X = random.randint(1,101)
    point.Y = random.randint(1,101)
    point.Z = random.randint(1,101)
    
def distance_between_points(p1, p2):
    return (((p1.X-p2.X)**2)+((p1.Y-p2.Y)**2)+((p1.Z-p2.Z)**2))**(0.5)


    
def main():

    p1 = Point()
    p2 = Point()

    fill_point(p1)
    fill_point(p2)


    print('P1: (', p1.X, ',', p1.Y, ',', p1.Z, ')')
    print('P2: (', p2.X, ',', p2.Y, ',', p2.Z, ')')


    print('Distance: ',distance_between_points(p1, p2))


if __name__ == '__main__':
    main()
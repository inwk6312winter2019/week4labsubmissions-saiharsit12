#TASK1

import math
class point():
    """"Represents a point in 2-D space."""

def distance_between_points(p1,p2):
    """Computes the distance between two Point objects.

    p1: Point
    p2: Point

    returns: float
    """
    return math.sqrt((p2.x-p1.x)**2+(p2.y-p1.y)**2)

def main():
    point1 = point()
    point2 = point()
    point1.x = 5
    point1.y = 10
    point2.x = 10
    point2.y = 15
    print(distance_between_points(point1, point2))

if __name__ == '__main__':
    main()

_____________________________________________________________

#TASK2

import turtle
import copy
from sample1 import point
turtle.pen(fillcolor="black", pencolor="red", pensize=10)

class rectangle():
    """Represents a rectangle.
       attributes: width, height, corner.
    """
def find_center(r):
    """Find the center of a rectangle

        r: Rectangle object.
        
        returns: center coordinates
    """
    cx=r.corner.x+(r.width/2)
    cy=r.corner.y+(r.height/2)
    return cx,cy

def move_rectangle(r,dx,dy):
    """Move the Rectangle by modifying its corner object.

        r: Rectangle object.
        dx: change in x coordinate (can be negative).
        dy: change in y coordinate (can be negative).

        returns:rectangle object
        """

    r.corner.x=r.corner.x+dx
    r.corner.y=r.corner.y+dy
    turtle.setx(r.corner.x)
    turtle.sety(r.corner.y)
    for i in range(2):
        turtle.fd(r.width)
        turtle.lt(90)
        turtle.fd(r.height)
        turtle.lt(90)
    return r

def move_rectangle1(r,dx,dy):
    """Move the Rectangle and return a new Rectangle object.

        r: Rectangle object.
        dx: change in x coordinate (can be negative).
        dy: change in y coordinate (can be negative).

        returns: new Rectangle
        """
    new = copy.deepcopy(r)
    move_rectangle(new, dx, dy)

    return new


def main():
    r = rectangle()
    r.width = 100.0
    r.height = 200.0
    r.corner = point()
    r.corner.x=50.0
    r.corner.y=50.0
    print("Center coordinates of rectangle:", find_center(r))
    r1=move_rectangle(r, 10, 5)
    print("Existing Rectangle new position corner coordinates:",r1.corner.x,r1.corner.y )
    r2=move_rectangle1(r, 100, 150)
    print("New Rectangle corner coordinates:",r2.corner.x,r2.corner.y )
    turtle.mainloop()

if __name__ == "__main__":
    main()

_____________________________________________________________

#TASK3

import turtle

class rectangle():
    """Represents a rectangle.
           attributes: width, height.
        """


class circle():
    """Represents a circle.
           attributes: radius.
        """
    radius=50

def draw_rect(r):
    """ Draws a rectangle with given width and height using turtle"""
    for i in range(2):
        turtle.fd(r.width)
        turtle.lt(90)
        turtle.fd(r.height)
        turtle.lt(90)

def draw_circle(c):
    """Draws a circle with given radius using turtle"""
    turtle.circle(c.radius)

def main():
    r = rectangle()
    r.width=50
    r.height=200
    c = circle()
    c.radius=50
    print(draw_rect(r))
    turtle.reset()
    print(draw_circle(c))
    turtle.mainloop()

if __name__ == '__main__':
    main()

_____________________________________________________________

#TASK4

import turtle

class rectangle():
    """Represents a rectangle.
           attributes: width, height.
        """


class circle():
    """Represents a circle.
           attributes: radius.
        """
    radius=50

def draw_rect(r):
    """ Draws a rectangle with given width and height using turtle"""
    for i in range(2):
        turtle.fd(r.width)
        turtle.lt(90)
        turtle.fd(r.height)
        turtle.lt(90)

def draw_circle(c):
    """Draws a circle with given radius using turtle"""
    turtle.circle(c.radius)

def main():
    r = rectangle()
    r.width=50
    r.height=200
    c = circle()
    c.radius=50
    print(draw_rect(r))
    turtle.reset()
    print(draw_circle(c))
    turtle.mainloop()

if __name__ == '__main__':
    main()

_____________________________________________________________

#TASK5

class time:
    """Represents the time of day.
    attributes: hour, minute, second
    """
def print_time(t):
    """Print the time by calling the time object attributes """
    print("Time is %.2d:%.2d:%.2d"%(t.hour,t.minute,t.second))

def main():
    t=time()
    t.hour=12
    t.minute=5
    t.second=9
    print_time(t)

if __name__ == '__main__':
    main()

_____________________________________________________________

#TASK6

class time:
    """Represents the time of day.
    attributes: hour, minute, second
    """

def is_after(t1,t2):
    """Returns True if t1 is after t2; false otherwise."""
    return (t1.hour, t1.minute, t1.second) > (t2.hour, t2.minute, t2.second)

def main():
    t1=time()
    t1.hour=12
    t1.minute=5
    t1.second=9
    t2=time()
    t2.hour=11
    t2.minute=45
    t2.second=55
    print(is_after(t1,t2))

if __name__ == '__main__':
    main()

_____________________________________________________________

#TASK7

class time:
    """Represents the time of day.
    attributes: hour, minute, second
    """
def int_to_time(seconds):
    """Makes a new Time object.

    seconds: int seconds since midnight.
    """
    time1 = time()
    minutes, time1.second = divmod(seconds, 60)
    time1.hour, time1.minute = divmod(minutes, 60)
    return time1


def time_to_int(time):
    """Computes the number of seconds since midnight.

    time: Time object.
    """
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def valid_time(time):
    """Checks whether a Time object satisfies the invariants.

    time: Time

    returns: boolean
    """
    if time.hour < 0 or time.minute < 0 or time.second < 0:
        return False
    if time.minute >= 60 or time.second >= 60:
        return False
    return True


def increment(time, seconds):
    """Adds seconds to a Time object."""
    assert valid_time(time)
    seconds += time_to_int(time)
    return int_to_time(seconds)

def main():
    t=time()
    t.hour=11
    t.minute=5
    t.second=30
    time1=increment(t,150)
    print("Incremented time is : %.2d:%.2d:%.2d" %(time1.hour,time1.minute,time1.second))

if __name__ == '__main__':
    main()

_____________________________________________________________

#TASK8_1

import calendar
from datetime import date

def main():
    my_date = date.today()
    print("Today's date :",my_date)
    print("Current day of the week is :",calendar.day_name[my_date.weekday()])


if __name__ == '__main__':
    main()

_____________________________________________________________

#TASK8_2

from datetime import date
from datetime import datetime


class birthday:
    """This has a person birthday
        Attributes: year,month,date


    """
def age(birthday):
    """Age calculator

    Attributes: birthday YYYY-MM-DD

    returns: age in years
    """
    today = date.today()
    y = today.year - birthday.year
    if today.month < birthday.month or today.month == birthday.month and today.day < birthday.day:
        y -= 1
    return y

def bday_date_diff(birthday):
    """Calculates the tim euntil next birthday

        Attributes: birthday YYYY-MM-DD

        returns: age in years
        """
    today = date.today()
    now = datetime.now()
    t0=datetime(today.year,today.month,today.day,now.hour,now.minute,now.second)
    t1=datetime(today.year+1,birthday.month,birthday.day,00,00,00)
    t=t1-t0
    return t


def main():
    b=birthday()
    b.year=int(input("Enter the birth year YYYY:"))
    b.month =int(input("Enter the birth month MM:"))
    b.day = int(input("Enter the birth date DD:"))
    print("your current age is :",age(b))
    print("No of days until next birthday is:",bday_date_diff(b))

if __name__ == '__main__':
    main()
_____________________________________________________________

#TASK9

class time:
    """Represents the time of day.
    attributes: hour, minute, second
    """

    def time_to_int(self):
        """Computes the number of seconds since midnight.

        time: Time object.
        """
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

def int_to_time(seconds):
    """Makes a new Time object.

    seconds: int seconds since midnight.
    """
    time1 = time()
    minutes, time1.second = divmod(seconds, 60)
    time1.hour, time1.minute = divmod(minutes, 60)
    return time1

def valid_time(time):
    """Checks whether a Time object satisfies the invariants.

    time: Time

    returns: boolean
    """
    if time.hour < 0 or time.minute < 0 or time.second < 0:
        return False
    if time.minute >= 60 or time.second >= 60:
        return False
    return True

def increment(time, seconds):
    """Adds seconds to a Time object."""
    assert valid_time(time)
    seconds += time.time_to_int()
    return int_to_time(seconds)

def main():
    t=time()
    t.hour=11
    t.minute=5
    t.second=30
    time1=increment(t,150)
    print("Incremented time is : %.2d:%.2d:%.2d" %(time1.hour,time1.minute,time1.second))


if __name__ == '__main__':
    main()

_____________________________________________________________

#TASK10

class point():
    """"Represents a point in 2-D space.
        Prints X and Y coordinates
        Adds two points
        """
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def __str__(self):
        return "X:Y-%.2d:%.2d"%(self.x,self.y)
    def __add__(self,other):
        """Adds a point."""
        return point(self.x+other.x,self.y+other.y)

def main():
    p1=point(10)
    p2=point(10,20)
    print(p1)
    print(p2)
    print(p1+p2)

if __name__ == '__main__':
    main()

_____________________________________________________________

#TASK11

class point():
    """"Represents a point in 2-D space.
        Prints X and Y coordinates
        Adds two points
        """
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def __str__(self):
        return "X:Y-%.2d:%.2d"%(self.x,self.y)
    def __add__(self,other):
        """Adds a Point or tuple."""
        if isinstance(other, point):
            return self.add_points(other)
        else:
            return self.add_points_tuple(other)
    def add_points(self,other):
        """Adds a point."""
        return point(self.x+other.x,self.y+other.x)
    def add_points_tuple(self,other):
        """Adds a tuple."""
        return point(self.x+other[0],self.y+other[1])

def main():
    p1=point(10)
    p2=point(10,20)
    print(p1)
    print(p2)
    print(p1+p2)
    print(p1+(20,30))

if __name__ == '__main__':
    main()

_____________________________________________________________

#TASK12

class kangaroo:
    def __init__(self):
        self.pouch_contents=[]
    def put_in_pouch(self,other):
        if(isinstance(other,kangaroo)):
            self.pouch_contents.append(other.pouch_contents)
        else:
            self.pouch_contents.append(other)
    def __str__(self):
        return str(self.pouch_contents)

def main():
    kanga=kangaroo()
    roo=kangaroo()
    kanga.put_in_pouch("apple")
    kanga.put_in_pouch(1)
    roo.put_in_pouch("orange")
    kanga.put_in_pouch(roo)
    print(kanga)
    print(roo)

if __name__ == '__main__':
    main()

_____________________________________________________________

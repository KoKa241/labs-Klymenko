from math import hypot

class Point:
    def __init__(self, x=0, y=0) -> None:
        self._x = x
        self._y = y
    
    def getx(self):
        return self._x
    
    def gety(self):
        return self._y

    def distance_from_xy(self, x, y):
        return round(hypot(self._x - x, self._y - y), 2)
    
    def distance_from_point(self, point):
        return round(hypot(self._x - point._x, self._y - point._y), 2)


if __name__ == "__main__":

  point = Point(2, 5)
  point2 = Point(10, 3)
  distance = point.distance_from_xy(10, 3)
  distance_point = point.distance_from_point(point2)
  print(distance)
  print(distance_point)

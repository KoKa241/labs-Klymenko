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


class Triangle:
    def __init__(self, verticle1, verticle2, verticle3) -> None:
        self._verticle1 = verticle1
        self._verticle2 = verticle2
        self._verticle3 = verticle3
    
    def perimeter(self):
        side1 = self._verticle1.distance_from_point(self._verticle2)
        side2 = self._verticle2.distance_from_point(self._verticle3)
        side3 = self._verticle3.distance_from_point(self._verticle1)
        perimeter = side1 + side2 + side3
        return perimeter   


if __name__ == "__main__":

  point = Point(2, 5)
  point2 = Point(10, 3)
  distance = point.distance_from_xy(10, 3)
  distance_point = point.distance_from_point(point2)
  print(distance)
  print(distance_point)

  triangle = Triangle(point, point2, Point(5, 7))
  perimeter = triangle.perimeter()
  print(perimeter)
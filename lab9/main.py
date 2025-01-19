import math
class Body:
    def __init__(self):
        pass
    def surface_area(self):
        pass
    def volume(self):
        pass
    def myName(self):
        return type(self).__name__


class Parallelepiped(Body):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def surface_area(self):
        return 2 * (self.a * self.b + self.a * self.c + self.b * self.c)

    def volume(self):
        return self.a * self.b * self.c

    def __str__(self):
        return f"Parallelepiped: a={self.a}, b={self.b}, c={self.c}"

class Ball(Body):
    def __init__(self, radius):
        self.radius = radius

    def surface_area(self):
        return 4 * math.pi * self.radius**2

    def volume(self):
        return (4 / 3) * math.pi * self.radius**3

    def __str__(self):
        return f"Ball: radius={self.radius}"

class Series:
    def __init__(self, bod=[]):
        self.bodies = bod

    def add_body(self, body):
        self.bodies.append(body)

    def filter_volume(self, min_value, max_value):
        filtered_bodies = [body for body in self.bodies if min_value <= body.volume() <= max_value]
        self.print_bodies(filtered_bodies)
        self.save_file(filtered_bodies)

    def filter_surface(self, surface_area):
        filtered_bodies = [body for body in self.bodies if abs(surface_area - body.surface_area()) < 1e-6]
        self.print_bodies(filtered_bodies)
        self.save_file(filtered_bodies)

    def filter_class(self, class_name):
        filtered_bodies = [body for body in self.bodies if body.myName() == class_name]
        self.print_bodies(filtered_bodies)
        self.save_file(filtered_bodies)

    def print_bodies(self, bodies):
        if not bodies:
            print("nothing found")
        for body in bodies:
            print(f"Type: {body.myName()}, Surface area: {body.surface_area():.2f}, Volume: {body.volume():.2f}") 

    def load_file(self):
        try:
          with open("1.txt", 'r') as f:
              for line in f:
                  line = line.strip()
                  parts = line.split(',')
                  if parts[0] == 'Parallelepiped':
                      a, b, c = map(float, parts[1:])
                      self.add_body(Parallelepiped(a, b, c))
                  elif parts[0] == 'Ball':
                      radius = float(parts[1])
                      self.add_body(Ball(radius))
                  else:
                      print("couldn't add data")
        except FileNotFoundError:
          print("File 1.txt not found.")


    def save_file(self, filtered_bodies):
        with open('2.txt', 'w') as f:
            for body in filtered_bodies:
                f.write(str(body) + '\n')
            print("data added to file")

series = Series()
series.load_file()

print("1 - filter by volume")
print("2 - filter by surface area")
print("3 - filter by class name")
input1 = int(input())

if input1 == 1:
    print('filter by min and max value for volume')
    min = float(input('input min value - '))
    max = float(input('input max value - '))
    series.filter_volume(min, max)

elif input1 == 2:
    print("filter by surface")
    surface_area = float(input("input surface area - "))
    series.filter_surface(surface_area)

elif input1 == 3:
    print("filter by class")
    name = str(input("input class name - "))
    series.filter_class(name)

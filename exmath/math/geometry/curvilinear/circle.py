import math

class circle(object):

    def __init__(self, radius = None, diameter = None, perimeter = None, area = None):

        self.set_radius(radius)
        self.set_diameter(diameter)
        self.set_perimeter(perimeter)
        self.set_area(area)
    
    def get_radius(self):
        if self._radius or self._radius is None:
            return self._radius
        else:
            self.calculate_radius()
            return self._radius

    def set_radius(self, value):
        if isinstance(value, int) or isinstance(value, float) or value is None:
            self._radius = value
        else:
            raise TypeError("radius requires as type int, float or NoneType")

    radius = property(get_radius, set_radius)

    def calculate_radius(self):
        if self.diameter is not None:
            self._calculate_radius_by_diameter()
        elif self.perimeter is not None:
            self._calculate_radius_by_perimeter()
        elif self.area is not None:
            self._calculate_radius_by_area()
        else:
            raise Exception

        return

    def _calculate_radius_by_diameter(self):
        self.radius = self.diameter / 2
        return

    def _calculate_radius_by_perimeter(self):
        self.radius = self.perimeter / (2 * math.pi)
        return

    def _calculate_radius_by_area(self):
        self.radius = math.sqrt(self.area / math.pi)
        return

    def get_diameter(self):
        if self._diameter or self._diameter is None:
            return self._diameter
        else:
            self.calculate_diameter()
            return self._diameter

    def set_diameter(self, value):
        if isinstance(value, int) or isinstance(value, float) or value is None:
            self._diameter = value
        else:
            raise TypeError("diameter requires as type int, float or NoneType")

    diameter = property(get_diameter, set_diameter)

    def calculate_diameter(self):
        if self.radius is not None:
            self._calculate_diameter_by_radius()
        elif self.area is not None:
            self._calculate_diameter_by_area()
        elif self.perimeter is not None:
            self._calculate_diameter_by_perimeter()
        else:
            raise Exception

        return

    def _calculate_diameter_by_radius(self):
        self.diameter = 2 * self.radius
        return

    def _calculate_diameter_by_area(self):
        self.diameter = 2 * math.sqrt(self.area / math.pi)
        return

    def _calculate_diameter_by_perimeter(self):
        self.diameter = self.perimeter / math.pi
        return

    def get_perimeter(self):
        if self._perimeter or self._perimeter is None:
            return self._perimeter
        else:
            self.calculate_perimeter()
            return self._perimeter

    def set_perimeter(self, value):
        if isinstance(value, int) or isinstance(value, float) or value is None:
            self._perimeter = value
        else:
            raise TypeError("perimeter requires as type int, float or NoneType")

    perimeter = property(get_perimeter, set_perimeter)

    def calculate_perimeter(self):
        if self.radius is not None:
            self._calculate_perimeter_by_radius()
        elif self.diameter is not None:
            self._calculate_perimeter_by_diameter()
        elif self.area is not None:
            self._calculate_perimeter_by_area()
        else:
            raise Exception

        return

    def _calculate_perimeter_by_diameter(self):
        self.perimeter = math.pi * self.diameter
        return

    def _calculate_perimeter_by_radius(self):
        self.perimeter = 2 * math.pi * self.diameter
        return

    def _calculate_perimeter_by_area(self):
        self.perimeter = math.pi * math.sqrt((4 * self.area) / math.pi)
        return

    def get_area(self):
        if self._area or self._area is None:
            return self._area
        else:
            self.calculate_area()
            return self._area

    def set_area(self, value):
        if isinstance(value, int) or isinstance(value, float) or value is None:
            self._area = value
        else:
            raise TypeError("area requires as type int, float or NoneType")

    area = property(get_area, set_area)

    def calculate_area(self):
        if self.radius is not None:
            self._calculate_area_by_radius()
        elif self.diameter is not None:
            self._calculate_area_by_diameter()
        elif self.perimeter is not None:
            self._calculate_area_by_perimeter()
        else:
            raise Exception

        return

    def _calculate_area_by_radius(self):
        self.area = math.pi * (self.radius ** 2)
        return

    def _calculate_area_by_diameter(self):
        self.area = (math.pi * (self.diameter ** 2)) / 4
        return

    def _calculate_area_by_perimeter(self):
        self.area = math.pi * ((self.perimeter / (2 * math.pi)) ** 2)
        return

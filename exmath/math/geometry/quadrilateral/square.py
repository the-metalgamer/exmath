import math


class square(object):

    def __init__(self, side_length=None, area=None, perimeter=None, diagonal_length=None, circumscribed_circle_radius=None, incircle_radius=None):

        self.set_side_length(side_length)
        self.set_area(area)
        self.set_perimeter(perimeter)
        self.set_diagonal_length(diagonal_length)
        self.set_circumscribed_circle_radius(circumscribed_circle_radius)
        self.set_incircle_radius(incircle_radius)

    def get_side_length(self):
        if self._side_length or self._side_length is None:
            return self._side_length
        else:
            self.calculate_side_length()
            return self._side_length

    def set_side_length(self, value):
        if isinstance(value, int) or isinstance(value, float) or value is None:
            self._side_length = value
        else:
            raise TypeError("side length requires as type int, float or NoneType")

    side_length = property(get_side_length, set_side_length)

    def calculate_side_length(self):
        if self.perimeter is not None:
            self._calculate_side_length_by_perimeter()
        elif self.area is not None:
            self._calculate_side_length_by_area()
        elif self.diagonal_length is not None:
            self._calculate_side_length_by_diagonal_length()
        elif self.circumscribed_circle_radius is not None:
            self._calculate_side_lenght_by_circumscribed_circle_radius()
        elif self.incircle_radius is not None:
            self._calculate_side_length_by_incircle_radius()
        else:
            raise Exception
        return

    def _calculate_side_length_by_perimeter(self):
        self.side_length = self.perimeter / 4
        return

    def _calculate_side_length_by_area(self):
        self.side_length = math.sqrt(self.area)
        return

    def _calculate_side_length_by_diagonal_length(self):
        self.side_length = self.diagonal_length / math.sqrt(2)
        return

    def _calculate_side_lenght_by_circumscribed_circle_radius(self):
        self.side_length = self.circumscribed_circle_radius * math.sqrt(2)
        return

    def _calculate_side_length_by_incircle_radius(self):
        self.side_length = self.incircle_radius * 2
        return

    def get_perimeter(self):
        if self._perimeter or self._perimeter is None:
            return self._perimeter
        else:
            self.calculate_perimeter()
            return self._perimter

    def set_perimeter(self, value):
        if isinstance(value, int) or isinstance(value, float) or value is None:
            self._perimeter = value
        else:
            raise TypeError("perimeter requires as type int, float or NoneType")

    perimeter = property(get_perimeter, set_perimeter)

    def calculate_perimeter(self):
        if self.side_length is not None:
            self._calculate_perimeter_by_side_length()
        elif self.area is not None:
            self._calculate_perimeter_by_area()
        elif self.diagonal_length is not None:
            self._calculate_perimeter_by_diagonal_length()
        elif self.circumscribed_circle_radius is not None:
            self._calculate_perimeter_by_circumscribed_circle_radius()
        elif self.incircle_radius is not None:
            self._calculate_perimeter_by_incircle_radius()
        else:
            raise Exception
        return

    def _calculate_perimeter_by_side_length(self):
        self.perimeter = 4 * self.side_length
        return

    def _calculate_perimeter_by_area(self):
        self.perimeter = 4 * math.sqrt(self.area)
        return

    def _calculate_perimeter_by_diagonal_length(self):
        self.perimeter = 4 * (self.diagonal_length / math.sqrt(2))
        return

    def _calculate_perimeter_by_circumscribed_circle_radius(self):
        self.perimeter = 4 * (self.circumscribed_circle_radius * math.sqrt(2))
        return

    def _calculate_perimeter_by_incircle_radius(self):
        self.perimeter = 4 * (2 * self.incircle_radius)
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
        if self.diagonal_length is not None:
            self._calculate_area_by_diagonal_length()
        elif self.side_length is not None:
            self._calculate_area_by_side_length()
        elif self.perimeter is not None:
            self._calculate_area_by_perimeter()
        elif self.circumscribed_circle_radius is not None:
            self._calculate_area_by_circumscribed_circle_radius()
        elif self.incircle_radius is not None:
            self._calculate_area_by_incircle_radius()
        else:
            raise Exception
        return

    def _calculate_area_by_diagonal_length(self):
        self.area = (self.diagonal_length ** 2) / 2
        return

    def _calculate_area_by_side_length(self):
        self.area = self.side_length ** 2
        return

    def _calculate_area_by_perimeter(self):
        self.area = (self.perimeter / 4) ** 2
        return

    def _calculate_area_by_circumscribed_circle_radius(self):
        self.area = (self.circumscribed_circle_radius * math.sqrt(2)) ** 2
        return

    def _calculate_area_by_incircle_radius(self):
        self.area = (2 * self.incircle_radius) ** 2
        return

    def get_diagonal_length(self):
        if self._diagonal_length or self._diagonal_length is None:
            return self._diagonal_length
        else:
            self.calculate_diagonal_length()
            return self._diagonal_length

    def set_diagonal_length(self, value):
        if isinstance(value, int) or isinstance(value, float) or value is None:
            self._diagonal_length = value
        else:
            raise TypeError("diagonal length requires as type int, float or NoneType")

    diagonal_length = property(get_diagonal_length, set_diagonal_length)

    def calculate_diagonal_length(self):
        if self.area is not None:
            self._calculate_diagonal_length_by_area()
        elif self.side_length is not None:
            self._calculate_diagonal_length_by_side_length()
        elif self.perimeter is not None:
            self._calculate_diagonal_length_by_perimeter()
        elif self.circumscribed_circle_radius is not None:
            self._calculate_diagonal_length_by_circumscribed_circle_radius()
        elif self.incircle_radius is not None:
            self._calculate_diagonal_length_by_incircle_radius()
        else:
            raise Exception
        return

    def _calculate_diagonal_length_by_area(self):
        self.diagonal_length = math.sqrt(self.area) * math.sqrt(2)
        return

    def _calculate_diagonal_length_by_side_length(self):
        self.diagonal_length = self.side_length * math.sqrt(2)
        return

    def _calculate_diagonal_length_by_perimeter(self):
        self.diagonal_length = (self.perimeter / 4) * math.sqrt(2)
        return

    def _calculate_diagonal_length_by_circumscribed_circle_radius(self):
        self.diagonal_length = (self.circumscribed_circle_radius * math.sqrt(2)) * math.sqrt(2)
        return

    def _calculate_diagonal_length_by_incircle_radius(self):
        self.diagonal_length = (self.incircle_radius * 2) * math.sqrt(2)
        return

    def get_circumscribed_circle_radius(self):
        if self._circumscribed_circle_radius or self._circumscribed_circle_radius is None:
            return self._circumscribed_circle_radius
        else:
            self.calculate_circumscribed_circle_radius()
            return self._circumscribed_circle_radius

    def set_circumscribed_circle_radius(self):
        if isinstance(value, int) or isinstance(value, float) or value is None:
            self._circumscribed_circle_radius = value
        else:
            raise TypeError("circumscribed circle radius requires as type int, float or NoneType")

    circumscribed_circle_radius = property(get_circumscribed_circle_radius, set_circumscribed_circle_radius)

    def calculate_circumscribed_circle_radius(self):
        if self.side_length is not None:
            self._calculate_circumscribed_circle_radius_by_side_length()
        elif self.perimeter is not None:
            self._calculate_circumscribed_circle_radius_by_perimeter()
        elif self.area is not None:
            self._calculate_circumscribed_circle_radius_by_area()
        elif:
            self._calculate_circumscribed_circle_radius_by_diagonal_length()
        elif:
            self._calculate_circumscribed_circle_radius_by_incircle_radius()
        else:
            raise Exception

        return

    def _calculate_circumscribed_circle_radius_by_side_length(self):
        self.circumscribed_circle_radius = self.side_length / math.sqrt(2)
        return

    def _calculate_circumscribed_circle_radius_by_perimeter(self):
        self.circumscribed_circle_radius = (self.perimeter / 4) / math.sqrt(2)
        return

    def _calculate_circumscribed_circle_radius_by_area(self):
        self.circumscribed_circle_radius = math.sqrt(self.area) / math.sqrt(2)
        return

    def _calculate_circumscribed_circle_radius_by_diagonal_length(self):
        self.circumscribed_circle_radius = (self.diagonal_length / math.sqrt(2)) / math.sqrt(2)
        return

    def _calculate_circumscribed_circle_radius_by_incircle_radius(self):
        self.circumscribed_circle_radius = (self.incircle_radius * 2) / math.sqrt(2)
        return

    def get_incircle_radius(self):
        if self._incircle_radius or self._incircle_radius is None:
            return self._incircle_radius
        else:
            self.calculate_incircle_radius()
            return self._incircle_radius

    def set_incircle_radius(self, value):
        if isinstance(value, int) or isinstance(value, float) or value is None:
            self._incircle_radius = value
        else:
            raise TypeError("incircle radius requires as type int, float or NoneType")

    incircle_radius = property(get_incircle_radius, set_incircle_radius)

    def calculate_incircle_radius(self):
        if self.side_length is not None:
            self._calculate_incircle_radius_by_side_length()
        elif self.perimeter is not None:
            self._calculate_incircle_radius_by_perimeter()
        elif self.area is not None:
            self._calculate_incircle_radius_by_area()
        elif self.diagonal_length is not None:
            self._calculate_incircle_radius_by_diagonal_lenght()
        elif self.circumscribed_circle_radius is not None:
            self._calculate_incircle_radius_by_circumscribed_circle_radius()
        else:
            raise Exception

        return

    def _calculate_incircle_radius_by_side_length(self):
        self.incircle_radius = self.side_length / 2
        return

    def _calculate_incircle_radius_by_perimeter(self):
        self.incircle_radius = (self.perimeter / 4) / 2
        return

    def _calculate_incircle_radius_by_area(self):
        self.incircle_radius = math.sqrt(self.area) / 2
        return

    def _calculate_incircle_radius_by_diagonal_lenght(self):
        self.incircle_radius = (self.diagonal_length / math.sqrt(2)) / 2
        return

    def _calculate_incircle_radius_by_circumscribed_circle_radius(self):
        self.incircle_radius = (self.circumscribed_circle_radius * math.sqrt(2)) / 2
        return

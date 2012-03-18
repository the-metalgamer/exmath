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

ANGLES_FACES = math.pi / 2

class cube(square.square):

    def __init__(self, surface_area = None, volume = None, space_diagonal_length = None, circumscribed_sphere_radius = None, **kwds):

        self.set_surface_area(surface_area)
        self.set_volume(volume)
        self.set_space_diagonal_length(space_diagonal_length)
        self.set_circumscribed_sphere_radius(circumscribed_sphere_radius)

        super().__init__(**kwds)

    def get_surface_area(self):
        if self._surface_area or self._surface_area is None:
            return self._surface_area
        else:
            self.calculate_surface_area()
            return self._surface_area

    def set_surface_area(self,value):
        if isinstance(value,int) or isinstance(value,float) or value is None:
            self._surface_area = value
        else:
            raise TypeError("surface area requires as type int, float or NoneType")

    surface_area = property(get_surface_area,set_surface_area)

    def calculate_surface_area(self):
        if self.side_length is not None:
            self._calculate_surface_area_by_side_length()
        elif self.volume is not None:
            self._calculate_surface_area_by_volume()
        elif self.diagonal_length is not None:
            self._calculate_surface_area_by_diagonal_length()
        elif self.space_diagonal_length is not None:
            self._calculate_surface_area_by_space_diagonal_length()
        elif self.circumscribed_sphere_radius is not None:
            self._calculate_surface_area_by_circumscribed_sphere_radius()
        elif self.circumscribed_circle_radius is not None:
            self._calculate_surface_area_by_circumscribed_circle_radius()
        elif self.incircle_radius is not None:
            self._calculate_surface_area_by_incircle_radius()
        elif self.area is not None:
            self._calculate_surface_area_by_area()
        elif self.perimeter is not None:
            self._calculate_surface_area_by_perimeter()
        else:
            raise Exception

        return

    def _calculate_surface_area_by_side_length(self):
        self.surface_area = 6 * self.side_length ** 2
        return

    def _calculate_surface_area_by_volume(self):
        self.surface_area = 6 * (helpers.cube_root(self.volume) ** 2)
        return

    def _calculate_surface_area_by_diagonal_length(self):
        self.surface_area = 6 * ((self.diagonal_length / math.sqrt(2) ** 2))
        return

    def _calculate_surface_area_by_space_diagonal_length(self):
        self.surface_area = 6 * ((self.space_diagonal_length / math.sqrt(3) ** 2))
        return

    def _calculate_surface_area_by_circumscribed_sphere_radius(self):
        self.surface_area = 6 * ((self.circumscribed_circle_radius / (math.sqrt(3) / 2)) ** 2)
        return

    def _calculate_surface_area_by_circumscribed_circle_radius(self):
        self.surface_area = 6 * ((self.circumscribed_circle_radius * math.sqrt(2)) ** 2)
        return

    def _calculate_surface_area_by_incircle_radius(self):
        self.surface_area = 6 * ((self.incircle_radius * 2) ** 2)
        return

    def _calculate_surface_area_by_area(self):
        self.surface_area = 6 * self.area
        return

    def _calculate_surface_area_by_perimeter(self):
        self.surface_area = 6 * ((self.perimeter / 4) ** 2)
        return

    def get_volume(self):
        if self._volume or self._volume is None:
            return self._volume
        else:
            self.calculate_volume()
            return self._volume

    def set_volume(self, value):
        if isinstance(value, int) or isinstance(value, float) or value is None:
            self._volume = value
        else:
            raise TypeError("volume requires as type int, float or NoneType")

    volume = property(get_volume, set_volume)

    def calculate_volume(self):
        if self.side_length is not None:
            self._calculate_volume_by_side_length()
        elif self.surface_area is not None:
            self._calculate_volume_by_surface_area()
        elif self.diagonal_length is not None:
            self._calculate_volume_by_diagonal_length()
        elif self.space_diagonal_length is not None:
            self._calculate_volume_by_space_diagonal_length()
        elif self.circumscribed_sphere_radius is not None:
            self._calculate_volume_by_circumscribed_sphere_radius()
        elif self.circumscribed_circle_radius is not None:
            self._calculate_volume_by_circumscribed_circle_radius()
        elif self.incircle_radius is not None:
            self._calculate_volume_by_incircle_radius()
        elif self.perimeter is not None:
            self._calculate_volume_by_perimeter()
        elif self.area is not None:
            self._calculate_volume_by_area()
        else:
            raise Exception

        return

    def _calculate_volume_by_side_length(self):
        self.volume = self.side_length ** 3
        return

    def _calculate_volume_by_surface_area(self):
        self.volume = (math.sqrt((self.surface_area / 6))) ** 3
        return

    def _calculate_volume_by_diagonal_length(self):
        self.volume = (self.diagonal_length / math.sqrt(2)) ** 3
        return

    def _calculate_volume_by_space_diagonal_length(self):
        self.volume = (self.space_diagonal_length / math.sqrt(3)) ** 3
        return

    def _calculate_volume_by_circumscribed_sphere_radius(self):
        self.volume = ( (self.circumscribed_sphere_radius / ( math.sqrt(3) / 2))) ** 3
        return

    def _calculate_volume_by_circumscribed_circle_radius(self):
        self.volume = (self.circumscribed_circle_radius * math.sqrt(2)) ** 3
        return

    def _calculate_volume_by_incircle_radius(self):
        self.volume = (self.incircle_radius * 2) ** 3
        return

    def _calculate_volume_by_perimeter(self):
        self.volume = (self.perimeter / 4) ** 3
        return

    def _calculate_volume_by_area(self):
        self.volume = (math.sqrt(self.area)) ** 3
        return

    def get_space_diagonal_length(self):
        if self._space_diagonal_length or self._space_diagonal_length is None:
            return self._space_diagonal_length
        else:
            self.calculate_space_diagonal_length()
            return self._space_diagonal_length

    def set_space_diagonal_length(self, value):
        if isinstance(value, int) or isinstance(value, float) or value is None:
            self.space_diagonal_length = value
        else:
            raise TypeError("space diagonal length requires as type int, float or NoneType")

    space_diagonal_length = property(get_space_diagonal_length, set_space_diagonal_length)

    def calculate_space_diagonal_length(self):
        if self.side_length is not None:
            self._calculate_space_diagonal_length_by_side_length()
        elif self.surface_area is not None:
            self. _calculate_space_diagonal_length_by_surface_area()
        elif self.volume is not None:
            self._calculate_space_diagonal_length_by_volume()
        elif: self.circumscribed_sphere_radius is not None:
            self._calculate_space_diagonal_length_by_circumscribed_sphere_radius()
        elif self.circumscribed_circle_radius is not None:
            self._calculate_space_diagonal_length_by_circumscribed_circle_radius()
        elif self.incircle_radius is not None:
            self._calculate_space_diagonal_length_by_incircle_radius()
        elif self.diagonal_length is not None:
            self._calculate_space_diagonal_length_by_diagonal_length()
        elif self.area is not None:
            self._calculate_space_diagonal_length_by_area()
        elif self.perimeter is not None:
            self._calculate_space_diagonal_length_by_perimeter()
        else:
            raise Exception

        return

    def _calculate_space_diagonal_length_by_side_length(self):
        self.space_diagonal_length = math.sqrt(3) * self.side_length
        return

    def _calculate_space_diagonal_length_by_surface_area(self):
        self.space_diagonal_length = math.sqrt(3) * math.sqrt(self.surface_area / 6)
        return

    def _calculate_space_diagonal_length_by_volume(self):
        self.space_diagonal_length = math.sqrt(3) * helpers.cube_root(self.volume)
        return

    def _calculate_space_diagonal_length_by_circumscribed_sphere_radius(self):
        self.space_diagonal_length = math.sqrt(3) * (self.circumscribed_sphere_radius / (math.sqrt(3) / 2))
        return

    def _calculate_space_diagonal_length_by_circumscribed_circle_radius(self):
        self.space_diagonal_length = math.sqrt(3) * self.circumscribed_circle_radius * math.sqrt(2)
        return

    def _calculate_space_diagonal_length_by_incircle_radius(self):
        self.space_diagonal_length = math.sqrt(3) * self.incircle_radius * 2
        return

    def _calculate_space_diagonal_length_by_diagonal_length(self):
        self.space_diagonal_length = math.sqrt(3) * (self.diagonal_length / math.sqrt(2))
        return

    def _calculate_space_diagonal_length_by_area(self):
        self.space_diagonal_length = math.sqrt(3) * math.sqrt(self.area)
        return

    def _calculate_space_diagonal_length_by_perimeter(self):
        self.space_diagonal_length = math.sqrt(3) * (self.perimeter / 4)
        return

    def get_circumscribed_sphere_radius(self):
        if self._circumscribed_sphere_radius or self._circumscribed_sphere_radius is None:
            return self._circumscribed_sphere_radius
        else:
            self.calculate_circumscribed_sphere_radius()
            return self._circumscribed_sphere_radius

    def set_circumscribed_sphere_radius(self, value):
        if isinstance(value, int) or isinstance(value,float) or value is None:
            self._circumscribed_sphere_radius = value
        else:
            raise TypeError("circumscribed sphere radius requires as type int, float or NoneType")

    circumscribed_sphere_radius = property(get_circumscribed_sphere_radius, set_circumscribed_sphere_radius)

    def calculate_circumscribed_sphere_radius(self):
        if self.side_length is not None:
            self._calculate_circumscribed_sphere_radius_by_side_length()
        elif self.surface_area is not None:
            self._calculate_circumscribed_sphere_radius_by_surface_area()
        elif self.volume is not None:
            self._calculate_circumscribed_sphere_radius_by_volume()
        elif self.diagonal_length is not None:
            self._calculate_circumscribed_sphere_radius_by_diagonal_length()
        elif self.space_diagonal_length is not None:
            self._calculate_circumscribed_sphere_radius_by_space_diagonal_length()
        elif self.circumscribed_circle_radius is not None:
            self._calculate_circumscribed_sphere_radius_by_circumscribed_circle_radius()
        elif self.incircle_radius is not None:
            self._calculate_circumscribed_sphere_radius_by_incircle_radius()
        elif self.area is not None:
            self._calculate_circumscribed_sphere_radius_by_area()
        elif self.perimeter is not None:
            self._calculate_circumscribed_sphere_radius_by_perimeter()
        else:
            raise Exception

        return

    def _calculate_circumscribed_sphere_radius_by_side_length(self):
        self.circumscribed_sphere_radius = (math.sqrt(3) / 2) * self.side_length
        return

    def _calculate_circumscribed_sphere_radius_by_surface_area(self):
        self.circumscribed_sphere_radius = (math.sqrt(3) / 2) * math.sqrt(self.surface_area / 6)
        return

    def _calculate_circumscribed_sphere_radius_by_volume(self):
        self.circumscribed_sphere_radius = (math.sqrt(3) / 2) * helpers.cube_root(self.volume)
        return

    def _calculate_circumscribed_sphere_radius_by_diagonal_length(self):
        self.circumscribed_sphere_radius = (math.sqrt(3) / 2) * (self.diagonal_length / math.sqrt(2))
        return

    def _calculate_circumscribed_sphere_radius_by_space_diagonal_length(self):
        self.circumscribed_sphere_radius = (math.sqrt(3) / 2) * (self.space_diagonal_length / math.sqrt(3))
        return

    def _calculate_circumscribed_sphere_radius_by_circumscribed_circle_radius(self):
        self.circumscribed_sphere_radius = (math.sqrt(3) / 2) * (self.circumscribed_circle_radius * math.sqrt(2))
        return

    def _calculate_circumscribed_sphere_radius_by_incircle_radius(self):
        self.circumscribed_sphere_radius = (math.sqrt(3) / 2) * (self.incircle_radius * 2)
        return

    def _calculate_circumscribed_sphere_radius_by_area(self):
        self.circumscribed_sphere_radius = (math.sqrt(3) / 2) * math.sqrt(self.area)
        return

    def _calculate_circumscribed_sphere_radius_by_perimeter(self):
        self.circumscribed_sphere_radius = (math.sqrt(3) / 2) * (self.perimeter / 4)
        return

    def calculate_side_length(self):
        if self.volume is not None:
            self._calculate_side_length_by_volume()
        elif self.surface_area is not None:
            self._calculate_side_length_by_surface_area()
        elif self.space_diagonal_length is not None:
            self._calculate_side_length_by_space_diagonal_length()
        elif self.circumscribed_sphere_radius is not None:
            self._calculate_side_length_by_circumscribed_sphere_radius()
        else:
            super().calculate_side_length()

        return

    def _calculate_side_length_by_volume(self):
        self.side_length = helpers.cube_root(self.volume)
        return

    def _calculate_side_length_by_surface_area(self):
        self.side_length = math.sqrt(self.surface_area/6)
        return

    def _calculate_side_length_by_space_diagonal_length(self):
        self.side_length = self.space_diagonal_length * math.sqrt(3)
        return

    def _calculate_side_length_by_circumscribed_sphere_radius(self):
        self.side_length = self.circumscribed_sphere_radius / (2 * math.sqrt(3))
        return

    def calculate_area(self):
        if self.surface_area is not None:
            self._calculate_area_by_surface_area()
        elif self.volume is not None:
            self._calculate_area_by_volume()
        elif self.space_diagonal_length is not None:
            self._calculate_area_by_space_diagonal_length()
        elif self.circumscribed_sphere_radius is not None:
            self._calculate_area_by_circumscribed_sphere_radius()
        else:
            super().calculate_area()

        return

    def _calculate_area_by_surface_area(self):
        self.area = self.surface_area / 6
        return

    def _calculate_area_by_volume(self):
        self.area = helpers.cube_root(self.volume) ** 2
        return

    def _calculate_area_by_space_diagonal_length(self):
        self.area = (self.space_diagonal_length / math.sqrt(3)) ** 2
        return

    def _calculate_area_by_circumscribed_sphere_radius(self):
        self.area = (self.circumscribed_sphere_radius / (math.sqrt(3) / 2)) ** 2
        return

    def calculate_perimeter(self):
        if self.surface_area is not None:
            self._calculate_perimeter_by_surface_area()
        elif self.volume is not None:
            self._calculate_perimeter_by_volume()
        elif self.space_diagonal_length is not None:
            self._calculate_perimeter_by_space_diagonal_length()
        elif self.circumscribed_sphere_radius is not None:
            self._calculate_perimeter_by_circumscribed_sphere_radius()
        else:
            super().calculate_perimeter()

        return

    def _calculate_perimeter_by_surface_area(self):
        self.perimeter = 4 * math.sqrt(self.surface_area / 6)
        return

    def _calculate_perimeter_by_volume(self):
        self.perimeter = 4 * helpers.cube_root(self.volume)
        return

    def _calculate_perimeter_by_space_diagonal_length(self):
        self.perimeter = 4 * (self.space_diagonal_length / math.sqrt(3))
        return

    def _calculate_perimeter_by_circumscribed_sphere_radius(self):
        self.perimeter = 4 * (self.circumscribed_sphere_radius / (math.sqrt(3) / 2))
        return

    def calculate_diagonal_length(self):
        if self.surface_area is not None:
            self._calculate_diagonal_length_by_surface_area()
        elif self.volume is not None:
            self._calculate_diagonal_length_by_volume()
        elif self.space_diagonal_length is not None:
            self._calculate_diagonal_length_by_space_diagonal_length()
        elif self.circumscribed_sphere_radius is not None:
            self._calculate_diagonal_length_by_circumscribed_sphere_radius()
        else:
            super().calculate_diagonal_length()

        return

    def _calculate_diagonal_length_by_surface_area(self):
        self.diagonal_length = math.sqrt(self.surface_area / 6) * math.sqrt(2)
        return

    def _calculate_diagonal_length_by_volume(self):
        self.diagonal_length = helpers.cube_root(self.volume) * math.sqrt(2)
        return

    def _calculate_diagonal_length_by_space_diagonal_length(self):
        self.diagonal_length = (self.space_diagonal_length / math.sqrt(3)) * math.sqrt(2)
        return

    def _calculate_diagonal_length_by_circumscribed_sphere_radius(self):
        self.diagonal_length = (self.circumscribed_sphere_radius / (math.sqrt(3) / 2)) * math.sqrt(2)
        return

    def calculate_circumscribed_circle_radius(self):
        if self.surface_area is not None:
            self._calculate_circumscribed_circle_radius_by_surface_area()
        elif self.volume is not None:
            self._calculate_circumscribed_circle_radius_by_volume()
        elif self.space_diagonal_length is not None:
            self._calculate_circumscribed_circle_radius_by_space_diagonal_length()
        elif self.circumscribed_sphere_radius is not None:
            self._calculate_circumscribed_circle_radius_by_circumscribed_sphere_radius()
        else:
            super().calculate_circumscribed_circle_radius()

        return

    def _calculate_circumscribed_circle_radius_by_surface_area(self):
        self.circumscribed_circle_radius = math.sqrt(self.surface_area / 6) / math.sqrt(2)
        return

    def _calculate_circumscribed_circle_radius_by_volume(self):
        self.circumscribed_circle_radius = helpers.cube_root(self.volume) / math.sqrt(2)
        return

    def _calculate_circumscribed_circle_radius_by_space_diagonal_length(self):
        self.circumscribed_circle_radius = (self.space_diagonal_length / math.sqrt(3)) / math.sqrt(2)
        return

    def _calculate_circumscribed_circle_radius_by_circumscribed_sphere_radius(self):
        self.circumscribed_circle_radius = (self.circumscribed_sphere_radius / (math.sqrt(3) / 2)) / math.sqrt(2)
        return

    def calculate_incircle_radius(self):
        if self.surface_area is not None:
            self._calculate_incircle_radius_by_surface_area()
        elif self.volume is not None:
            self._calculate_incircle_radius_by_volume()
        elif self.space_diagonal_length is not None:
            self._calculate_incircle_radius_by_space_diagonal_length()
        elif self.circumscribed_sphere_radius is not None:
            self._calculate_incircle_radius_by_circumscribed_sphere_radius()
        else:
            super().calculate_incircle_radius()

        return

    def _calculate_incircle_radius_by_surface_area(self):
        self.incircle_radius = math.sqrt(self.surface_area / 6) / 2
        return

    def _calculate_incircle_radius_by_volume(self):
        self.incircle_radius = helpers.cube_root(self.volume) / 2
        return

    def _calculate_incircle_radius_by_space_diagonal_length(self):
        self.incircle_radius = (self.space_diagonal_length / math.sqrt(3)) / 2
        return

    def _calculate_incircle_radius_by_circumscribed_sphere_radius(self):
        self.incircle_radius = (self.circumscribed_sphere_radius / (math.sqrt(3) / 2)) / 2
        return


class rectangle(object):

    def __init__(self, long_side=None, short_side=None, area=None, perimeter=None, diagonal_length=None, circumscribed_circle_radius=None):

        self.set_long_side(long_side)
        self.set_short_side(short_side)
        self.set_area(area)
        self.set_perimeter(perimeter)
        self.set_diagonal_length(diagonal_length)
        self.set_circumscribed_circle_radius(circumscribed_circle_radius)

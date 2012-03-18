import math

import circle
import helpers

class sphere(circle.circle):

    def __init__(self, volume = None, surface_area = None, **kwds):
        
        self.set_volume(volume)
        self.set_surface_area(surface_area)

        super().__init__(**kwds)

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
        if self.radius is not None:
            self._calculate_volume_by_radius()
        elif self.diameter is not None:
            self._calculate_volume_by_diameter()
        elif self.area is not None:
            self._calculate_volume_by_area()
        elif self.perimeter is not None:
            self._calculate_volume_by_perimeter()
        elif self.surface_area is not None:
            self._calculate_volume_by_surface_area()
        else:
            raise Exception

        return

    def _calculate_volume_by_radius(self):
        self.volume = (4 / 3) * math.pi * (self.radius ** 3)
        return

    def _calculate_volume_by_diameter(self):
        self.volume = (1 / 6) * math.pi * (self.diameter ** 3)
        return

    def _calculate_volume_by_area(self):
        self.volume = (4 / 3) * math.pi * (math.sqrt(self.area / math.pi) ** 3)
        return

    def _calculate_volume_by_perimeter(self):
        self.volume = (4 / 3) * math.pi * ((self.perimeter / (2 * math.pi)) ** 3)
        return

    def _calculate_volume_by_surface_area(self):
        self.volume = (4 / 3) * math.pi * ((math.sqrt(self.surface_area / 4 *
                        math.pi) ) ** 3)
        return

    def get_surface_area(self):
        if self._surface_area or self._surface_area is None:
            return self._surface_area
        else:
            self.calculate_surface_area()
            return self._surface_area

    def set_surface_area(self, value):
        if isinstance(value, int) or isinstance(value, float) or value is None:
            self._surface_area = value
        else:
            raise TypeError("surface area requires as type int, float or
                    NoneType")

    surface_area = property(get_surface_area, set_surface_area)

    def calculate_surface_area(self):
        if self.radius is not None:
            self._calculate_surface_area_by_radius()
        elif self.diameter is not None:
            self._calculate_surface_area_by_diameter()
        elif self.area is not None:
            self._calculate_surface_area_by_area()
        elif self.perimeter is not None:
            self._calculate_surface_area_by_perimeter()
        elif self.volume is not None:
            self._calculate_surface_area_by_volume()
        else:
            raise Exception

        return

    def _calculate_surface_area_by_radius(self):
        self.surface_area = 4 * math.pi * (self.radius ** 2)
        return

    def _calculate_surface_area_by_diameter(self):
        self.surface_area = math.pi * (self.diameter ** 2)
        return

    def _calculate_surface_area_by_area(self):
        self.surface_area = 4 * math.sqrt(self.area)**2
        return

    def _calculate_surface_area_by_perimeter(self):
        self.surface_area = (self.perimeter ** 2) / math.pi
        return

    def _calculate_surface_area_by_volume(self):
        self.surface_area = 4 * math.pi * helpers.cube_root((3 * self.volume) /
                (4 * math.pi)) ** 2)
        return

    def calculate_radius(self):
        if self.surface_area is not None:
            self._calculate_radius_by_surface_area()
        elif self.volume is not None:
            self._caclculate_radius_by_volume()
        else:
            super().calculate_radius()

        return

    def _calculate_radius_by_surface_area(self):
        self.radius = math.sqrt(self.surface_area / (4 * math.pi))
        return

    def _calculate_radius_by_volume(self):
        self.radius = helpers.cube_root((3 * self.volume) / (4 * math.pi))
        return

    def calculate_diameter(self):
        if self.surface_area is not None:
            self._calculate_diameter_by_surface_area()
        elif self.volume is not None:
            self._calculate_diameter_by_volume()
        else:
            super().calculate_diameter()

        return

    def _calculate_diameter_by_surface_area(self):
        self.diameter = math.sqrt(self.surface_area / math.pi)
        return

    def _calculate_diameter_by_volume(self):
        self.diameter = helpers.cube_root((6 * self.volume) / math.pi)
        return

    def calculate_area(self):
        if self.surface_area is not None:
            self._calculate_area_by_surface_area()
        elif self.volume is not None:
            self._calculate_area_by_volume()
        else:
            super().calculate_area()

        return

    def _calculate_area_by_surface_area(self):
        self.area = math.pi * (math.sqrt(self.surface_area / (4 * math.pi)) **
                2)
        return

    def _calculate_area_by_volume(self):
        self.area = math.pi * (helpers.cube_root((3 * self.volume) / (4 *
                        math.pi)) ** 2)
        return

    def calculate_perimeter(self):
        if self.surface_area is not None:
            self._calculate_perimeter_by_surface_area()
        elif self.volume is not None:
            self._calculate_perimeter_by_volume()
        else:
            super().calculate_perimeter()

        return

    def _calculate_perimeter_by_surface_area(self):
        self.perimeter = 2 * math.pi * (math.sqrt(self.surface_area / (4 *
                        math.pi)))
        return

    def _calculate_perimeter_by_volume(self):
        self.perimeter = 2 * math.pi * (helpers.cube_root((3 * self.volume) /
                    (4 * math.pi)))
        return


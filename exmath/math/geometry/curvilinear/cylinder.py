import math

import circle

class cylinder(circle.circle):

    def __init__(self, height = None, surface_area = None, volume = None, surface = None, **kwargs):
        self.set_height(height)
        self.set_surface_area(surface_area)
        self.set_volume(volume)
        self.set_surface(surface)

        super().__init__(**kwargs)

    def get_height(self):
        if self._height or self._height is None:
            return self._height
        else:
            self.calculate_height()
            return self._height

    def set_height(self, value):
        if isinstance(value, int) or isinstance(value, float) or value is None:
            self._height = value
        else:
            raise TypeError("height requires as type int, float or NoneType")

    height = property(get_height, set_height)

    def calculate_height(self):
        if self.volume is not None:
            self._calculate_height_by_volume()
        elif self.surface_area is not None:
            self._calculate_height_by_surface_area()
        elif self.surface is not None:
            self._calculate_height_by_surface()
        else:
            raise Exception

        return

    def _calculate_height_by_volume(self):
        self.height = self.volume / (math.pi * self.radius ** 2)
        return

    def _calculate_height_by_surface(self):
        self.height = self.surface / (2 * math.pi * self.radius)
        return

    def _calculate_height_by_surface_area(self):
        self.height = (self.surface_area - (2 * math.pi * self.radius)) / (2 * math.pi * self.radius)
        return

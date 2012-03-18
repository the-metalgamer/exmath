
import math


class triangle:

    def __init__(self):
        self.a_length = 0
        self.b_length = 0
        self.c_length = 0
        self.angle_alpha = 0
        self.angle_beta = 0
        self.angle_gamma = 0

    def get_angle_alpha(self):
        if self.angle_alpha:
            return self.angle_alpha
        elif self.angle_beta and self.angle_gamma:
            self.angle_alpha = 180 - self.angle_beta - self.angle_gamma
        elif self.a_length and self.b_length and self.c_length:
            self.angle_alpha = math.acos((self.b_length**2+self.c_length**2-self.a_length**2)/2*self.b_length*self.c_length)
            return self.angle_alpha
        elif self.a_length and self.c_length and self.angle_beta:
            self.angle_alpha = math.asin((math.sin(self.angle_beta)*self.a_length)/math.sqrt(self.a_length**2 + self.c_length**2 - 2 * self.a_length * self.c_length * math.cos(self.angle_beta)))
            return self.angle_alpha
        elif self.b_length and self.c_length and self.angle_gamma    
    
    def get_angle_beta(self):
        if self.angle_beta:
            return self.angle_beta
        elif self.a_length and self.b_length and self.c_length:
            self.angle_beta = math.acos((self.a_length**2+self.c_length**2-self.b_length**2)/2*self.a_length*self.c_length)
            return self.angle_beta

    def get_angle_gamma(self):
        if self.angle_gamma:
            return self.angle_gamma
        elif self.a_length and self.b_length and self.c_length:
            self.angle_gamma = math.acos((self.a_length**2+self.b_length**2-self.c_length**2)/2*self.a_length*self.b_length)
            return self.angle_gamma

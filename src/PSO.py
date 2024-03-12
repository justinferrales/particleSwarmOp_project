import random
import numpy as np

class Particle:
    def __init__(self, x, v, w, phi_p, phi_g, target_location):
        """
        x is position R^n, v is velocity, etc
        self.x = x, etc
        """
        self.x = x
        self.v = v
        self.w = w
        self.phi_p = phi_p
        self.phi_g = phi_g
        self.p = x.copy()
        self.value = f(x, target_location)
    def updatePosition(self):
        # implement x = x+v on self
        self.x += self.v
    def updateVelocity(self, g):
        # random r_p and r_g
        # then update self.v = ...
        # picking uniform random randoms on uniform distribution
        r_p = random.random()
        r_g = random.random()
        self.v = (self.w*self.v) + ((self.phi_p*r_p)*(self.p - self.x)) + ((self.phi_g*r_g)*(g-self.x))
    def updateValue(self, target_location):
        """
        calculate self.value, based on f(x)
        in the mean time may as well update my best know position
        # ie update p
        """
        self.value = f(self.x, target_location)
        if self.value < f(self.p, target_location):
            self.p = self.x.copy()


def f(x, target_location):
    # Manhattan distance-based objective function
    # Assuming the target location is at (0, 0)
    return np.sum(np.abs(x - target_location))


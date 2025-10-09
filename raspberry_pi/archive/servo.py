"""This is a template code to be completed when we set up the servos completely"""

import numpy as np


LENGTH = 400
WIDTH = 300

def get_radius(angle):
    return LENGTH / np.tan(np.deg2rad(angle))


"""
The way this will work is by asigning a wanted angle to the side it is turning to:
So if based on the angle, we are turning left, we will asign the left side to turn that much
Simillarly for turning right

And then we will calculate the radiuses neccessary for the inner and outer wheels.
Based on this we will calculate and asign the angles to the servos
"""

# Example of how the servos would be controlled

class Rover():
    def __init__(self, wheels, max_turn_angle):
        '''
        Initialize the rover's parameters
        wheels => list of wheels (1st 3 on the left, the other 3 on the right side of the rover)
        '''
        self.wheels = wheels

        self.max_turn_angle = max_turn_angle
        self.angle = 0

    
    def turn(self, a):
        '''
        turn the rover by `a` degrees conter clockwise
        '''

        self.angle += a
        if abs(self.angle) > self.max_turn_angle:
            self.angle = (self.angle / abs(self.angle)) * self.max_turn_angle

        # check which way the rover is turning
        if  self.angle > 0:
            # if turning to the left
            self.wheels[0].angle = self.angle
            r1 = get_radius(self.wheels[0].angle)  # Inner radius
    
            # Calculate the outer radius (for outer front wheel)
            r2 = get_radius(self.wheels[0].angle) + WIDTH / 2  # Outer radius
            
            # Calculate the outer wheel angle (for outer front wheel)
            self.wheels[3].angle = np.rad2deg(np.arctan(LENGTH / r2))  # Outer right wheel angle
            
            # Rear wheels (steering in opposite direction for sharper turn)
            self.wheels[2].angle = -self.wheels[0].angle  # Rear left wheel
            self.wheels[5].angle = -self.wheels[3].angle  # Rear right wheel
        elif self.angle < 0:
            # if turning to the right
            self.wheels[3].angle = self.angle
            r1 = get_radius(self.wheels[3].angle)  # Inner radius
    
            # Calculate the outer radius (for outer front wheel)
            r2 = get_radius(self.wheels[3].angle) - WIDTH / 2  # Outer radius
            
            # Calculate the outer wheel angle (for outer front wheel)
            self.wheels[0].angle = np.rad2deg(np.arctan(LENGTH / r2))  # Outer right wheel angle
            
            # Rear wheels (steering in opposite direction for sharper turn)
            self.wheels[2].angle = -self.wheels[0].angle  # Rear left wheel
            self.wheels[5].angle = -self.wheels[3].angle  # Rear right wheel
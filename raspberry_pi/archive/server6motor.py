import asyncio
import websockets
import serial
"""This is a template code to be completed when we set up the servos completely"""

import numpy as np
def_angle = 90

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
        self.angle = def_angle

    
    def turn(self, a):
        '''
        turn the rover by `a` degrees counter clockwise
        '''

        self.angle += a
        if abs(self.angle) > self.max_turn_angle:
            self.angle = (self.angle / abs(self.angle)) * self.max_turn_angle

        # check which way the rover is turning
        if  self.angle > def_angle:
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
        elif self.angle < def_angle:
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

# Constants
PORT = 8765

# Serial connection to the Arduino Nano
serial = serial.Serial("/dev/ttyACM0", 9600, timeout=1)

async def connect(websocket):
    print("[*] Connection Established!")
    
    # Listen for commands
    while True:
        try:
            outer_speed = 255
            inner_speed = outer_speed/Rover.r2*Rover.r1
            # Wait for a command
            command = await websocket.recv(4)
            print(f"[*] Recieved: {command}")

            # Do something about the recieved command her
            
            if command[1] == "1":
                serial.write(b'\xff\xff\xff\xff\xff\xff')
            elif command[2] == "1":
                serial.write(b'\x00\x00\x00\x00\x00\x00')
            else:
                serial.write(b"\x7f\x7f\x7f\x7f\x7f\x7f")
            if command[3] == "1":
                right = bytearray([outer_speed, outer_speed, outer_speed, inner_speed, inner_speed, inner_speed])
                serial.write(right)
            if command[4] == "1":
                left = bytearray([inner_speed, inner_speed, inner_speed, outer_speed, outer_speed, outer_speed])
                serial.write(left)

        except websockets.exceptions.ConnectionClosed as e:
            print(f"[*] Connection Closed: {e}")
            break


async def main():
    async with websockets.serve(connect, "0.0.0.0", PORT):
        print(f"[*] Server Started on Port {PORT}")
        await asyncio.Future() # run forever


# Start the Server
if __name__ == "__main__":
    asyncio.run(main())


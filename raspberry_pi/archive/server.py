import asyncio
import websockets
import serial

# Constants
PORT = 8765

# Serial connection to the Arduino Nano
serial = serial.Serial("/dev/ttyACM0", 9600, timeout=1)

async def connect(websocket):
    """Connect to a client and listen for commands"""
    print("[*] Connection Established!")
    
    # Listen for commands
    while True:
        try:
            # Wait for a command
            command = await websocket.recv()
            print(f"[*] Recieved: {command}")

            # Do something about the recieved command here
            # Example sending 1 or 0 to arduino which turns an led on/off
            if command == "1":
                serial.write(b'1')
            elif command == "0":
                serial.write(b'0')

        except websockets.exceptions.ConnectionClosed as e:
            print(f"[*] Connection Closed: {e}")
            break


async def main():
    """Start a server on a configured port"""
    async with websockets.serve(connect, "0.0.0.0", PORT):
        print(f"[*] Server Started on Port {PORT}")
        await asyncio.Future() # run forever


# Start the Server
if __name__ == "__main__":
    asyncio.run(main())

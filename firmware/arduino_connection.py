import serial
import time 
import threading

class ArduinoController:
    def __init__(self, port='COM5', baudrate=115200):  # enter port number
        self.port = port
        self.baudrate = baudrate
        self.ser = None
        self.is_connected = False

    def connect(self) -> bool:
        """Establishing connection to arduino"""
        try:
            self.ser = serial.Serial(self.port, self.baudrate, timeout=5)
            time.sleep(2)  # Wait for Arduino reset after connection
            self.is_connected = True
            print("Successfully connected to arduino.", flush=True)
            return True
        except serial.SerialException as e:
            print(f"Connection issue: {e}", flush=True)
            self.is_connected = False
            return False

    def send_angles(self, j1: float, j2: float, j3: float, callback=None):
        """Sending angle data to the arduino"""
        if not self.is_connected or not self.ser:
            print("Error: Arduino isn't connected", flush=True)
            return

        def _worker1():
            cmd = f"j1:{j1},j2:{j2},j3:{j3}\n"
            try:
                self.ser.write(cmd.encode('utf-8'))
                
                while True:
                    line = self.ser.readline().decode('utf-8', errors='ignore').strip()
                    if line == "OK":
                        print("Done moving.", flush=True)
                        if callback:
                            callback()
                        break
                    elif line.startswith("ERR"):
                        print(f"Arduino error: {line}", flush=True)
                        break
            except Exception as e:
                print(f"Error while transmitting data: {e}", flush=True)

        # Using separate thread to avoid GUI freezing
        threading.Thread(target=_worker1, daemon=True).start()

    def home(self, joint: str = "ALL", callback=None):
        if not self.is_connected or not self.ser:
            print("Error: Arduino isn't connected", flush=True)
            return

        def _worker2():
            cmd = f"HOME:{joint}\n"
            try:
                self.ser.write(cmd.encode('utf-8'))
                print(f"Started homing joint {joint}", flush=True)
                
                while True:
                    line = self.ser.readline().decode('utf-8', errors='ignore').strip()
                    if line == "OK":
                        print(f"Finished homing joint {joint}", flush=True)
                        if callback:
                            callback()
                        break
                    elif line.startswith("ERR"):
                        print(f"Homing error: {line}", flush=True)
                        break
            except Exception as e:
                print(f"Error while transmitting: {e}", flush=True)

        threading.Thread(target=_worker2, daemon=True).start()

    def disconnect(self):
        """Disconnects serial interface"""
        if self.ser and self.ser.is_open:
            self.ser.close()
            self.is_connected = False
            print("Disconnected.", flush=True)
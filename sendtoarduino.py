import serial
import time

ser = serial.Serial('COM3', 9600, timeout=1)


if ser.writable():
    print(ser.write(12))
    ser.write('31)
    
else:
    time.sleep(1)
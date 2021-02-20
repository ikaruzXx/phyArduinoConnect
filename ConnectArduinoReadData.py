import serial
import time

arduino = serial.Serial ('COM3', 9600.,timeout=0)

while input() != 's':
print (lectura)
arduino.close()

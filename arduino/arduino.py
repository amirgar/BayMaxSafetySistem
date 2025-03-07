import serial

def connect():
    ser = serial.Serial("COM7", 9600)
    print('Closing connection')

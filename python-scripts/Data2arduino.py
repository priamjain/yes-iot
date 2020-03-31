import serial
from firebase import firebase
arduino = serial.Serial('/dev/ttyACM0',9600);
firebase = firebase.FirebaseApplication('https://yes-iot.firebaseio.com')
while(1):
    result = firebase.get('/User1/D1', None)
    arduino.write(result.encode())

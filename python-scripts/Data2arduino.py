import serial
from firebase import firebase
#from firebase_admin import credentials
#from firebase_admin import db
#from firebase import firebase
firebase = firebase.FirebaseApplication('https://yes-iot.firebaseio.com')
result = firebase.get('/User1/D1', None)
print(result)
#default_app = firebase_admin.initialize_app()

import serial
import time
from flask import Flask
from flask import request
from flask import render_template
arduino = serial.Serial('/dev/ttyACM1',9600);
time.sleep(2)
app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template("my_form.html")

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form.getlist('cb')
    str1 = ''.join([str(elem) for elem in text])
    arduino.write(str1.encode())
    print(str1)
    return str1
if __name__ == '__main__':
    app.run()

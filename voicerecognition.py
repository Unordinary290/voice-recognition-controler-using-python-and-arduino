from telnetlib import DO
import speech_recognition as sr
import pyfirmata
from pyfirmata import Arduino, SERVO,  util
from time import sleep
import pyttsx3

port = 'COM5'
board = Arduino(port)
r = sr.Recognizer()
mic = sr.Microphone()

bluePin = 10
redPin = 11
pin = 9
fan = 8
rPin = 12
ePin = 13 

engine = pyttsx3.init()

def rotate(pin,angle):
    board.digital[pin].write(angle)
    sleep(0.1)

with mic as source:

        engine.say("Its David")
        print("Its David")
        engine.say("your home assistance")
        print("your home assistance")
        engine.say("To start any appliance give command ")
        print("To start any appliance give command")
        engine.say("first switch on light or switch off light")
        print("1. switch on light or switch off light")
        engine.say("second start red light")
        print("2. start red light")
        engine.say("third start blue light")
        print("3. start blue light")
        engine.say("Fourth Disco light")
        print("4. Disco light")
        engine.say("fifth open door or close door")
        print("5. open door or close door")
        engine.say("sixth Start motor")
        print("6. Start motor")
        engine.runAndWait()
        engine.say("And close assistance help Say close program")
        print("close program")
        engine.runAndWait()

while True:
  
    with mic as source:
        print("Listening ... .. .")
        audio = r.listen(source)
        
    try:
        command = r.recognize_google(audio)
        print(command)

    except sr.UnknownValueError:
        command = "Didn't catch sound for an internal error"
        engine.say(command)
        engine.runAndWait()

    command = command.lower()


    if "start blue light" in command:
        engine.say("Blue led is blinking")
        engine.runAndWait()
        board.digital[bluePin].write(1)
        sleep(3)
        board.digital[bluePin].write(0)
        engine.say("Blue led is closed")
        engine.runAndWait()
        

    if "switch on light" in command:
        board.digital[ePin].write(1)
        engine.say("light is on")
        engine.runAndWait()

    if "switch off light" in command:
        board.digital[ePin].write(0)
        engine.say("light is off")
        engine.runAndWait()


    if "start red light" in command:
        engine.say("Red led is blinking")
        engine.runAndWait()
        board.digital[redPin].write(1)
        sleep(10)
        board.digital[redPin].write(0)
        engine.say("Red led is closed")
        engine.runAndWait()
        
       

    if "open door" in command:
        engine.say("Door is opening")
        engine.runAndWait()
        board.digital[pin].mode=SERVO
        for i in range(0,90):
                    rotate(pin,i)

    if "start motor" in command:
        engine.say("Tank is filling")
        engine.runAndWait()
        board.digital[fan].write(1)
        sleep(7)
        board.digital[fan].write(0)
        engine.say("Tank is filled")
        engine.runAndWait()

    if "disco light" in command:
        engine.say("Disco light is on")
        engine.runAndWait()
        board.digital[rPin].write(1)
        sleep(4)
        board.digital[rPin].write(0)
        engine.say("Disco light is off")
        engine.runAndWait()

    if "close door" in command:
        board.digital[pin].mode=SERVO
        engine.say("Door is closed")
        engine.runAndWait()
        for i in range(100,-10):
                    rotate(pin,i)

    if "close program" in command:
        engine.say("program is closing")
        engine.runAndWait()
        break
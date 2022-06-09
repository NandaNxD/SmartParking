import RPi.GPIO as GPIO
import time
import os
from cloudconnect import Cloud
from ultrasonic import Ultrasonic
from led import Led
from camera import Camera
from licenseplate import LicensePlate
from buzzer import Buzzer

def cameraTest():
    c=Camera('image.jpg')
    c.capture()
    
def ultrasonicTest():
    print('Enter Trigger Pin Number')
    t=int(input())
    print('Enter Echo Pin Number')
    e=int(input())
    us=Ultrasonic(t,e)
    dis=us.getDistance()
    if(dis==-1):
        raise Exception('Ultrasonic Connection Loose')
    print('Distance'+dis)
    
def ledTest():
    print('Enter Led Pin Number')
    pin=int(input())
    led=Led(pin)
    led.turnOn()
    time.sleep(5)
    led.turnOff()
    
def servoTest():
    print('Enter Servo Pin Number')
    pin=int(input())
    factory = PiGPIOFactory()
    servo = Servo(pin, pin_factory=factory)
    servo=Servo(4)
    print("Start in the middle")
    servo.mid()
    sleep(1)
    print("Go to min")
    servo.min()
    sleep(1)
    print("Go to max")
    servo.max()
    sleep(1)
    print("And back to middle")
    servo.mid()
    sleep(0.1)
    servo.value = None
def buzzerTest():
    print('Enter Buzzer Pin number')
    pin=int(input())
    b=Buzzer(4)
    b.makeSound()
    time.sleep(1)
    b.stopSound()
    
def parkingPriceTest():
    p=calculate_parking_price(1,2,3)
    print(p)
    
def licensePlateTest():
    print('Enter image file name')
    fname=input()
    l=LicensePlate(fname)
    print(l.getLicensePlateNumber())

def cloudConnectTest():
    c=Cloud('smartparkingsystem-5ffb7-2f4717e68ead.json',AREA_ID='1',AREA_COORDINATES=[10,12])
    c.assignSlot(1,'KA')

if __name__ == '__main__':    
    GPIO.setmode(GPIO.BCM)
    while(True):
        time.sleep(3)
        os.system('clear')
        choice=0
        print('Enter the component to test')
        print('1: Camera 2: Ultrasonic')
        print('3: Led 4: Servo')
        print('5: Buzzer 6: ParkingPrice')
        print('7: LicensePlate 8: Cloud')
        print('9: ExitTest')
        try:
            choice=int(input())
        except:
            print('Input Error')
            time.sleep(3)
            os.system('clear')
            continue;
        if(choice==1):
            try:
                cameraTest()
            except:
                print('TestFailed')
                continue;
            print('TestPassed')
        elif(choice==2):
            try:
                ultrasonicTest()
            except:
                print('TestFailed')
                continue;
            print('TestPassed')
        elif(choice==3):
            try:
                ledTest()
            except:
                print('TestFailed')
                continue;
            print('TestPassed')
        elif(choice==4):
            try:
                servoTest()
            except:
                print('TestFailed')
                continue;
            print('TestPassed')
        elif(choice==5):
            try:
                buzzerTest()
            except:
                print('TestFailed')
                continue;
            print('TestPassed')
        elif(choice==6):
            try:
                parkingPriceTest()
            except:
                print('TestFailed')
                continue;
            print('TestPassed')
        elif(choice==7):
            try:
                licensePlateTest()
            except:
                print('TestFailed')
                continue;
            print('TestPassed')
        elif(choice==8):
            try:
                cloudTest()
            except:
                print('TestFailed')
                continue;
            print('TestPassed')
        elif(choice==9):
            exit()
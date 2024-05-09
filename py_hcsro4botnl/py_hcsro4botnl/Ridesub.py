
#dit is een subscriber node  om een robot met dc motors en hcsr04 distance sensor en  l298N in ROS2 (Iron_Irwini) Framework.

#nu importeert ROS2 library
import rclpy
from rclpy.node import Node

from std_msgs.msg import String                   # import strings.
from time import sleep # import sleep voor tijd.
from gpiozero import PWMOutputDevice # imports  gpiozero library  pwm (if yo dont have gpizero more info here https://gpiozero.readthedocs.io/en/latest/index.html# )
#now import the the board and the sensor library.  
import board #is nodig om de  adafruit_hcsr04  te gebruiken. als je geen circuitpython hebt of meer info wil hier is de link: https://learn.adafruit.com/welcome-to-circuitpython/what-is-circuitpython
import adafruit_hcsr04 # de sensor library (if you dont have it installed or need more info here is the link https://docs.circuitpython.org/projects/hcsr04/en/latest/index.html )
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D17, echo_pin=board.D4) # zet up de sensor sensor

# now we  setup the pwm output for l298N motor driver we using.#this is the enable pins

#this are the gpio pin setup for using L298N motor driver.
ena = PWMOutputDevice(14)
enb = PWMOutputDevice(25)
in1 = PWMOutputDevice(15)
in2 = PWMOutputDevice(18)

in3 = PWMOutputDevice(23)
in4 = PWMOutputDevice(24)
#this are the motor direction.
def stop():
    ena.value = 0
    enb.value = 0
    in1.value = 0
    in2.value = 0
    in3.value = 0
    in4.value = 0
def forward():
    
   
    ena.value = 1
    enb.value = 1
    in1.value = 1
    in2.value = 0
    in3.value = 1
    in4.value = 0
def backward():
    
    ena.value = 1
    enb.value = 1
    in1.value = 0
    in2.value = 1
    in3.value = 0
    in4.value = 1
def left():
    
   
    ena.value = 1
    enb.value = 1
    in1.value = 1
    in2.value = 0
    in3.value = 1
    in4.value = 0

def right():
    
    ena.value = 1
    enb.value = 1
    in1.value = 0
    in2.value = 1
    in3.value = 1
    in4.value = 0
    
      
       



   
class Ridesub(Node):
    def __init__(self):
        super().__init__('Robot_sub')
        self.subscription = self.create_subscription(
            String, 'robot',
        self.listener_callback,10,)
        self.subscription
      
   

    
    
    
    #now it listens to the publisher so that it can ride.
    def listener_callback(self,msg):  
        
        self.get_logger().info('I heard riding and distance cm is: : "%s"' % sonar.distance)
        if sonar.distance > 25 :
            forward()
            print("forward",sonar.distance,"cm")
            sleep(0.5)
        if sonar.distance< 10:
            backward()
            print("backward",sonar.distance,"cm")
            sleep(0.5)
        if sonar.distance < 25 and sonar.distance > 20 :
            left()
            print("left",sonar.distance,"cm")
            sleep(0.5)
        if sonar.distance < 20 and sonar.distance > 15:
            right()
            print("right",sonar.distance,"cm")
            sleep(0.5)
        if sonar.distance < 5 and sonar.distance > 1:
            stop()
            print("stop",sonar.distance,"cm")
            sleep(1)
            backward()
            print("right",sonar.distance,"cm")
            sleep(1)
        
    
        
    
      
      
      
      
      
def main(args=None):
    rclpy.init(args=args)

    ridesub = Ridesub()

    rclpy.spin(ridesub)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
   
   

if __name__ == '__main__':
    main()
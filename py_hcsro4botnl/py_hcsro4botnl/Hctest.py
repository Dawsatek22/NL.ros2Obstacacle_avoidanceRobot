#dit is een node om distance sensor te testen.
import rclpy
from rclpy.node import Node

from std_msgs.msg import String, Float64                      # CHANGE
from time import sleep
from gpiozero import PWMOutputDevice
import board
import adafruit_hcsr04


sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D17, echo_pin=board.D4) # setting up of the sensor pins


class SonarTest(Node):
  
  

    def __init__(self):
        super().__init__('sonartest')
        self.hctest_ = self.create_publisher(Float64,'sonar_testtopic',10)
        #self.stringtest_ = self.create_publisher(String,'sonar_string',10)
        timer_period = 0.5 # a seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0
        
    def timer_callback(self):
        Smsg = Float64()
        Smsg.data= (sonar.distance)
        self.hctest_.publish(Smsg)
        self.get_logger().info(  'cm "%s"' % Smsg.data ) # logs the sensor data

def main(args=None):
    rclpy.init(args=args)

    sonartest = SonarTest()

    rclpy.spin(sonartest)

    


if __name__ == '__main__':
    main()




        
    
   
       
  
        
                  

    
    
        
   
     
            
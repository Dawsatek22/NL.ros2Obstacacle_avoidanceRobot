#this is publisher node  to control a simple robot with dc motors and hcsr04 distance sensor and l298N in ROS2 (Iron_Irwini) Framework.

#import the  Ros2 library
import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class Ridepub(Node):

    def __init__(self):
        super().__init__('Robot_pub')
        self.publisher_ = self.create_publisher(String, 'robot', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = 'Hello robot: %d' % self.i
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1

    
def main(args=None):
    rclpy.init(args=args)

    ridepub = Ridepub()

    rclpy.spin(ridepub)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
   
    rclpy.shutdown()


if __name__ == '__main__':
    main()
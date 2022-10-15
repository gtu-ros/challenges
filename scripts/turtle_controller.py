#!/bin/python3

import math
import rospy
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from math import pow,atan2,sqrt
from my_robot_controller.msg import position



class triangle:
    
    def __init__(self):
        
        rospy.on_shutdown(self.cleanup)
        self.pub = rospy.Publisher("/turtle1/cmd_vel",Twist,queue_size=10)
        rospy.sleep(1)
        r = rospy.Rate(5.0)
        self.ptr = rospy.Publisher("draw_triangle",position,queue_size=10)
        prc = 0.0

        msg = position()        
        msg.message = "My position is: "
        msg.percent = prc
        length = 12
        while length > 11:
         length = int(input("Enter side length of triangle(it must be integer): "))
        
        t0 = rospy.Time.now().to_sec()
        #tft = rospy.get_param("cmd_vell") 
        #rospy.loginfo(tft)
        #rospy.set_param("cmd_vell",2.0)
        #rospy.loginfo(tft)  
        ct = 0.0

        while not rospy.is_shutdown():
            
            twist = Twist()
            twist.linear.x = 2.0
            t2 = rospy.Time.now().to_sec()
            
            
            for i in range(length):
                
                self.pub.publish(twist)
                t3 = rospy.Time.now().to_sec()
                ct = (t3-t2)*2
                
                if prc > 70:
                    prc = 0.0
                    rospy.loginfo("New Triangle has been started")
                    while length > 11:
                        t1 = rospy.Time.now().to_sec()
                        buf = (t1-t0) * 2
                        rospy.loginfo(buf)
                        length = int(input("Enter side length of triangle(it must be integer): "))
                        t0 = rospy.Time.now().to_sec()
                msg.percent = 33.33 + prc
                
                r.sleep()
                
            twist = Twist()
            twist.angular.z = math.pi* 120 / 360
            ct = 0.0
            for i in range(10):

                self.pub.publish(twist)
                r.sleep()
            
                
            self.ptr.publish(msg)    
            prc = prc+ 33.3
            length = 12
           

    def cleanup(self):
        twist = Twist()
        self.pub.publish(twist)



if __name__ == '__main__':
    rospy.init_node('draw_triangle')
    triangle()
#!/usr/bin/env python3

import rospy 
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from challenge1.msg import Completed
PI = 3.14159265358979

def rotate_turtle(distance,velocityPub):
    speed = rospy.get_param("speed")
       
    velc = Twist()
     
    velc.linear.x = 0
    velc.linear.y = 0
    velc.linear.z = 0
    velc.angular.x = 0
    velc.angular.y = 0
    velc.angular.z = speed #Giving the turtle an angular speed
     
    t0 = rospy.Time.now().to_sec()
    currentAngle = 0
    rotateAngle = 120*2*PI/360
     
    while(currentAngle <= rotateAngle):
        velocityPub.publish(velc)
        t1= rospy.Time.now().to_sec()
        currentAngle = speed * (t1-t0)
         
    velc.angular.z=0  # to avoid turtle moving more
    velocityPub.publish(velc)
     
 # END OF ROTATE_TURTLE FUNCTION
 
def percent(x):
    r = rospy.Rate(1)
    pub = rospy.Publisher('draw_percent', Completed, queue_size=10)
    msg = Completed()
    msg.Completed=x
    rospy.loginfo(msg)
    pub.publish(msg)
    r.sleep()
     
#END OF PERCENT FUNCTION

def draw_triangle(distance,velocityPub):
    

    velocity = Twist()
    for i in range(3):
        speed = float(rospy.get_param("speed"))
        velocity.linear.x = speed
        velocity.linear.y =0
        velocity.linear.z =0
        velocity.angular.x =0
        velocity.angular.y =0
        velocity.angular.z =0
      
        t0 = rospy.Time.now().to_sec()
        current_distance = 0
    
        while(current_distance <= distance):
            velocityPub.publish(velocity);
            t1 = rospy.Time.now().to_sec()
            
            current_distance = speed*(t1-t0)
            if(i==0):
                percent((current_distance)/(distance*3)*100)
            elif(i==1):
                percent(((current_distance)/(distance*3))*100+33.3)
            else:
                percent((current_distance)/(distance*3)*100+66.6)
            
            
        velocity.linear.x = 0
        
        velocityPub.publish(velocity)
        rotate_turtle(distance,velocityPub)
        
if __name__ == '__main__':
    rospy.init_node('draw_triangle', anonymous=True)
    velocityPub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    
    exit = False
    while not exit:
        try:
            print("Type 0 to exit\nEnter the side of triangle: ", end="")
            side_length = (input())
            side_length = float(side_length)
            if side_length == 0 :
                exit  = True
            else:
                draw_triangle(side_length,velocityPub)
        
        except rospy.ROSInterruptException:
            pass
    

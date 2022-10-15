#!/usr/bin/env python
from itertools import count
import rospy
from geometry_msgs.msg import Twist
from challenge.msg import Complated
import os
PI = 3.1415926535897

def move():

    # Starts a new node
    rospy.init_node('draw_triangle', anonymous=True)

    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    progress_publisher = rospy.Publisher("/challenge/draw_percent", Complated, queue_size=2)

    vel_msg = Twist()
    rate = rospy.Rate(5)
    
    speed = 5
    angle = 120
    angular_speed = 100*2*PI/360
    relative_angle = angle*2*PI/360
    counter = 0

    #enter to draw triangle
    while not rospy.is_shutdown():
        
        #get a lenght of triangle side 
        distance = input("Type your the lenght of triangle:")
        while not counter==3:
            vel_msg.linear.x = abs(speed)

            #Since we are moving just in x-axis
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0
            vel_msg.angular.x = 0
            vel_msg.angular.y = 0
            vel_msg.angular.z = 0
            

            #Setting the current time for distance calculus
            t0 = float(rospy.Time.now().to_sec())
            current_distance = 0
            

            #Loop to move the turtle in an specified distance
            while(current_distance < distance):
                #Publish the velocity
                velocity_publisher.publish(vel_msg)
                #Takes actual time to velocity calculus
                t1=float(rospy.Time.now().to_sec())
                #Calculates distancePoseStamped
                current_distance= speed*(t1-t0)

            #After drawing one side, stops the robot
            vel_msg.linear.x = 0

            counter += 1
            print(counter)
            #setting angular speed
            vel_msg.angular.z = abs(angular_speed)

            # Setting the current time for distance calculus
            t0 = rospy.Time.now().to_sec()
            current_angle = 0

            while(current_angle < relative_angle):
                velocity_publisher.publish(vel_msg)
                t1 = rospy.Time.now().to_sec()
                current_angle = angular_speed*(t1-t0)

            #Forcing our robot to stop
            vel_msg.angular.z = 0
            #Force the robot to stop
            velocity_publisher.publish(vel_msg)
            
        is_new_triangle = input("do you want to draw new triangle? (just type 'yes' or it will quit): ")
        
        if not is_new_triangle=="yes":
            os.system("rosnode kill "+ rospy.get_name()  + " /turtlesim")

                 
            

if __name__ == '__main__':
    try:
        #Testing our function
        move()
    except rospy.ROSInterruptException: pass
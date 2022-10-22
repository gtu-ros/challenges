#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 13:48:34 2022

@author: ilker
"""

import rospy 
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from challenge1.msg import Completed
import math



def percent(y):
	
	r=rospy.Rate(1)
	pub = rospy.Publisher('draw_percent', Completed, queue_size=10)
	msg = Completed()
	msg.Completed = y
	rospy.loginfo(msg)
	pub.publish(msg)
	r.sleep()
	
def rotate_turtle(distance):
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    speed=rospy.get_param("speed")
 
    
    speedAngle = 40*(speed*2*math.pi/360)
    vel = Twist()
    
    vel.linear.x = 0
    vel.linear.y = 0
    vel.linear.z = 0
    vel.angular.x = 0
    vel.angular.y = 0
    vel.angular.z = speedAngle
    
    t0 = rospy.Time.now().to_sec()
    currentAngle = 0
    rotateAngle = 120*2*math.pi/360
    
    while(currentAngle <= rotateAngle):
        pub.publish(vel)
        t1 = rospy.Time.now().to_sec()
        currentAngle = speedAngle * (t1-t0)
    
    vel.angular.z = 0
    pub.publish(vel)
    
     
    
    
    
def draw_triangle(distance):
    rospy.init_node('draw_triangle', anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rospy.Subscriber('/turtle1/pose',Pose)
    # rate = rospy.Rate(10)
    
    vel = Twist()
    r = 3
    for i in range(r):
        speed=rospy.get_param("speed")
        vel.linear.x = speed
        vel.linear.y = 0
        vel.linear.z = 0
        vel.angular.x = 0
        vel.angular.y = 0
        vel.angular.z = 0
        
        t0 = rospy.Time.now().to_sec()
        current_distance = 0
        
        while(current_distance <= distance):
            
            pub.publish(vel)
            t1=rospy.Time.now().to_sec()
            
            current_distance = speed*(t1-t0)
            if(i==0):
            	percent((current_distance)/(distance*3)*100)
            elif(i==1):
            	percent((current_distance)/(distance*3)*100+33.3)
            else:
            	percent((current_distance)/(distance*3)*100+66.6)
            
        vel.linear.x = 0
        pub.publish(vel)
        rotate_turtle(distance)
        
    
    
    


if __name__ == '__main__':
	flag = True
	while flag:
		try:
			speed = float(rospy.get_param("speed"))
		
			print("q => exit\nEnter side value : ", end="")
			distance = (input())
			if distance == 'q':
				flag = False
			else:
				distance = float(distance)
				draw_triangle(distance)
		except rospy.ROSInterruptException:
			pass
    
                
        

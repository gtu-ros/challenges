#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
import sys
from math import sqrt
import math
from turtlesim.msg import Pose
from challenge1.msg import Check_complete

a=0

#def draw_percent(percent):
#	rospy.init_node('draw_triangle', anonymous=True)
#	comp_pub = rospy.Publisher('draw_percent', Check_complete, queue_size=10)
#	rate = rospy.Rate(10)
#	
#	msg=Check_complete()
#	msg.completed=percent
#	global a
#	a=a+1
#	print(a)
#	rospy.loginfo(msg)
#	comp_pub.publish(msg)
#	rate.sleep()


mylist = [0.0, 0.0, 0.0]

def callback(Pose):
	mylist[0]=Pose.x
	mylist[1]=Pose.y
	mylist[2]=Pose.theta

def draw_triangle(length, speed):
	rospy.init_node('draw_triangle', anonymous=True)
	rospy.Subscriber("turtle1/pose", Pose, callback)
	vel_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
	rate = rospy.Rate(10)
	vel = Twist()
	
	percent=0
	
	vel.linear.x = speed
	vel.linear.y = 0
	vel.linear.z = 0
	
	vel.angular.x = 0
	vel.angular.y = 0
	vel.angular.z = 0

	while(mylist[0]<5.544445+length):
		vel_pub.publish(vel)
		#draw_percent(percent)
		
	vel.linear.x = 0
	vel.linear.y = 0
	vel.linear.z = 0
	
	vel.angular.x = 0
	vel.angular.y = 0
	vel.angular.z = speed
	
	while(mylist[2]<2*math.pi/3):
		vel_pub.publish(vel)
	
	vel.linear.x = speed
	vel.linear.y = 0
	vel.linear.z = 0
	
	vel.angular.x = 0
	vel.angular.y = 0
	vel.angular.z = 0
	while(mylist[0]>5.544445+(length/2) or mylist[1]<5.544445+(sqrt(3)*(length/2))):
		vel_pub.publish(vel)
		#draw_percent(percent)
		
	vel.linear.x = 0
	vel.linear.y = 0
	vel.linear.z = 0
	
	vel.angular.x = 0
	vel.angular.y = 0
	vel.angular.z = speed

	while(mylist[2]>0):
		vel_pub.publish(vel)
	while(mylist[2]<(-1)*2*math.pi/3):
		vel_pub.publish(vel)
	
	vel.linear.x = speed
	vel.linear.y = 0
	vel.linear.z = 0
	
	vel.angular.x = 0
	vel.angular.y = 0
	vel.angular.z = 0
	
	while(mylist[0]>5.544445 or mylist[1]>5.544445):
		vel_pub.publish(vel)
		#draw_percent(percent)
		
	vel.linear.x = 0
	vel.linear.y = 0
	vel.linear.z = 0
	
	vel.angular.x = 0
	vel.angular.y = 0
	vel.angular.z = speed
	while(mylist[2]<0):
		vel_pub.publish(vel)
		
	vel.linear.x = 0
	vel.linear.y = 0
	vel.linear.z = 0
	
	vel.angular.x = 0
	vel.angular.y = 0
	vel.angular.z = 0
	
	vel_pub.publish(vel)
	rate.sleep()

if __name__ == '__main__':
	try:
		length=int(input("Enter the length of side: "))
		#send speed with param
		draw_triangle(length, 3)
	except rospy.ROSInterruptException:
		pass

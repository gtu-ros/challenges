#!/usr/bin/env python

import rospy
from math import sqrt
from geometry_msgs.msg import Twist
import sys
from challenge_one.msg import Completed

def draw_percent(n):
	rospy.init_node('draw_triangle', anonymous=True)
	r = rospy.Rate(10) #10hz 
	
	pub = rospy.Publisher('draw_percent', Completed, queue_size=1)
	n *= 100
	
	msg = Completed()
	msg.completed = n

	rospy.loginfo(msg)
	pub.publish(msg)
	r.sleep()
		

def draw_triangle(l):
	rospy.init_node('draw_triangle', anonymous=True)
	pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
	rate = rospy.Rate(10)
	
	vel = Twist()
	side = sqrt(l*l)
	temp = 0
	filled = 0
	# half mid
	percentage = 0
	while temp < l/2:
		vel.linear.x = 0.3
		vel.linear.y = 0
		vel.linear.z = 0
		
		vel.angular.x = 0
		vel.angular.y = 0
		vel.angular.z = 0
		
		temp += 0.3
		
		pub.publish(vel)
		rate.sleep()
		
		filled += 0.3
		percentage = filled / (3 * l)
		draw_percent(percentage)
	temp = 0

	# right side
	while temp < side:
		kok_value = sqrt(3)
		vel.linear.x = -0.5
		vel.linear.y = 0.5*kok_value
		vel.linear.z = 0
		
		vel.angular.x = 0
		vel.angular.y = 0
		vel.angular.z = 0
		
		temp += sqrt(0.5*0.5 + 0.5*kok_value*0.5*kok_value)
		
		pub.publish(vel)
		rate.sleep()
		
		filled += sqrt(0.5*0.5 + 0.5*kok_value*0.5*kok_value)
		percentage = filled / (3 * l)
		draw_percent(percentage)
	temp = 0
	
	# left side
	while temp < side:
		kok_value = sqrt(3)
		vel.linear.x = -0.5
		vel.linear.y = -0.5*kok_value
		vel.linear.z = 0
		
		vel.angular.x = 0
		vel.angular.y = 0
		vel.angular.z = 0
		
		temp += sqrt(0.5*0.5 + 0.5*kok_value*0.5*kok_value)
		
		pub.publish(vel)
		rate.sleep()
		
		filled += sqrt(0.5*0.5 + 0.5*kok_value*0.5*kok_value)
		percentage = filled / (3 * l)
		draw_percent(percentage)
	temp = 0
	# half side of mid
	while temp < l/2:
		vel.linear.x = 0.3
		vel.linear.y = 0
		vel.linear.z = 0
		
		vel.angular.x = 0
		vel.angular.y = 0
		vel.angular.z = 0
		
		temp += 0.3
		
		pub.publish(vel)
		rate.sleep()
		
		filled += 0.3
		percentage = filled / (3 * l)
		draw_percent(percentage)
if __name__ == '__main__':
	flag = True
	while flag:
		try:
			print("q => exit\nEnter side value : ", end="")
			l = (input())
			if l == 'q':
				flag = False
			else:
				l = float(l)
				while l<5 or l>65:
					print("Please enter 5-65 numbers! ", end = "");
					l = float(input())
				draw_triangle(l)
		except rospy.ROSInterruptException:
			pass
		

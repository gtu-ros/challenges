#!/usr/bin/env python3

import rospy
from math import sqrt
from geometry_msgs.msg import Twist
import sys

def draw_triangle(l, speed):
	rospy.init_node('draw_triangle', anonymous=True)
	pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
	rate = rospy.Rate(10)
	
	vel = Twist()

	went = 0
	flag = 0
	
	while flag < 3: #her yon icin ayri ayri kural
		sensivity = 36
		piece = float(l/sensivity)
		vel.linear.x = 0
		vel.linear.y = 0
		vel.linear.z = 0

		vel.angular.x = 0
		vel.angular.y = 0
		vel.angular.z = 0
		drw = sqrt(3)
		if flag == 0: #saga dogru sadece x yonunde ilerliyor
			vel.linear.x = piece
			
		elif flag == 1: #sol uste dogru ilerleme
			
			vel.linear.x = -piece/2 
			vel.linear.y = drw*piece/2
			
		elif flag == 2: #ucgeni bitirme
			vel.linear.x = -piece/2
			vel.linear.y = -piece*drw/2
		
		for _ in range(sensivity):
			pub.publish(vel)
			rate.sleep()
			
		flag += 1
		
if __name__ == '__main__':

	speed = 1
	while 1:
		print("q => exit\nEnter side value : ", end="")
		lenn = input()
		if lenn=='q':
			break
		lenn = int(lenn)
		draw_triangle(lenn, speed)

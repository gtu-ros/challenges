#!/usr/bin/env python3
# GTU ROVER-ROS Challenge 1            
# Designed by: Müjgan OZAN          
# Date: 14/10/2022

import rospy
from geometry_msgs.msg import Twist
import math

def draw_side(speed, distance, vel, velocityPub):
	vel.linear.x = speed
	vel.linear.y = 0
	vel.linear.z = 0
	vel.angular.x = 0
	vel.angular.y = 0
	vel.angular.z = 0

	#Setting time to get distance calculation
	t0 = rospy.Time.now().to_sec()
	currentDistance = 0

	#Loop to move the turtle in distance
	while(currentDistance < distance):
		#Publish the velocity
		velocityPub.publish(vel)

		#Takes actual time to calculate velocity
		t1=rospy.Time.now().to_sec()

		#Calculates distance of turtle pose
		currentDistance = speed*(t1-t0)
    
	#Stops the turtle
	vel.linear.x = 0

	#Publish stop message
	velocityPub.publish(vel)

    
def rotate(vel, velocityPub, speed):
	speedAngle = (speed*2*math.pi/360)*15

	vel.linear.x = 0
	vel.linear.y = 0
	vel.linear.z = 0
	vel.angular.x = 0
	vel.angular.y = 0
	vel.angular.z = speedAngle

	t0 = rospy.Time.now().to_sec()
	currentAngle = 0
	rotateAngle = 120*2*math.pi/360 

	#Same loop as changing linear velocity, but applied to angular velocity instead
	while(currentAngle < rotateAngle):
		velocityPub.publish(vel)
		t1 = rospy.Time.now().to_sec()
		currentAngle = speedAngle * (t1 - t0)

	vel.angular.z = 0
	velocityPub.publish(vel)

def go_turtle():
	# Starts a new node
	rospy.init_node("turtlemove", anonymous=True)
	velocityPub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
	vel = Twist()

	#Receiveing the user's input and setting parameters
	speed = rospy.get_param("turtle_speed");
	distance = float(input("Please enter the distance you want:"))

	#drawing triangle 
	while not rospy.is_shutdown():
		draw_side(speed, distance, vel, velocityPub)
		rotate(vel, velocityPub, speed)
		draw_side(speed, distance, vel, velocityPub)
		rotate(vel, velocityPub, speed)
		draw_side(speed, distance, vel, velocityPub)
		
		break

if __name__ == '__main__':
	try:
		go_turtle()
		while input("Enter -365 to exit, any other key to continue:  ") != "-365":
			go_turtle()
        
	except rospy.ROSInterruptException: 
		pass
#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import pow, atan2, sqrt, sin, cos, pi
from challenge1.msg import Challenge

locationx = 0.0
locationy = 0.0
asd = 0
pub = rospy.Publisher('draw_percent', Challenge, queue_size=10)

def rastgele(data): # This func takes positions of turtle and assign it global location variables
	#rospy.loginfo(data)
	global locationx
	locationx = data.x
	global locationy
	locationy = data.y

def percentage(percent): #This func takes percantage and it publish percantage message to node called "draw_percent"
	percent = percent * 100
	global asd
	#slp = rospy.Rate(0.5)
	#if(asd%9900 == 0):
	print(asd)
	msg = Challenge()
	msg.completed=percent
	rospy.loginfo(msg)
	pub.publish(msg)
	#slp.sleep()
	asd = asd + 1

def move():
	global locationx
	global locationy
	rospy.init_node('draw_triangle', anonymous=True) #it creates a new and called with a name unique.
	velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
	pose_sub = rospy.Subscriber('/turtle1/pose', Pose, rastgele) #It takes positions of turtle and send it rastgele func as parameter
	vel_msg = Twist()
	pose = Pose()
	
	#speed = 1
	speed = rospy.get_param("turtle_speed")
	while True:
		cont_or_exit = int(input("Enter 1 to continue drawing, enter 2 to exit "))
		if cont_or_exit == 1:
			speed = 1
			length_of_side = float(input("Please enter length side of triangle: "))
			i = 0.0
			while(i < 3.0): # For each side loop goes 1 times
				#İNİTİALİZİNG OF VELOCİTİES
				vel_msg.linear.x = abs(speed)
				vel_msg.linear.y = 0
				vel_msg.linear.z = 0
				vel_msg.angular.x = 0
				vel_msg.angular.y = 0
				vel_msg.angular.z = 0
				
				#positions of corner points
				current_x = locationx
				current_y = locationy
				
				#I controlled the distance between turtle and corner point
				current_len = sqrt(pow((locationx - current_x),2) + pow((locationy - current_y),2))
				#t0 = rospy.Time.now().to_sec()
				print(i)
				while(current_len < length_of_side):# when the distance between turtle and corner point equals to length it stops
					velocity_publisher.publish(vel_msg) #It publish velocity
					#print("inin değeri")
					#print(float(i))
					percent = (i*length_of_side + current_len)/(3*length_of_side) #It calculates percantage  of distance traveled
					percentage(percent)
					
					#t1 = rospy.Time.now().to_sec()
					#current_len = speed * (t1 - t0)
					current_len = sqrt(pow((locationx - current_x),2) + pow((locationy - current_y),2))
					
				
				vel_msg.linear.x = 0 #It is zero because while changing angular_vel turtle should not move linearly
				vel_msg.angular.z = 120 * pi / 180
				velocity_publisher.publish(vel_msg)  
				i = i + 1
				slp = rospy.Rate(1)#This is for turning
				slp.sleep()
		elif(cont_or_exit == 2): # This is exit statement
			break
	

if __name__ == '__main__':
	try:
	    #Testing our function
	    move()
	except rospy.ROSInterruptException: 
	    pass

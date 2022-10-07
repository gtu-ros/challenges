#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from std_msgs.msg import String
from challange1.msg import Completed
PI = 3.1415926535897

def percent(y):
    rospy.init_node('draw_Triangle', anonymous=True)
    r = rospy.Rate(1)
    pub = rospy.Publisher('draw_percent', Completed, queue_size=10)
    msg = Completed()
    msg.Completed=y
    rospy.loginfo(msg)
    pub.publish(msg)
    r.sleep()

def draw_triangle():
    rospy.init_node('draw_Triangle', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()
    rospy.Subscriber('/turtle1/pose',Pose)
    while True:
    	choose=input("1-New triangle\n2-Exit\nYour choose:")
        if(choose==2):
	    break
        elif(choose==1):
	    print("\nLet's move your robot")
            angular_speed = 5*PI/3
            relative_angle = 2*PI/3
            #speed = rospy.get_param("speed") ###
            distance = input("Type your distance:")
	    if(distance>5.5):
		print("distance is high")
	        print("\n")
	    elif(distance<=0):
		print("Invalid distance")
	        print("\n")
	    else:
                for i in range(0,3):
                    vel_msg.linear.y = 0
                    vel_msg.linear.z = 0
                    vel_msg.angular.x = 0
                    vel_msg.angular.y = 0
                    vel_msg.angular.z = 0
                    speed = rospy.get_param("speed") ###
                    #vel_msg.linear.x = abs(speed)

                    current_distance = 0
                    t0 = rospy.Time.now().to_sec()
                    while(current_distance < distance):
                        velocity_publisher.publish(vel_msg)
                        t1=rospy.Time.now().to_sec()
                        vel_msg.linear.x = abs(speed)
                        current_distance= speed*(t1-t0)
                        if(i==0):
                            percent((current_distance)/(distance*3)*100)
                        elif(i==1):
                            percent(((current_distance)/(distance*3))*100+33.3)
                        else:
                            percent((current_distance)/(distance*3)*100+66.6)
                    vel_msg.linear.x = 0
                    velocity_publisher.publish(vel_msg)

                    t2 = rospy.Time.now().to_sec()
                    current_angle = 0
                    vel_msg.angular.z=abs(angular_speed)
                    while(current_angle < relative_angle):
                        velocity_publisher.publish(vel_msg)
                        t3 = rospy.Time.now().to_sec()
                        current_angle = angular_speed*(t3-t2)
                    vel_msg.angular.z = 0
                    velocity_publisher.publish(vel_msg)
		print("\n")
	else:
	    print("Invalid value\n")

if __name__ == '__main__':
    try:
        draw_triangle()
    except rospy.ROSInterruptException:
        pass

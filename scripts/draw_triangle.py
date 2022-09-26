#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
#from challenge1.msg import Progress

PI = 3.14


class MyTurtle:
    def __init__(self):
        rospy.init_node("draw_triangle", anonymous=True)

        self.velocity_pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
        self.vel = Twist()
        self.rate = rospy.Rate(10)

    def update_vel(self, is_angular, is_linear, velocity, distance):
        if is_linear:
            # If turtle is to draw a side, it only has linear velocity
            self.vel.linear.x = velocity
            self.vel.linear.y = 0.0
            self.vel.linear.z = 0.0
            self.vel.angular.x = 0.0
            self.vel.angular.y = 0.0
            self.vel.angular.z = 0.0

            distance_taken = 0
            t0 = rospy.Time.now().to_sec()
            while distance > distance_taken:
                self.velocity_pub.publish(self.vel)
                t1 = rospy.Time.now().to_sec()
                distance_taken = velocity * (t1 - t0)
            self.vel.linear.x = 0  # Stop the turtle

        if is_angular:
            # If turtle is on a corner, turn 120 degrees to draw the next side
            current_angle = 0.0
            angular_speed = velocity * 2 * PI / 360
            relative_angle = 120 * 2 * PI / 360  # Equaliteral triangle
            self.vel.linear.x = 0.0
            self.vel.linear.y = 0.0
            self.vel.linear.z = 0.0
            self.vel.angular.x = 0.0
            self.vel.angular.y = 0.0
            self.vel.angular.z = angular_speed

            t0 = rospy.Time.now().to_sec()
            while relative_angle > current_angle:
                self.velocity_pub.publish(self.vel)
                t1 = rospy.Time.now().to_sec()
                current_angle = angular_speed * (t1 - t0)
            self.vel.angular.z = 0  # Stop the turtle

        self.velocity_pub.publish(self.vel)  # Publish the stop message

    def draw(self):
        while not rospy.is_shutdown():
            side_length = float(input("Enter side length: "))
            if side_length > 0.0:
                self.update_vel(False, True, 1, side_length)
                self.update_vel(True, False, 20, 0)
                self.update_vel(False, True, 1, side_length)
                self.update_vel(True, False, 20, 0)
                self.update_vel(False, True, 1, side_length)
            break


if __name__ == "__main__":
    try:
        turtle = MyTurtle()
        turtle.draw()
    except rospy.ROSInterruptException:
        pass

#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
import math
from challenge1.msg import Progress


class Turtle:
    def __init__(self):
        rospy.init_node("draw_triangle", anonymous=True)

        self.velocity_pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
        self.vel = Twist()
        self.rate = rospy.Rate(10)
        self.progress_pub = rospy.Publisher(
            "/challenge1/draw_percent", Progress, queue_size=2
        )

    def update_progress(self, percentage, line_number):
        rate = rospy.Rate(1)

        progress = Progress()
        progress.completed = percentage / 3 + 100 / 3 * (line_number - 1)

        rospy.loginfo(f"Completed {int(progress.completed)}%")
        self.progress_pub.publish(progress.completed)
        rate.sleep()

    def update_vel(self, is_angular, is_linear, velocity, distance, line_number):
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
                # distance_taken -> distance**3 x percentage -> 100; 100*distance_taken/distance*3
                percentage = 100 * distance_taken / distance
                self.update_progress(percentage, line_number)
            self.vel.linear.x = 0  # Stop the turtle

        if is_angular:
            # If turtle is on a corner, turn 120 degrees to draw the next side
            current_angle = 0.0
            angular_speed = velocity * 2 * math.pi / 360
            relative_angle = 120 * 2 * math.pi / 360  # Equaliteral triangle
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
                self.update_vel(False, True, 1, side_length, 1)
                self.update_vel(True, False, 20, 0, 0)
                self.update_vel(False, True, 1, side_length, 2)
                self.update_vel(True, False, 20, 0, 0)
                self.update_vel(False, True, 1, side_length, 3)
            break


if __name__ == "__main__":
    try:
        turtle = Turtle()
        turtle.draw()
        while input("Enter -1 to exit, any other key to continue: ") != "-1":
            turtle.draw()

    except rospy.ROSInterruptException:
        pass

#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math

TOLERANCE = 0.1


def init_movement(diff):

    vel_msg = Twist()

    vel_msg.linear.x = TOLERANCE
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0
    return vel_msg


class TurtleBot:
    def __init__(self):

        rospy.init_node('turtlebot_controller', anonymous=True)
        self.velocity_publisher = rospy.Publisher('/turtle1/cmd_vel',
                                                  Twist,
                                                  queue_size=10)
        self.pose_subscriber = rospy.Subscriber('/turtle1/pose', Pose,
                                                self.update_pose)

        self.pose = Pose()
        self.rate = rospy.Rate(10)

    def update_pose(self, data):
        self.pose = data
        self.pose.x = round(self.pose.x, 2)
        self.pose.y = round(self.pose.y, 2)

    def init_rotation(self, diff_y):
        vel_msg = Twist()

        vel_msg.linear.x = 0
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        # to find out fastest rotation
        vel_msg.angular.z = TOLERANCE
        if (diff_y > 0):
            vel_msg.angular.z = TOLERANCE
        else:
            vel_msg.angular.z = -TOLERANCE
        return vel_msg

    def correctAngle(self, diff):
        return abs(self.pose.theta - diff.theta) < TOLERANCE

    def isReached(self, distance):
        x = 5.54 - abs(self.pose.x)
        y = 5.54 - abs(self.pose.y)

        d = math.sqrt(x * x + y * y)

        return (d > distance)

    def move2goal(self):
        goal_pose = Pose()
        diff = Pose()

        goal_pose.x = float(input("Set your x goal: "))
        goal_pose.y = float(input("Set your y goal: "))

        self.rate.sleep()
        diff.x = goal_pose.x - self.pose.x
        diff.y = goal_pose.y - self.pose.y
        diff.theta = math.atan(diff.y / diff.x)
        if (diff.x < 0):
            if (diff.y > 0):
                diff.theta = math.pi + diff.theta
            else:
                diff.theta = -math.pi + diff.theta

        print(diff)

        vel_msg = self.init_rotation(diff.y)

        # rotates until finds correct angle to move
        while not self.correctAngle(diff):
            self.rate.sleep()

            print("x: ", self.pose.x)
            print("y: ", self.pose.y)
            print("theta: ", self.pose.theta)

            self.velocity_publisher.publish(vel_msg)

            self.rate.sleep()

        # move euclidian distance
        vel_msg = init_movement(diff)

        distance = math.sqrt(diff.x * diff.x + diff.y * diff.y)

        while not self.isReached(distance):
            self.rate.sleep()

            print("x: ", self.pose.x)
            print("y: ", self.pose.y)
            print("theta: ", self.pose.theta)

            self.velocity_publisher.publish(vel_msg)

            self.rate.sleep()

        rospy.spin()


if __name__ == '__main__':

    try:
        x = TurtleBot()
        x.move2goal()
    except rospy.ROSInterruptException:
        pass

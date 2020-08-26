#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math


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

    def init_rotation(self, goal_pose_y):
        vel_msg = Twist()

        vel_msg.linear.x = 0
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        # to find out fastest rotation
        if (goal_pose_y > 0):
            vel_msg.angular.z = 0.1
        else:
            vel_msg.angular.z = -0.1
        return vel_msg

    def move2goal(self):
        goal_pose = Pose()

        # goal_pose.x = input("Set your x goal: ")
        # goal_pose.y = input("Set your y goal: ")

        goal_pose.x = 4
        goal_pose.y = 3
        goal_pose.theta = math.atan(goal_pose.y / goal_pose.x)
        print(goal_pose)

        vel_msg = self.init_rotation(goal_pose.y)

        # rotates until finds correct angle to move
        while self.pose.theta < goal_pose.theta:
            self.rate.sleep()

            print("x: ", self.pose.x)
            print("y: ", self.pose.y)
            print("theta: ", self.pose.theta)

            self.velocity_publisher.publish(vel_msg)

            self.rate.sleep()

        # TODO
        # move euclidian distance

        rospy.spin()


if __name__ == '__main__':

    try:
        x = TurtleBot()
        x.move2goal()
    except rospy.ROSInterruptException:
        pass

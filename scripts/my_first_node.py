#!/bin/python3
from ast import IsNot
import rospy 


if __name__ == '__main__':
    rospy.init_node("test_node")

    rospy.loginfo("This node has beeen started.")

    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        rospy.loginfo("Hi")
        rate.sleep()
  
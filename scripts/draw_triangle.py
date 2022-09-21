#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from challenge1.msg import Progress


def draw():
    rospy.init_node("draw_triangle", anonymous=True)
    pub = rospy.Publisher("draw_percent", Progress, queue_size=10)

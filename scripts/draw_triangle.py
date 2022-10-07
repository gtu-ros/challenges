from tabnanny import check
import rospy
from geometry_msgs.msg  import Twist
from turtlesim.msg import Pose
from math import pow,atan2,sqrt
PI = 3.1415926535897

class turtlebot():

    def __init__(self):
        #Creating our node,publisher and subscriber
        rospy.init_node('turtlebot_controller', anonymous=True)
        self.velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        self.pose_subscriber = rospy.Subscriber('/turtle1/pose', Pose, self.callback)
        self.pose = Pose()
        self.rate = rospy.Rate(10)
        self.speed=1

    #Callback function implementing the pose value received
    def callback(self, data):
        self.pose = data
        self.pose.x = round(self.pose.x, 4)
        self.pose.y = round(self.pose.y, 4)

    def move_in_line(self,side_length):
        vel_msg = Twist()
        vel_msg.linear.x = self.speed
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = 0

        t0 = rospy.Time.now().to_sec()
        distance_travelled = 0

        while distance_travelled < side_length:
            self.velocity_publisher.publish(vel_msg)
            t1 = rospy.Time.now().to_sec()
            distance_travelled = self.speed*(t1-t0)

        vel_msg.linear.x = 0
        self.velocity_publisher.publish(vel_msg)
    def rotate(self):
        vel_msg=Twist()
        vel_msg.angular.z = self.speed
        t0	= rospy.Time.now().to_sec()
        angle_travelled = 0

        while ( angle_travelled < PI*(2/3) ):
            self.velocity_publisher.publish(vel_msg)
            t1 = rospy.Time.now().to_sec()
            angle_travelled = self.speed*(t1-t0)

        vel_msg.angular.z = 0
        self.velocity_publisher.publish(vel_msg)
    def final(self):
        a=float(input("Give a number:"))
        x = turtlebot()
        for i in range(3):
            x.move_in_line(a)
            x.rotate()
        
        kontrol=str(input("close ---> 'q' ,'Q' or shutdown to rospy \n continue ---> Press any key except 'q'\n Press key:"))
        a=kontrol=="q" or kontrol=="Q"
        if a==False:
            x = turtlebot()
            x.final()
        else:
            quit()

if __name__ == '__main__':
    try:
        #Testing our function
        x = turtlebot()
        x.final()
        

    except rospy.ROSInterruptException: pass

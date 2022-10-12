
import rospy
from geometry_msgs.msg  import Twist
from turtlesim.msg import Pose
from challenges.msg import Completed
PI = 3.1415926535897

class turtlebot():

    def __init__(self):
        #Creating our node,publisher and subscriber
        rospy.init_node('draw_triangle', anonymous=True)
        self.velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        self.progress_publisher = rospy.Publisher("/challenge/draw_percent", Completed, queue_size=10)
        self.pose_subscriber = rospy.Subscriber('/turtle1/pose', Pose)
        self.pose = Pose()
        self.rate = rospy.Rate(10)
        self.speed=rospy.get_param("turtle_speed")
        self.percent=Completed()

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
        self.percent.completed=0
        self.progress_publisher.publish(self.percent)
        self.velocity_publisher.publish(vel_msg)
    def rotate(self):
        vel_msg=Twist()
        vel_msg.angular.z = self.speed
        t0= rospy.Time.now().to_sec()
        angle_travelled = 0

        while ( angle_travelled < PI*(2/3) ):
            self.velocity_publisher.publish(vel_msg)
            t1 = rospy.Time.now().to_sec()
            angle_travelled = self.speed*(t1-t0)

        vel_msg.angular.z = 0
        self.velocity_publisher.publish(vel_msg)
    def move_turtle(self):
        a=float(input("Length:"))
        x = turtlebot()
        for i in range(3):
            x.move_in_line(a)
            x.rotate()
        
        kontrol=str(input('if you want to draw a new triangle, press the "Y" key. If you want to exit, press any key other than "Y".'))
        a=kontrol=="y" or kontrol=="Y"
        if a==True:
            x = turtlebot()
            x.move_turtle()
        else:
            quit()

if __name__ == '__main__':
    try:
        #Testing our function
        x = turtlebot()
        x.move_turtle()
        

    except rospy.ROSInterruptException: pass


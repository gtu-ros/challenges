
//What percentage of the triangle is complete is calculated incorrectly.
//Even though I created the draw_percent topic, I can't publish the message to it continuously because I couldn't put that part inside the loop.
//If I am being wanted to draw a second triangle, I try to change the direction of the turtle back to its original direction. But this rotation process is not perfect for some reason that I don't understand. Therefore, there may be shifts in the triangle drawings after the first triangle.



 #include <boost/bind/bind.hpp>
 #include <ros/ros.h>
 #include <turtlesim/Pose.h>
 #include <geometry_msgs/Twist.h>
 #include <std_srvs/Empty.h>
 #include <stdlib.h>
 #include <cmath>
 #include <std_msgs/String.h>
 #include <sstream>
//#include "std_msgs/Float64.h"
//#include "std_msgs/Float32.h"
 #include "challenges/Num.h"
 
 using namespace std;
  
 turtlesim::PoseConstPtr g_pose;
 turtlesim::Pose g_goal;
 

 int count1=0;
 float length;
 float rate=0;  //yüzde kaçı tamamlandı öğrenme amacıyla
  
 enum State
 {
   FORWARD,
   STOP_FORWARD,
   TURN,
   STOP_TURN,
 };
  
 State g_state = FORWARD;
 State g_last_state = FORWARD;
 bool g_first_goal_set = false;
  
 #define PI 3.141592


void rotate (double angular_speed, double relative_angle, bool clockwise, ros::Publisher twist_pub); 

//void percent(ros::NodeHandle nh);
void percent();
  
 void poseCallback(const turtlesim::PoseConstPtr& pose)
 {
   g_pose = pose;
 }
  
 bool hasReachedGoal()
 {
   return fabsf(g_pose->x - g_goal.x) < 0.1 && fabsf(g_pose->y - g_goal.y) < 0.2 && fabsf(g_pose->theta - g_goal.theta) < 0.01;
 }
  
 bool hasStopped()
 {
   return g_pose->angular_velocity < 0.0001 && g_pose->linear_velocity < 0.0001;
 }
  
 void printGoal()
 {
   ROS_INFO("New goal [%f %f, %f]", g_goal.x, g_goal.y, g_goal.theta);
 }
  
 void commandTurtle(ros::Publisher twist_pub, float linear, float angular)
 {
   geometry_msgs::Twist twist;
   twist.linear.x = linear;
   twist.angular.z = angular;
   twist_pub.publish(twist);
 }
  
 void stopForward(ros::Publisher twist_pub)
 {
   if (hasStopped())
   {
     count1++; //2 oldu. 4 oldu
     ROS_INFO("Reached goal");
     g_state = TURN;
     g_goal.x = g_pose->x;
     g_goal.y = g_pose->y;
     if(count1 == 2) g_goal.theta = 2.0943951;
     if(count1 == 4) g_goal.theta = 4.18879;
     // wrap g_goal.theta to [-pi, pi)
     if (g_goal.theta >= PI) g_goal.theta -= 2 * PI;
     printGoal();
   }
   else
   {
     commandTurtle(twist_pub, 0, 0);
   }
 }
  
 void stopTurn(ros::Publisher twist_pub)
 {
   if (hasStopped())
   {
     ROS_INFO("Reached goal");
     count1++; //3 oldu.
     g_state = FORWARD;
     if(count1 == 3){
        g_goal.x = g_pose->x - length/2.0;
        g_goal.y = (length*(sqrt(3)/2.0)) + g_pose->y;
        g_goal.theta = g_pose->theta;
     }

     if(count1 == 5){
        g_goal.x = g_pose->x - length/2.0;
        g_goal.y =  g_pose->y - (length*(sqrt(3)/2.0)) ;
        g_goal.theta = g_pose->theta;
        
     }     
     
     printGoal();
   }
   else
   {
     commandTurtle(twist_pub, 0, 0);
   }
 }
  
  
 void forward(ros::Publisher twist_pub)
 {
   if (hasReachedGoal())
   {
   //if(count1 == 5) cerr<<endl<<"fonk forward hasreachedgoal";
     g_state = STOP_FORWARD;
     commandTurtle(twist_pub, 0, 0);
   }
   else
   {
     commandTurtle(twist_pub, 1.0, 0.0);  //neden 1.0 ???
   }
 }
  
 void turn(ros::Publisher twist_pub)
 {
   if (hasReachedGoal())
   {
     g_state = STOP_TURN;
     commandTurtle(twist_pub, 0, 0);
   }
   else
   {
     commandTurtle(twist_pub, 0.0, 0.4);  //buradaki 0.4'ü değişmek gerekebilir. ???
   }
 }
  
 void timerCallback(const ros::TimerEvent&, ros::Publisher twist_pub)
 //void timerCallback(ros::Publisher twist_pub)
 {
      
   percent();
   
   if(count1> 6){ 
      
      while(1){
         cout<<endl<<"If you want to exit, enter 0. If you want to draw a new triangle, please enter the side length: ";
         cin>>length;
         if(length <= 5.3) break;
         else cout<<endl<<"You can't enter the number greater than 5.3";      
      }
      
      if(length == 0) exit(0);
      
      else{ 
         cout<<endl<<"Buraya giriyor1";
         count1 = 0; 
         g_first_goal_set=false;  
         //rotate(2.09, 2.09, 0,twist_pub);
         rotate(2.0943951, 2.0943951, 0,twist_pub);
         //commandTurtle(twist_pub, 0.0, 2.09);
         //commandTurtle(twist_pub, 0, 0); 
      } 
   }
   
   
   
     
   if (!g_pose)
   {
     return;
   }
  
   if (!g_first_goal_set)
   {

     g_first_goal_set = true;
     g_state = FORWARD;
     g_goal.x = length + g_pose->x;
     g_goal.y =  g_pose->y;
     g_goal.theta = g_pose->theta;
     printGoal();
     count1++;

   }
  
   if (g_state == FORWARD)
   {

     forward(twist_pub);
     
   }
   else if (g_state == STOP_FORWARD)
   {
     stopForward(twist_pub);
   }
   else if (g_state == TURN)
   {
     turn(twist_pub);
   }
   else if (g_state == STOP_TURN)
   {
     stopTurn(twist_pub);
   }
 }
  
 int main(int argc, char** argv)
 {
 
   
   while(1){
   cout<<endl<<"Enter the side length(If you want to exit,press 0): "; 
   cin>>length;   
   
      if(length <= 5.3) break;
      else cout<<endl<<"You can't enter the number greater than 5.3";
   }
   ros::init(argc, argv, "draw_triangle");
   ros::NodeHandle nh;
   //percent(nh);
   ros::Subscriber pose_sub = nh.subscribe("turtle1/pose", 1, poseCallback);
   ros::Publisher twist_pub = nh.advertise<geometry_msgs::Twist>("turtle1/cmd_vel", 1);
   ros::ServiceClient reset = nh.serviceClient<std_srvs::Empty>("reset");
   ros::Timer timer = nh.createTimer(ros::Duration(0.016), boost::bind(timerCallback, boost::placeholders::_1, twist_pub));
   
   /*
   while(1){
      //timerCallback(boost::placeholders::_1, twist_pub);

   ros::Subscriber pose_sub = nh.subscribe("turtle1/pose", 1, poseCallback);
   ros::Publisher twist_pub = nh.advertise<geometry_msgs::Twist>("turtle1/cmd_vel", 1);
   ros::ServiceClient reset = nh.serviceClient<std_srvs::Empty>("reset");     
         timerCallback(twist_pub); 
            std_srvs::Empty empty;
   reset.call(empty);
   }
   */
   
   //cout<<endl<<"La girsene";
   //percent(nh);
   
   std_srvs::Empty empty;
   reset.call(empty);

   
   
   //percent();
   ros::Publisher pub2 = nh.advertise<challenges::Num>("draw_percent", 1);
   //ros::Rate rateHandler = ros::Rate(2);
   challenges::Num vrb;
   vrb.completed.data = rate;
   pub2.publish(vrb);  
   
   
   /*
   percent();
   ros::Publisher pub2 = nh.advertise<std_msgs::Float32>("draw_percent", 1);
   //std_msgs::message vrb(new std_msgs::Float32);
   //std_msgs::float32 vrb;
   std_msgs::Float32 vrb;
   //str->data = "hello world";
   vrb.data = rate;
   pub2.publish(vrb);   
   */
   
   /*
   percent();
   ros::Publisher publishingObj = nh.advertise<std_msgs::Float64>("floating_numbers", 2);
   ros::Rate rateHandler = ros::Rate(2);
   std_msgs::Float64 pubMsg;
   pubMsg.data = rate;
   publishingObj.publish(pubMsg);
   */  
   
   /*
   ros::Publisher pub = nh.advertise<std_msgs::String>("topic_name", 5);
   std_msgs::String str;
   str.data = "hello world";
   pub.publish(str);
   */
  
   ros::spin();
 }   




void rotate (double angular_speed, double relative_angle, bool clockwise, ros::Publisher twist_pub){

	//geometry_msgs::Twist vel_msg;
	//set a random linear velocity in the x-axis
	geometry_msgs::Twist twist;
	
	twist.linear.x =0;
	twist.linear.y =0;
	twist.linear.z =0;
	//set a random angular velocity in the y-axis
	twist.angular.x = 0;
	twist.angular.y = 0;
	if (clockwise)
		twist.angular.z =-abs(angular_speed);
	else
		twist.angular.z =abs(angular_speed);

	double t0 = ros::Time::now().toSec();
	double current_angle = 0.0;
	ros::Rate loop_rate(1000);
	do{
		//velocity_publisher.publish(twist);
		twist_pub.publish(twist);
		double t1 = ros::Time::now().toSec();
		current_angle = angular_speed * (t1-t0);
		ros::spinOnce();
		loop_rate.sleep();
		//cout<<(t1-t0)<<", "<<current_angle <<", "<<relative_angle<<endl;
	}while(current_angle<relative_angle);

	//force the robot to stop when it reaches the desired angle
	twist.angular.z =0;
	//velocity_publisher.publish(twist);
	twist_pub.publish(twist);
} 

//void percent(ros::NodeHandle nh){
void percent(){

//g_pose->x - g_goal.x
   float remaining;

   if(count1 == 1){
     remaining= g_goal.x-g_pose->x;
     rate = ((length-remaining)/length)*(100/3.0);
   }
   
   else if(count1 == 3){
      //remaining= (g_pose->x-g_goal.x)
      remaining= (g_goal.y - g_pose ->y)*(2.0/sqrt(3));
      //cout<<endl<<"(g_goal.y - g_pose ->y): "<<(g_goal.y - g_pose ->y)<<" (2.0/sqrt(3)): "<< (2.0/sqrt(3)); 
      //cout<<endl<<"Remaining in count 3: "<<remaining;
      //cout<<endl<<"((length-remaining)/length)*(100/3.0): "<<((length-remaining)/length)*(100/3.0);
      rate=34+ ((length-remaining)/length)*(100/3.0);
   }
   
   else if(count1 == 5){
      remaining= (g_pose->y - g_goal.y)*(2.0/sqrt(3));
      //cout<<endl<<"(g_pose->y - g_goal.y): "<<(g_pose->y - g_goal.y)<<" (2.0/sqrt(3)): "<< (2.0/sqrt(3)); 
      //cout<<endl<<"Remaining in count 5: "<<remaining;
      rate=67+ ((length-remaining)/length)*(100/3.0);
   }
   
   //cout<<endl<<"Tamamlanan: "<<rate;

/*
   //percent();
   ros::Publisher pub2 = nh.advertise<challenges::Num>("draw_percent", 1);
   //std_msgs::message vrb(new std_msgs::Float32);
   //std_msgs::float32 vrb;
   challenges::Num vrb;
   //str->data = "hello world";
   vrb.completed.data = rate;
   pub2.publish(vrb);  
   */  

}

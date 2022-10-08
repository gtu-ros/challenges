
#include <cstdlib> // Use for the absolute value method abs()
#include <iostream> // Enables command line input and output
 
#include "ros/ros.h" // Necessary header files for ROS
#include "geometry_msgs/Twist.h" // Twist messages (linear & angular velocity)
#include "geometry_msgs/Pose2D.h" // x, y position and theta orientation
#include "turtlesim/Pose.h" // x, y, theta, linear & angular velocity
#include "std_msgs/Float32.h"
#include "challenge1/Completed.h"
// Remove the need to use std:: prefix
using namespace std;
 
// Key variable declarations 
geometry_msgs::Twist velCommand; // Linear and angular velocity in m/s 
geometry_msgs::Pose2D current; // Current x, y, and theta 
geometry_msgs::Pose2D desired; // Desired x, y, and theta 
geometry_msgs::Pose2D startpos;
geometry_msgs::Pose2D firstcorner;
geometry_msgs::Pose2D secondcorner;
geometry_msgs::Pose2D goal;
challenge1::Completed msg;

double sideLen = 1;
const double PI = 3.14159265359;
bool firstCornerReached = false;
bool secondCornerReached = false;
bool triangleDone = false;
bool startPosDetermined = false;
double velocity = 0;
 
// The distance threshold in meters that will determine when 
// the turtlesim robot successfully reaches the goal.
const double distanceTolerance = 0.1;

// Initialized variables and take care of other setup tasks
void setup() {
  // Initial linear and angular velocities are 0 m/s and rad/s, respectively.
  velCommand.linear.x = 0.0;
  velCommand.linear.y = 0.0;
  velCommand.linear.z = 0.0;
  velCommand.angular.x = 0.0;
  velCommand.angular.y = 0.0;
  velCommand.angular.z = 0.0;
}
/**
 *  converts angles from degree to radians  
 */

double degrees2radians(double angle_in_degrees){
	return angle_in_degrees *PI /180.0;
}
 void rotate (double angular_speed, double relative_angle, bool clockwise,ros::Publisher velocityPub){
	   geometry_msgs::Twist vel_msg;
	   //set a random linear velocity in the x-axis
	   vel_msg.linear.x = 0;
	   vel_msg.linear.y = 0;
	   vel_msg.linear.z = 0;
	   //set a random angular velocity in the y-axis
	   vel_msg.angular.x = 0;
	   vel_msg.angular.y = 0;
	   if (clockwise)
	   	vel_msg.angular.z = -abs(angular_speed);
	   else
	   	vel_msg.angular.z = abs(angular_speed);

	   double t0 = ros::Time::now().toSec();
	   double current_angle = 0.0;
	   ros::Rate loop_rate(1000);
	   do{
		   velocityPub.publish(vel_msg);
		   double t1 = ros::Time::now().toSec();
		   current_angle = angular_speed * (t1-t0);
		   ros::spinOnce();
		   loop_rate.sleep();
		   //cout<<(t1-t0)<<", "<<current_angle <<", "<<relative_angle<<endl;
	   }while(current_angle<relative_angle);
	   vel_msg.angular.z = 0;
	   velocityPub.publish(vel_msg);
}


double getDistanceToGoalx() {
  return (goal.x - current.x);
}
double getDistanceToGoaly(){
  return (goal.y - current.y);
}
double setTriangleCorners()
{
  firstcorner.x = startpos.x + sideLen;
  firstcorner.y = startpos.y;
  secondcorner.x = (startpos.x + firstcorner.x) / 2;
  double yval = sqrt((sideLen*sideLen) - ((sideLen/2) * sideLen/2));
  secondcorner.y = startpos.y + yval;
  goal = firstcorner;
}

void changeGoal(ros::Publisher velocityPub){
  if(!firstCornerReached){
    goal = firstcorner;
    rotate(degrees2radians(30),degrees2radians(120),false,velocityPub);
  }else if(!secondCornerReached){
    goal = secondcorner;
    rotate(degrees2radians(30),degrees2radians(120),false,velocityPub);
    msg.completed = 33.333333f;
    

  }else if(!triangleDone){
    goal = startpos;
    rotate(degrees2radians(30),degrees2radians(120),false,velocityPub);
    msg.completed = 66.666666f;
  }else{
    msg.completed = 100;
    cout << "Triangle has been drawn!"<< endl << endl;
  }
  
}
// when a triangle is finished, reset the necessary values and be ready to draw another triangle
 void reset(){
  startPosDetermined = false;
  firstCornerReached = false;
  secondCornerReached = false;
  triangleDone = false;
}
// If we haven't yet reached the goal, set the velocity value.
// Otherwise, stop the robot.
void setVelocity(ros::Publisher velocityPub) {
  if (abs(getDistanceToGoalx()) > distanceTolerance || abs(getDistanceToGoaly()) > distanceTolerance) {
 
    // The magnitude of the robot's velocity is directly
    // proportional to the distance the robot is from the 
    // goal.
    velCommand.linear.x = velocity;
    if(!firstCornerReached){
      msg.completed = (((current.x - startpos.x) /sideLen) * ((double)1/3)) * 100;
    }else if(!secondCornerReached){
      msg.completed = (sqrt((firstcorner.x - current.x)*(firstcorner.x - current.x) + (current.y - firstcorner.y)*(current.y - firstcorner.y)) + sideLen) * 100 / (3 * sideLen);
    }else if(!triangleDone){
      msg.completed = (sqrt((secondcorner.x - current.x)*(secondcorner.x - current.x) + (secondcorner.y - current.y)*(secondcorner.y - current.y)) + (2*sideLen)) * 100 / (3 * sideLen);
    }
  }
  else {
    velCommand.linear.x = 0;
    velCommand.linear.y = 0;
    if(!firstCornerReached){
      firstCornerReached = true;
    }else if(!secondCornerReached){
      secondCornerReached = true;
    }else if(!triangleDone){
      triangleDone = true;
    }else{   
      reset();
    }
    changeGoal(velocityPub);

  }
}
void updatePose(const turtlesim::PoseConstPtr &currentPose) {
  current.x = currentPose->x;
  current.y = currentPose->y;
  current.theta = currentPose->theta;
}


 
int main(int argc, char **argv) {
 
  setup();  
 
  // Initiate ROS
  ros::init(argc, argv, "draw_triangle");
  // Create the main access point to communicate with ROS
  ros::NodeHandle node;
 
  // Subscribe to the robot's pose
  // Hold no messages in the queue. Automatically throw away 
  // any messages that are received that are not able to be
  // processed quickly enough.
  // Every time a new pose is received, update the robot's pose.
  ros::Subscriber currentPoseSub =
    node.subscribe("turtle1/pose", 0, updatePose);
 
  // Publish velocity commands to a topic.
  // Hold no messages in the queue. Automatically throw away 
  // any messages that are received that are not able to be
  // processed quickly enough.
  ros::Publisher velocityPub = node.advertise<geometry_msgs::Twist>("turtle1/cmd_vel", 0);
  
  ros::Publisher draw_percent_pub = node.advertise<std_msgs::Float32>("draw_percent",1000);

  //ros::Publisher pub = node.advertise<challenge1::Completed>("completed",10);
  // Specify a frequency that want the while loop below to loop at
  // In this case, we want to loop 10 cycles per second
  ros::Rate loop_rate(10); 
  
  // Keep running the while loop below as long as the ROS Master is active. 
  while (ros::ok()) {
 
    // Here is where we call the callbacks that need to be called.
   ros::spinOnce();
   if(current.x != 0 && !startPosDetermined){
    
    startpos = current;
    startPosDetermined = true;
    //x 11.104889
    // y 0 
    double maxLen = 11.104889 - startpos.x;
    if(startpos.y < maxLen){
      maxLen = startpos.y;
    }
    char ask;
    cout << "continue drawing? (y/n):" ;
    cin >> ask;
    if(ask == 'n'){
      return 0;
    }

    cout << "enter side length (max:" << maxLen <<"min:0): ";
    cin >> sideLen;
    setTriangleCorners();
   }
   if(!startPosDetermined){
    continue;
   }
   node.getParam("turtle_speed",velocity);
   // After we call the callback function to update the robot's pose, we 
   // set the velocity values for the robot.
   setVelocity(velocityPub);
   // Publish the velocity command to the ROS topic
   velocityPub.publish(velCommand);
   
   draw_percent_pub.publish(msg);
  
    // Sleep as long as we need to to make sure that we have a frequency of
    // 10Hz
    loop_rate.sleep();
  }
 
  return 0;
}

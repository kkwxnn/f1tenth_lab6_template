#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

import numpy as np
from sensor_msgs.msg import LaserScan
from ackermann_msgs.msg import AckermannDriveStamped, AckermannDrive
# TODO CHECK: include needed ROS msg type headers and libraries
from nav_msgs.msg import Odometry
from geometry_msgs.msg import PoseStamped
import tf_transformations
import tf2_ros

class PurePursuit(Node):
    """ 
    Implement Pure Pursuit on the car
    This is just a template, you are free to implement your own node!
    """
    def __init__(self):
        super().__init__('pure_pursuit_node')
        # TODO: create ROS subscribers and publishers
        self.subscription_odom = self.create_subscription(Odometry, '/odom',  self.pose_callback, 10)
        self.publisher_drive = self.create_publisher(AckermannDriveStamped, '/drive', 10)
        self.lookahead_distance = 1.0
        
        self.cwd = '/home/kwan/f1tenth/src/f1tenth_lab6_template/pure_pursuit/scripts'
        wps = np.genfromtxt(self.cwd+'/levine_blocked_waypoints.csv', delimiter = ',')
        uniques = np.unique(wps, axis = 0, return_index = True)
        idxs = np.sort(uniques[1])
        self.unique_wps = wps[idxs]
        self.unique_xys = self.unique_wps[:,:2] # waypoints only x and y

        self.odom_x = 0
        self.odom_y = 0
        self.odom_theta = 0

    def pose_callback(self, pose_msg):
       
        _, _, self.odom_theta = tf_transformations.euler_from_quaternion([pose_msg.pose.pose.orientation.x,
                                                                pose_msg.pose.pose.orientation.y,
                                                                pose_msg.pose.pose.orientation.z,
                                                                pose_msg.pose.pose.orientation.w])
        self.odom_x = pose_msg.pose.pose.position.x
        self.odom_y = pose_msg.pose.pose.position.y

        # TODO: find the current waypoint to track using methods mentioned in lecture
        
        # odom represent the coordinates of the lookahead point in global frame of reference
        odom_lookahead_x = self.odom_x + (self.lookahead_distance * np.cos(self.odom_theta))
        odom_lookahead_y = self.odom_y + (self.lookahead_distance * np.sin(self.odom_theta))

        # find closest waypoint to calculate eucledian distance
        eucledian_dist = np.sqrt(np.sum((self.unique_xys - [odom_lookahead_x, odom_lookahead_y]) ** 2, axis=1))
        min_dist_index = np.argmin(eucledian_dist)
        wp_x = self.unique_xys[min_dist_index][0]
        wp_y = self.unique_xys[min_dist_index][1]
        
        # TODO: transform goal point to vehicle frame of reference
        dx = wp_x - self.odom_x
        dy = wp_y + self.odom_y

        # transform to robot's local coordinate frame
        transform_x = dx * np.cos(self.odom_theta) + dy * np.sin(self.odom_theta)
        transform_y = - dx * np.sin(self.odom_theta) + dy * np.cos(self.odom_theta)

        # TODO: calculate curvature/steering angle
        steering_angle = (2 * transform_y) / ((transform_x ** 2) + (transform_y ** 2))
        K = 0.6
        steering_angle = K * steering_angle

        # TODO: publish drive message, don't forget to limit the steering angle.
        if steering_angle >= np.pi/6:
            steering_angle = np.pi/6
        elif steering_angle <= -np.pi/6:
            steering_angle = -np.pi/6
        
        drive_msg = AckermannDriveStamped()
        drive_msg.drive.speed = 0.5
        drive_msg.drive.steering_angle = steering_angle
        self.publisher_drive.publish(drive_msg)

def main(args=None):
    rclpy.init(args=args)
    print("PurePursuit Initialized")
    pure_pursuit_node = PurePursuit()
    rclpy.spin(pure_pursuit_node)

    pure_pursuit_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

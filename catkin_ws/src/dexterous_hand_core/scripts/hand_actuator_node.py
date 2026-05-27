#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from sensor_msgs.msg import JointState

def joint_callback(msg):
    rospy.loginfo("=======================================")
    rospy.loginfo("Received target joints from planner!")
    rospy.loginfo(f"Total Joints: {len(msg.name)}")
    for i in range(len(msg.name)):
        rospy.loginfo(f"{msg.name[i]}: {msg.position[i]:.2f}")
    rospy.loginfo("Actuation simulated successfully.")
    rospy.loginfo("=======================================")

def main():
    rospy.init_node('hand_actuator_node', anonymous=True)
    rospy.Subscriber('/planning/target_joints', JointState, joint_callback)
    
    rospy.loginfo("Hand Actuator Node Initialized.")
    rospy.loginfo("Waiting for JointState messages on /planning/target_joints...")
    
    rospy.spin()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass

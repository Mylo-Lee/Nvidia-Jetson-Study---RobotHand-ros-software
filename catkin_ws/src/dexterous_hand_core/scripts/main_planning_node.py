#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String
from sensor_msgs.msg import JointState

class MainPlanningNode:
    def __init__(self):
        rospy.init_node('main_planning_node', anonymous=True)
        self.pub = rospy.Publisher('/planning/target_joints', JointState, queue_size=10)
        self.sub = rospy.Subscriber('/teleop/keyboard_cmd', String, self.cmd_callback)
        
        self.joint_names = [f'joint_{i}' for i in range(1, 16)]
        self.current_positions = [0.0] * 15
        
        rospy.loginfo("Main Planning Node Initialized. Waiting for commands...")

    def cmd_callback(self, msg):
        cmd = msg.data
        rospy.loginfo(f"Received command: {cmd}, calculating trajectory...")
        
        # Calculate target positions based on command
        if cmd == 'q': # Open
            self.current_positions = [0.0] * 15
        elif cmd == 'w': # Close
            self.current_positions = [1.57] * 15
        elif cmd == 'e': # Pinch
            # Thumb and Index (Assume joint 1, 2, 3, 4 are thumb and index)
            self.current_positions = [0.0] * 15
            self.current_positions[0] = 1.0
            self.current_positions[1] = 1.0
            self.current_positions[2] = 1.0
            self.current_positions[3] = 1.0
        elif cmd == 'r': # Point
            # Index open (0.0), others closed (1.57)
            self.current_positions = [1.57] * 15
            self.current_positions[2] = 0.0
            self.current_positions[3] = 0.0
        elif cmd == 's': # Stop / Reset
            self.current_positions = [0.0] * 15
        else:
            return

        self.publish_joints()

    def publish_joints(self):
        js = JointState()
        js.header.stamp = rospy.Time.now()
        js.name = self.joint_names
        js.position = self.current_positions
        self.pub.publish(js)

if __name__ == '__main__':
    try:
        MainPlanningNode()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass

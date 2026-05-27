#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
import cv2
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

def main():
    rospy.init_node('camera_driver_node', anonymous=True)
    pub = rospy.Publisher('/camera/image_raw', Image, queue_size=10)
    rate = rospy.Rate(10) # 10hz
    bridge = CvBridge()

    while not rospy.is_shutdown():
        # Create a blank black image
        img = np.zeros((480, 640, 3), dtype=np.uint8)
        
        # Add text
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = "Camera is running..."
        cv2.putText(img, text, (150, 240), font, 1, (0, 255, 0), 2, cv2.LINE_AA)
        
        # Convert and publish
        img_msg = bridge.cv2_to_imgmsg(img, encoding="bgr8")
        pub.publish(img_msg)
        
        rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass

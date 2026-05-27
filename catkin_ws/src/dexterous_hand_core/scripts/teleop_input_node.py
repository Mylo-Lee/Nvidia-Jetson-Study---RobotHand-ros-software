#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String
import sys
import select
import os

if os.name == 'nt':
    import msvcrt
else:
    import termios
    import tty

msg = """
Reading from the keyboard and Publishing to /teleop/keyboard_cmd!
---------------------------
Shortcut keys:
   q : Open Hand
   w : Close Hand (Grasp)
   e : Pinch
   r : Point
   s : Stop / Reset

CTRL-C to quit
"""

def getKey():
    if os.name == 'nt':
        if msvcrt.kbhit():
            return msvcrt.getch().decode('utf-8')
        return ''
    else:
        tty.setraw(sys.stdin.fileno())
        rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
        if rlist:
            key = sys.stdin.read(1)
        else:
            key = ''
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
        return key

if __name__=="__main__":
    if os.name != 'nt':
        settings = termios.tcgetattr(sys.stdin)

    rospy.init_node('teleop_input_node')
    pub = rospy.Publisher('/teleop/keyboard_cmd', String, queue_size=1)

    print(msg)

    try:
        while not rospy.is_shutdown():
            key = getKey()
            if key:
                if key == '\x03': # CTRL-C
                    break
                if key in ['q', 'w', 'e', 'r', 's']:
                    rospy.loginfo(f"Publishing Command: {key}")
                    pub.publish(String(data=key))
    except Exception as e:
        print(e)
    finally:
        if os.name != 'nt':
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)

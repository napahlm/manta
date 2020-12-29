#! /usr/bin/env python

import rospy
from sensor_msgs.msg import Joy
from manta_msgs.msg import Propulsion

class Joystick():
    def __init__(self):
        rospy.init_node('joystick_node')

        self.sub = rospy.Subscriber('joy', Joy, self.callback, queue_size=1)
        self.pub = rospy.Publisher('throttle', Propulsion, queue_size=1)

        # Mapping buttons from the Xbox controller
        # v: vertical, h: horizontal
        self.buttons_map = ['A', 'B', 'X', 'Y',
                            'L1', 'R1', 'back', 'start', 'xbox',
                            'stick_button_left', 'stick_button_right']
        self.axes_map = ['axis_left_h', 'axis_left_v', 'L2',
                         'axis_right_h', 'axis_right_v', 'R2',
                         'dpad_h', 'dpad_v']

    def callback(self, msg):
        # Creating dictionaries containing the mapped buttons
        buttons = {}
        axes = {}

        for i in range(len(msg.buttons)):
            buttons[self.buttons_map[i]] = msg.buttons[i]

        for j in range(len(msg.axes)):
            axes[self.axes_map[j]] = msg.axes[j]

        throttle_msg = Propulsion()
        throttle_msg.throttle = abs(axes['axis_left_h'])    # PWM throttle

        throttle_msg.header.stamp = rospy.get_rostime()

        self.pub.publish(throttle_msg)

if __name__ == '__main__':
    try:
        joystick_node = Joystick()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass

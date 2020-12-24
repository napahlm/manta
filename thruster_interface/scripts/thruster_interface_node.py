#!/usr/bin/env python

import rospy

from manta_msgs.msg import Propulsion, Pwm

global throttle

class ThrusterInterface():
    def __init__(self):
        rospy.init_node('thruster_interface', anonymous=False)

        self.sub = rospy.Subscriber('throttle', Propulsion, self.callback)
        self.pub = rospy.Publisher('pwm', Pwm, queue_size=10)
        self.pwmmax = 1400

        rospy.loginfo('Initialized thrusters.')

    def callback(self, msg):

        microsecs = 1000
        pwm_msg = Pwm()
        throttle = msg.throttle

        # REMAPPING VALUES TO PWM
        propulsion_range = (1 - 0)      # using absolute values on the joystick
        if (propulsion_range == 0):
            pwm_var = 1000
        else:
            pwm_range = (self.pwmmax - 1000)
            pwm_var = (((throttle - 0) * pwm_range) / propulsion_range) + 1000.0

        # REMOVING OUTLIERS
        if pwm_var < 1000 and pwm_var > self.pwmmax:
            pwm_var = 1000

        # ASSIGNING DATA
        pwm_msg.positive_width_us = int(pwm_var)

        # PUBLISHING DATA
        self.pub.publish(pwm_msg)

        

if __name__ == '__main__':
    try:
        thruster_interface = ThrusterInterface()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass

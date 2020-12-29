#! /usr/bin/env python

import rospy
from std_msgs.msg import Int16
import random

class Shout():
    def __init__(self):
        rospy.init_node('shouter_node')
        self.pub = rospy.Publisher('shouter_topic', Int16, queue_size=10)
        self.rate = rospy.Rate(1)

    def callback(self, msg):
        random_shout = random.randint(1, 100)

        shouter_msg = Int16()
        shouter_msg.shout = random_shout

        shouter_msg.header.stamp = rospy.get_rostime()
        print(random_shout)
        self.pub.publish(shouter_msg)

        rate.sleep()

if __name__ == '__main__':
    try:
        shouter_node = Shout()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass

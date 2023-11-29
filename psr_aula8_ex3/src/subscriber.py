#!/usr/bin/env python3

import argparse
import rospy
from std_msgs.msg import String

def callback(message_recieved):
    print(message_recieved.data)

def main():

    #----------------------------
    # Initialization
    #----------------------------

    # setup of argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--topic', type=str, help='Topic name to subscribe to.', default='chatter')
    args = vars(parser.parse_args())

    # setup ROS
    rospy.init_node('subscriber', anonymous=True)
    rospy.Subscriber(args['topic'], String, callback)

    #----------------------------
    # Execution
    #----------------------------

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

    #----------------------------
    # Termination
    #----------------------------

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
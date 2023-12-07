#!/usr/bin/env python3

from psr_aula8_ex4.msg import Dog
import argparse
import rospy
from std_msgs.msg import String

def main():

    #----------------------------
    # Initialization
    #----------------------------

    # setup of argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--topic', type=str, help='Topic name to subscribe to.', default='chatter')
    parser.add_argument('-f', '--frequency', type=int, help='Publication frequency.', default=1)
    parser.add_argument('-c', '--content', type=str, help='Content to publish.',
                        default='silencio absoluto ...')
    args = vars(parser.parse_args())

    # setup ROS
    pub = rospy.Publisher(args['topic'], String, queue_size=10)

    rospy.init_node('publisher', anonymous=True)

    rate = rospy.Rate(args['frequency'])
    while not rospy.is_shutdown():

        # construct the message to send
        message_to_send = Dog()
        message_to_send = 'Nono'
        message_to_send = 'Black'
        message_to_send = 9
        message_to_send.brothers.append('Bobi')
        message_to_send.brothers.append('Lassie')

        rospy.loginfo(message_to_send)
        pub.publish(message_to_send)
        rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
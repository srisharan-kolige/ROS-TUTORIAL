#!/usr/bin/env python3
import rospy
from std_msgs.msg import String, Int32MultiArray


def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard from the talker %s', data.data)

def listener_talker():

    rospy.init_node('talker_listener', anonymous=True)

    rospy.Subscriber('chatter', String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    #rospy.spin()

    pub = rospy.Publisher('chatter_2', String, queue_size=10)
    
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        hello_str = "This message is from the publisher_subscriber %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

    

if __name__ == '__main__':
    try:
        listener_talker()
    except rospy.ROSInterruptException:
        pass

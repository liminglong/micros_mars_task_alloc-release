#!/usr/bin/env python

__author__ = 'Minglong Li'

#import sys
#sys.path.append("~/catkin_ws/src/multi_robot_patrol/scripts/basic_support")

from robot_patrol_area_0 import RobotPatrolArea0
from robot_patrol_area_1 import RobotPatrolArea1
from robot_patrol_area_2 import RobotPatrolArea2
from motivational_behavior import MotivationalBehavior
from switch import Switch
from std_msgs.msg import Bool
from geometry_msgs.msg import Twist
from robot_detect import RobotDetect0
from robot_follow import RobotFollow0
import move_base_msgs.msg

bs0 = RobotPatrolArea0("robot_0/move_base/switch0","robot_0_partrol0_node")
bs1 = RobotPatrolArea1("robot_0/move_base/switch1","robot_0_partrol1_node")
bs2 = RobotPatrolArea2("robot_0/move_base/switch2","robot_0_partrol2_node")
bs0.start()
bs1.start()
bs2.start()

mb0 = MotivationalBehavior('r0_mb0',0,0,'robot0_switch0_patrol/activate')#nodename,robotid,behaviorid
mb0.set_fast(20)
mb0.enable_random_inc()
mb0.set_sensory_feedback(1)
mb0.set_sensor('robot_0/patrol_sensory_feedback')
mb0.start()
s0 = Switch('robot0_switch0_patrol','robot_0/move_base/switch0/goal',move_base_msgs.msg.MoveBaseActionGoal,'robot_0/move_base/goal','/robot_0/move_base/result', move_base_msgs.msg.MoveBaseActionResult, '/robot_0/move_base/switch0/result')#nodename,subtopic,type,pubtopic
s0.add_action('robot_0/move_base/switch0','robot_0/move_base')
s0.start()

mb1 = MotivationalBehavior('r0_mb1',0,1,'robot0_switch1_patrol/activate')#nodename,robotid,behaviorid
mb1.set_fast(10)
mb1.enable_random_inc()
mb1.set_sensory_feedback(1)
mb1.set_sensor('robot_0/patrol_sensory_feedback')
mb1.start()
s1 = Switch('robot0_switch1_patrol','robot_0/move_base/switch1/goal',move_base_msgs.msg.MoveBaseActionGoal,'robot_0/move_base/goal','/robot_0/move_base/result', move_base_msgs.msg.MoveBaseActionResult, '/robot_0/move_base/switch1/result')#nodename,subtopic,type,pubtopic
s1.add_action('robot_0/move_base/switch1','robot_0/move_base')
s1.start()

mb2 = MotivationalBehavior('r0_mb2',0,2,'robot0_switch2_patrol/activate')#nodename,robotid,behaviorid
mb2.set_fast(10)
mb2.enable_random_inc()
mb2.set_sensory_feedback(1)
mb2.set_sensor('robot_0/patrol_sensory_feedback')
mb2.start()
s2 = Switch('robot0_switch2_patrol','robot_0/move_base/switch2/goal',move_base_msgs.msg.MoveBaseActionGoal,'robot_0/move_base/goal','/robot_0/move_base/result', move_base_msgs.msg.MoveBaseActionResult, '/robot_0/move_base/switch2/result')#nodename,subtopic,type,pubtopic
s2.add_action('robot_0/move_base/switch2','robot_0/move_base')
s2.start()

rDetect = RobotDetect0()
rDetect.start()
bs4 = RobotFollow0()
bs4.start()
mb4 = MotivationalBehavior('r0_mb4',0,4,'robot0_switch_follow/activate')#nodename,robotid,behaviorid
mb4.set_fast(110)
mb4.set_sensor('robot_0/follow_sensory_feedback')
mb4.start()
ob7 = Switch('robot0_switch_follow','robot_0/cmd_vel/follow',Twist,'robot_0/cmd_vel')#nodename,subtopic,type,pubtopic
ob7.start()

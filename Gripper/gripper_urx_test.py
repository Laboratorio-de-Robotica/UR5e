import urx
from robotiq_two_finger_gripper import Robotiq_Two_Finger_Gripper

miRobot = urx.Robot("100.0.0.16")
robotiqgrip = Robotiq_Two_Finger_Gripper()
robotiqgrip.close_gripper()
miRobot.send_program(robotiqgrip.ret_program_to_run())
miRobot.close()
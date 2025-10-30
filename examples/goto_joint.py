from utils import get_dobot_port

from pydobotpp import Dobot, PTPMode, Pose

"""
Test script to move the Dobot to specified joint angles and read back the pose of the effector 
and the joint positions of the robot.
"""


def main():
    import argparse

    parser = argparse.ArgumentParser()

    parser.add_argument("joint1", type=float, help="Joint 1 angle")
    parser.add_argument("joint2", type=float, help="Joint 2 angle")
    parser.add_argument("joint3", type=float, help="Joint 3 angle")
    parser.add_argument("joint4", type=float, help="Joint 4 angle")

    parser.add_argument(
        "--reset", action="store_true", help="Reset to initial position after move"
    )

    parser.add_argument(
        "--home", action="store_true", help="Home the robot before moving"
    )

    args = parser.parse_args()
    dobot = Dobot(port=get_dobot_port())

    try:
        if args.home:
            dobot.wait_for_cmd(dobot.home())

        pose = dobot.get_pose()
        dobot.move_to(
            args.joint1, args.joint2, args.joint3, args.joint4, mode=PTPMode.MOVJ_ANGLE
        )
        current_pose = dobot.get_pose()
        print(
            f"Current effector position = {current_pose.position} | Q = {current_pose.joints}"
        )
        dobot.wait(1000)

        if args.reset:
            dobot.move_to(
                pose.joints.j1,
                pose.joints.j2,
                pose.joints.j3,
                pose.joints.j4,
                mode=PTPMode.MOVJ_ANGLE,
            )
    except KeyboardInterrupt:
        pass
    finally:
        dobot.close()


if __name__ == "__main__":
    main()

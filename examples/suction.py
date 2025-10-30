from utils import get_dobot_port

from pydobotpp import Dobot

"""
Test script to activate and deactivate the suction cup of the Dobot.
"""


def main():
    dobot = Dobot(port=get_dobot_port())

    try:
        print("Activating suction cup for 1.5 seconds")
        dobot.suck(True)
        dobot.wait(1500)
        dobot.wait_for_cmd(dobot.suck(False))
        print("Deactivating suction cup")
    except KeyboardInterrupt:
        pass
    finally:
        dobot.close()


if __name__ == "__main__":
    main()

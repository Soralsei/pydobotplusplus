from utils import get_dobot_port

from pydobotpp import Dobot

if __name__ == "__main__":
    """
    Test script to print the current alarms of the Dobot.
    """

    dobot = Dobot(port=get_dobot_port(), should_clear_alarms=False)

    alarms = dobot.get_alarms()
    if not alarms:
        print("No alarms.")
    else:
        print("Current alarms:")
        for alarm in alarms:
            print(f"- {alarm.name} (code: {alarm.value:#04x})")
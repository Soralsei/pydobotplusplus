from serial.tools import list_ports

DOBOT_COM_VID = 0x10C4
DOBOT_COM_PID = 0xEA60


def get_dobot_port():
    available_ports = list_ports.comports()
    for port in available_ports:
        print(
            f"Found port: {port.device} - {port.description}, HWID: [{port.hwid}], VID: {port.vid}, PID: {port.pid}"
        )
        if DOBOT_COM_VID == port.vid and DOBOT_COM_PID == port.pid:
            return port.device

    return None

import asyncio
from pymata_core import PymataCore
from constants import Constants
import sys
import signal


# this program monitors the A2 pin. Modify to meet your needs

async def my_callback(data):
    # data[0] is the pin number and data[1] is the changed value
    print("data: {}".format(data))


try:
    # board = PymataCore(com_port="/dev/cu.usbmodemHIDFG1")
    board = PymataCore()
    board.start()
    board.set_command_center_callback(my_callback)
except KeyboardInterrupt:
    sys.exit(0)


# Signal handler to trap control C
def _signal_handler(sig, frame):
    if board is not None:
        print('\nYou pressed Ctrl+C')
        sys.exit(1)


signal.signal(signal.SIGINT, _signal_handler)
signal.signal(signal.SIGTERM, _signal_handler)

# add SIGALRM if platform is not windows
if not sys.platform.startswith('win32'):
    signal.signal(signal.SIGALRM, _signal_handler)


async def cc_test():
    while True:
        hid_enabled = await board.command_center_get(100)
        up = await board.command_center_get(6)
        down = await board.command_center_get(7)
        left = await board.command_center_get(8)
        right = await board.command_center_get(9)
        js = await board.command_center_get(13)
        print("hid: {}, up: {}, down: {}, left: {}, right: {}, js: {}".format(hid_enabled,
                                                                              up, down, left, right, js))
        # await board.command_center_set(100, not hid_enabled)
        await board.command_center_set(6, down)
        await board.command_center_set(7, left)
        await board.command_center_set(8, right)
        await board.command_center_set(9, js)
        await board.command_center_set(13, up)
        await board.sleep(10)

loop = asyncio.get_event_loop()
loop.run_until_complete(cc_test())

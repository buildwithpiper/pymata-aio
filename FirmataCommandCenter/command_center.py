import time

import asyncio

from pymata_aio.pymata_core import PymataCore
from pymata_aio.constants import Constants
from pymata_aio.private_constants import PrivateConstants
from pymata_aio.pymata_serial import PymataSerial
from pymata_aio.pymata_socket import PymataSocket

HID_ENABLE = 0x72
HID_DISABLE = 0x73

# port = PymataSerial('/dev/cu.usbmodemHIDF1', 57600)


async def send_message(message, board):
    print("message: {}".format(chr(message)))
    sysex_message = chr(PrivateConstants.START_SYSEX)
    sysex_message += chr(message)
    sysex_message += chr(PrivateConstants.END_SYSEX)
    for data in sysex_message:
        print("write {}".format(data))
        await board.write(data)


async def do_it(board):
    while True:
        print("enable")
        await send_message(HID_ENABLE, board)
        await asyncio.sleep(10)
        print("disable")
        await send_message(HID_DISABLE, board)
        await asyncio.sleep(10)
# async def pin_6_pwm_128(my_board):
#     """
#     Set digital pin 6 as a PWM output and set its output value to 128
#     @param my_board: A PymataCore instance
#     @return: No Return Value
#     """
#     # toggle on/off
#     while True:
#         await my_board._send_sysex(HID_ENABLE, [])
#         await asyncio.sleep(10)
#         await my_board._send_sysex(HID_DISABLE, [])
#         await asyncio.sleep(10)


# # create a PyMataCore instance and complete the initialization with a call to start()
board = PymataCore(com_port='/dev/cu.usbmodemHIDF1')
board.start()

# get the loop, and execute pin6_pwm_128
loop = asyncio.get_event_loop()
loop.run_until_complete(do_it(board))

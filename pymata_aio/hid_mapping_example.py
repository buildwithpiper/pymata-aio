#!/usr/bin/env python3

import asyncio

from pymata_core import PymataCore
from constants import Constants

def get_button_list():
    return {
        'up': Constants.HID_BUTTON_UP,
        'down': Constants.HID_BUTTON_DOWN,
        'left': Constants.HID_BUTTON_LEFT,
        'right': Constants.HID_BUTTON_RIGHT,
        'joystick': Constants.HID_BUTTON_JOYSTICK
    }

async def enable_hid(my_board):
    await my_board._hid_set(Constants.HID_ENABLED, 1)

async def disable_hid(my_board):
    await my_board._hid_set(Constants.HID_ENABLED, 0)

async def get_hid_status(my_board):
    return await my_board._hid_get(Constants.HID_ENABLED)

async def print_hid_status(my_board):
    hid_status = await get_hid_status(my_board)
    print("Current HID Status: {}".format(hid_status))

async def print_button_state(my_board):
    button_code = get_button_list()
    for button in button_code.keys():
        button_mapping = await my_board._hid_get(button_code[button])
        print("{} Button: '{}'".format(button.upper(), button_mapping))

async def change_button_mapping(my_board):
    print("Changing button mappings.")
    await my_board._hid_set(Constants.HID_BUTTON_UP, ord('w'))
    await my_board._hid_set(Constants.HID_BUTTON_LEFT, ord('a'))
    await my_board._hid_set(Constants.HID_BUTTON_DOWN, ord('s'))
    await my_board._hid_set(Constants.HID_BUTTON_RIGHT, ord('d'))

async def hid_test(my_board):
    await enable_hid(my_board)

    for i in range(20):
        await asyncio.sleep(1)

    await disable_hid(my_board)
    await my_board.shutdown()

board = PymataCore()
board.start()
loop = asyncio.get_event_loop()
loop.run_until_complete(hid_test(board))
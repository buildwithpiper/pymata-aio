# Command Center Event Channels usage example
# Author: John Chen

import asyncio
from pymata_core import PymataCore
from command_center_event_channels import CommandCenterEventChannels

async def apply_subscriptions(channels):
    channels.subscribe(print, 'RAW')

async def initialize(board, channels):
    await apply_subscriptions(channels)
    await board.start_aio()
    await board.enable_hid()

async def shutdown(board):
    await board.disable_hid()
    await board.shutdown()

async def messenger_test(board, channels):
    await initialize(board, channels)

    STOP_TIME = 6
    for i in range(STOP_TIME):
        await asyncio.sleep(1)

    await shutdown(board)

def loop(board, channels):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(messenger_test(board, channels))

def setup():
    channels = CommandCenterEventChannels()
    board = PymataCore(command_center_channels=channels)

    return (board, channels)

def main():
    board, channels = setup()
    loop(board, channels)

if __name__ == '__main__':
    main()
    
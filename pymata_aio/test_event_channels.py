from pymata_core import PymataCore
from command_center_event_channels import CommandCenterEventChannels

__DEBUG__ = True
__DEBUG_PRINT__ = True

def debug_print(stmt):
    if __DEBUG_PRINT__:
        print(stmt)

def print_channel_list(test_channels):
    debug_print("Current channels: {}".format(test_channels.channel_list()))

def test_creation():
    test_board = PymataCore()
    my_channels = CommandCenterEventChannels()
    assert (my_channels), "Could not initialize channels."
    return my_channels

def test_add_channel(test_channels):
    print_channel_list(test_channels)

    debug_print("Adding channels...")
    test_channels.add_channels(['A', 'B', 'C'])
    test_channels.add_channel('D')
    debug_print("Channels added!")

    print_channel_list(test_channels)
    
def test_subscribe_print(payload=None):
    assert (payload), "No payload to print in test_subscribe_print()"
    data = payload
    debug_print("MESSAGE RECEIVED: {}".format(data))

def test_subscribe(test_channels):
    debug_print("Current subscribers:")
    debug_print(test_channels.get_subscribers('RAW'))

    debug_print("Adding subscribers...")
    test_channels.subscribe(test_subscribe_print, 'RAW')
    test_channels.subscribe(test_subscribe_print, 'A')
    test_channels.subscribe(test_subscribe_print, 'B')
    test_channels.subscribe(test_subscribe_print, 'B')
    test_channels.subscribe(test_subscribe_print, 'C')
    test_channels.subscribe(test_subscribe_print, 'C')
    test_channels.subscribe(test_subscribe_print, 'C')

    debug_print("Current subscribers:")
    for channel_name in test_channels.channel_list():
        subscribers = test_channels.get_subscribers(channel_name)
        debug_print("{}: {}".format(channel_name, subscribers))

def test_broadcast(test_channels):
    for channel in test_channels.channel_list():
        debug_print("Broadcasting to {}".format(channel))
        
        test_payload = ["TEST_MESSAGE_TO", channel]
        test_channels.publish(test_payload, channel)

def debug_test():
    debug_print("\n"+"Testing channel creation...")
    test_channels = test_creation()
    debug_print("Channels creation test success!"+"\n")

    debug_print("\n"+"Testing channel addition...")
    test_add_channel(test_channels)
    debug_print("Channel addition test success!"+"\n")

    debug_print("\n"+"Testing channel subscription...")
    test_subscribe(test_channels)
    debug_print("Channel subscription test success!"+"\n")

    debug_print("\n"+"Testing channel broadcast...")
    test_broadcast(test_channels)
    debug_print("Channel broadcast test success!"+"\n")

def main():
    if __DEBUG__:
        debug_test()

if __name__ == '__main__':
    main()
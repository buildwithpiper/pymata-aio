import asyncio

class CommandCenterEventChannels:
    RAW_CHANNEL = "RAW"

    def __init__(self):
        self.channels = {}
        self.channels[self.RAW_CHANNEL] = []

    def channel_list(self):
        return self.channels.keys()
    
    def add_channel(self, channel_name=None):
        assert (channel_name), "No channel name supplied."
        assert (channel_name not in self.channels.keys()), "Channel already exists"

        self.channels[channel_name] = []

    def add_channels(self, channel_names=[]):
        assert (type(channel_names) == list), "Did not receive a list of channel names"
        assert (len(channel_names) >= 1), "No channel names in list"

        for channel_name in channel_names:
            self.add_channel(channel_name)

    def get_subscribers(self, channel_name=None):
        assert (channel_name), "No channel name to select with."
        assert (channel_name in self.channels.keys()), "Channel {} not found.".format(channel_name)

        return self.channels[channel_name]

    def subscribe(self, subscriber_callback=None, channel_name=None):
        assert (channel_name), "No channel name to subscribe to."
        assert (subscriber_callback), "No subscriber callback information."

        subscribers = self.get_subscribers(channel_name)
        subscribers.append(subscriber_callback)

    def publish(self, payload=None, channel_name=None):
        assert (payload), "Nothing to publish to channel {}.".format(channel_name)

        subscribers = self.get_subscribers(channel_name)
        for callback_function in subscribers:
            callback_function(payload)
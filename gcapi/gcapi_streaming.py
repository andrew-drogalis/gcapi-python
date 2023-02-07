from lightstreamer_client import LightstreamerClient, LightstreamerSubscription

class GCapiStreamingClient:

    def __init__(self, username, session_id):
        self.stream_client = LightstreamerClient(username,session_id,"https://push.cityindex.com/","STREAMINGALL")

    def subscribe_to_streaming(self, subscription_keys):
        """
		Connects to the Streaming Service
		:param subcription_keys: formated string with the market ID included
		"""
        self.stream_client.connect()
        self.subscription = LightstreamerSubscription(mode="MERGE",adapter="PRICES",items=subscription_keys,fields=["Bid", "Offer", "AuditId","MarketId","TickDate"])
        self.sub_key = self.stream_client.subscribe(self.subscription)

    def unsubscribe_to_streaming(self):
        """
		Disconnects from the Streaming Service
		"""
        self.stream_client.unsubscribe(self.sub_key)
        self.stream_client.disconnect()

    def real_time_snapshot(self):
        """
		Gets snapshot of the subscription fields
		:return: List of Real-Time Subscription Info
		"""
        subscription_snapshot = [*self.subscription._items_map.values()]

        return subscription_snapshot

    def add_event_listener(self, listener):
        """
		Adds the Listener to the Subscription Client
        :param listener: event listener function to execute upon data update
		"""
        self.subscription.addlistener(listener=listener)
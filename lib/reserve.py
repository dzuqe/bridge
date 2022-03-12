import os

class Reserve:
    def __init__(self):
        self.algo_rsv = os.environ['BRIDGE_ALGO_RSV']
        self.algo_key = os.environ['BRIDGE_ALGO_KEY']
        self.matic_rsv = os.environ['BRIDGE_MATIC_RSV']
        self.matic_key = os.environ['BRIDGE_MATIC_KEY']



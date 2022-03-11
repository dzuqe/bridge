from web3 import Web3
import algosdk

class Bridge:
    def __init__(self):
        self.web3 = Web3.HttpProvider('http://localhost:8777')
        self.client = algo.Client()
        self.reserve = Reserve()
        self.db = Db()

    def init_tx(self, from, to, value):
        self.db.start_with_data(from, to, value)
        if from is algo:
            self.algo_to_matic(from, to, value)
        else:
            self.matic_to_algo(from, to, value)

    def algo_to_matic(self, from, to, value):
        self.db.from_tx = client.send(
            from, 
            self.reserve.algo_rsv, 
            value
        )

        self.db.update()

        if from_tx is success:
            self.db.to_tx = eth.send({
                'from': self.reserve.matic_rsv, 
                'to': to, 
                'amount': value - fee,
                private_key = self.reserve.matic_key
            })
            self.status = 'SUCCESS'
            self.db.update()

    def matic_to_algo(self, from, to, value):
        self.db.from_tx = eth.send(
            from, 
            self.reserve.eth, 
            value
        )

        self.db.update()

        if self.db.from_tx is success:
            self.db.to_tx = client.send(
                self.reserve.algo, 
                to, 
                value - fee
            )

            self.status = 'SUCCESS'
            self.db.update()


    def withdraw_matic(self, id):
        self.db.start_with_id(id)

        pull_tx = self.eth.functions.transfer(
                'from': self.reserve.matic_rsv,
                'to': self.db.from_addr,
                'amount': self.db.value
                )

        self.db.status = 'WITHDREW'
        self.db.update()


    def withdraw_algo(self, id):
        self.db.start_with_id(id)
        self.client.send(
            'from': self.reserve.algo_rsv,
            'to': self.db.from_addr,
            'amount': self.db.value
            )

        self.db.status = 'WITHDREW'
        self.db.update()

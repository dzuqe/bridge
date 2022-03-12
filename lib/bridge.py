from web3 import Web3
from Algorand import Algorand
from Ethereum import Ethereum
from db import Db
import algosdk

class Bridge:
    def __init__(self):
        self.eth = Ethereum(
            os.environ['ETH_ADDR'],
            os.environ['ETH_KEY']
        )

        self.algo = Algorand(
            os.environ['PURESTAKE_API_KEY']
        )

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


contract_abi = open("./build/SwearJar.abi", "r").read()
token_abi = open("/home/hydrogen/polygon/scarg-token/build/ScarredEntertainment.abi", "r").read()

jar_address = web3.toChecksumAddress("0xbbde180847bf3b9f87c8fbfaac301390f5205928")
token_address = web3.toChecksumAddress("0xb11c1cfcee8d5879fcc1c191719b9371b195bd38")

jar = eth.contract(address=jar_address, abi=contract_abi)
token = eth.contract(address=web3.toChecksumAddress(token_address), abi=token_abi)

tx_info = {
    'gas': 1000000,
    'gasPrice': web3.toWei(1, 'gwei'),
    'chainId': eth.chainId,
    'from': '',
    'nonce': '',
}

# utils
def sos(tx, _key):
   signed = eth.account.signTransaction(tx, private_key=_key)
   result = eth.sendRawTransaction(signed.rawTransaction)
   print(result.hex())


print("approve me")
tx_info.update({'nonce': eth.getTransactionCount(me)})
tx_info.update({'from': me})
amount = web3.toWei(10000000, 'ether')
me_approve_tx = token.functions.approve(jar_address, amount).buildTransaction(tx_info)
sos(me_approve_tx, key)

print("approve for everyone else")
for id in range(1, len(users)):
    tx_info.update({'nonce': eth.getTransactionCount(users[id])})
    tx_info.update({'from': users[id]})
    amount = web3.toWei(1000000, 'ether')
    approve_tx = token.functions.approve(jar_address, amount).buildTransaction(tx_info)
    sos(approve_tx, keys[id])

print("send users erc20")
for id in range(1, len(users)):
   tx_info.update({'nonce': eth.getTransactionCount(me)})
   tx_info.update({'from': me})
   transfer_tx = token.functions.transfer(users[id], web3.toWei(300000, 'ether')).buildTransaction(tx_info)
   sos(transfer_tx, key)

 

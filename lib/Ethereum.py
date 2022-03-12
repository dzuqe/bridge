from web3 import Web3

class Ethereum:
    def __init__(self, address, key):
        self.address = address
        self.key = key

        # if os.environ['ETH_PROV'] is not None:
        # else:
        #   degenerate values
        self.web3 = Web3(Web3.HTTPProvider(os.environ['ETH_PROV']))
        self.eth = self.web3.eth
        self.check_addr = self.web3.toChecksumAddress


    def raw(self, tx):
        signed = self.eth.account.signTransaction(tx, private_key=self.key)
        result = self.eth.sendRawTransaction(signed.rawTransaction)
        print(result)
        return result.hex()


#!/usr/bin/python3

import datetime
from urllib.parse import urlparse


class Block:

    def __init__(self, previous_hash=None, proof=0, transactions=[]):
        self.previous_hash = previous_hash
        self.transactions  = transactions
        self.timestamp     = datetime.datetime.now()
        self.proof         = proof
        self.this_hash     = self.generate_hash()
    

    def generate_hash(self):
        return hash((self.previous_hash, self.timestamp, self.proof) + tuple(self.transactions))
   

    def __repr__(self):
        return "transactions: %s\ntimestamp: %s\n" % (str(self.transactions), str(self.timestamp))


class Chain(list):
    
    def __init__(self):
        genesis_block = Block()
        self.unmined_transactions = []
        self.append(genesis_block)
        self.nodes = set()


    def register_node(self, address):
        parsed_url = urlparse(address)
        if parsed_url.netloc:
            self.nodes.add(parsed_url.netloc)
        elif parsed_url.path:
            self.nodes.add(parsed_url.path)
        else:
            raise ValueError('Invalid URL')


    def register_block(self, proof=0, transactions=[]):
        self.append(Block(
            self[-1].this_hash,
            proof        = proof,
            transactions = transactions
        ))
        return len(self)-1
    
    
    def get_data(self):
        return [block.__dict__ for block in self]
    

    def isvalid(self):
        for i, block in enumerate(self):
            if i==0: continue
            if block.previous_hash != self[i-1].generate_hash():
                return False

        return True


    def add_transaction(self, transaction):
        self.unmined_transactions.append(transaction)


    def mine(self):
        self.register_block(
            proof        = self.proof_of_work(),
            transactions = self.unmined_transactions
        )
        self.unmined_transactions = []


    def proof_of_work(self):
        proof = 0
        while self.working(proof):
            proof += 1
        return proof


    def working(self, proof):
        last_proof = self[-1].proof
        last_hash  = self[-1].this_hash
        return not str(hash((last_proof, proof, last_hash)))[-4:]=="0000"



if __name__ == "__main__":
    chain = Chain()
    chain.register_block([1, 2, 3,])
    chain.register_block([1, 2, 3, 4,])
    
    print(chain)
    print(chain.isvalid())
    
    chain.chain[1].transactions[1] = 11
    print(chain)
    print(chain.isvalid())

#!/usr/bin/python3

import datetime
from urllib.parse import urlparse


class Block:

    def __init__(self, previous_hash=None, transactions=[]):
        self.previous_hash = previous_hash
        self.transactions  = transactions
        self.timestamp     = datetime.datetime.now()
        self.this_hash     = self.generate_hash()
    

    def generate_hash(self):
        return hash((self.previous_hash, self.timestamp) + tuple(self.transactions))
   

    def __repr__(self):
        return "transactions: %s\ntimestamp: %s\n" % (str(self.transactions), str(self.timestamp))


class Chain:
    
    def __init__(self):
        genesis_block = Block()
        self.chain = [genesis_block]
        self.nodes = set()


    def register_node(self, address):
        parsed_url = urlparse(address)
        if parsed_url.netloc:
            self.nodes.add(parsed_url.netloc)
        elif parsed_url.path:
            self.nodes.add(parsed_url.path)
        else:
            raise ValueError('Invalid URL')


    def register_block(self, transactions):
        self.chain.append(Block(self.chain[-1].this_hash, transactions))
        return len(self.chain)-1
    
    
    def get_data(self):
        return [block.__dict__ for block in self.chain]
    

    def isvalid(self):
        for i, block in enumerate(self.chain):
            if i==0: continue
            if block.previous_hash != self.chain[i-1].generate_hash():
                return False

        return True


if __name__ == "__main__":
    chain = Chain()
    chain.register_block([1, 2, 3,])
    chain.register_block([1, 2, 3, 4,])
    
    print(chain)
    print(chain.isvalid())
    
    chain.chain[1].transactions[1] = 11
    print(chain)
    print(chain.isvalid())

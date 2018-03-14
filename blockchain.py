#!/usr/bin/python3

import datetime


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


    def register_block(self, transactions):
        self.chain.append(Block(self.chain[-1].this_hash, transactions))
    
    
    def __repr__(self):
        output = ""
        for block in self.chain:
            output += "%s\n" % block
        return output
    

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

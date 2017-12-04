#!/usr/bin/python3

import datetime


class Block:

    def __init__(self, previous_hash=None, transactions=()):
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.this_hash = hash((previous_hash,) + transactions)
        self.timestamp = datetime.datetime.now()

    
    def __repr__(self):
        return "transactions: %s, timestamp: %s" % (str(self.transactions), str(self.timestamp))


class Chain:
    
    def __init__(self):
        genesis_block = Block()
        self.chain = [genesis_block]


    def register_block(self, transactions):
        self.chain.append(Block(self.chain[-1].this_hash, transactions))
    
    
    def __repr__(self):
        out = ""
        for block in self.chain:
            out += "%s\n" % str(block)
        return out


if __name__ == "__main__":
    chain = Chain()
    chain.register_block((1, 2, 3,))
    chain.register_block((1, 2, 3, 4,))
    print(chain)

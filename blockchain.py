class Block:

    def __init__(self, previous_hash=None, transactions=()):
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.this_hash = hash((previous_hash,) + transactions)

    
class Chain:
    
    def __init__(self):
        genesis_block = Block()
        self.chain = [genesis_block]

    def register_block(self, transactions):
        self.chain.append(Block(self.chain[-1].this_hash, transactions))


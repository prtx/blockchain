class Block:

    def __init__(self, previous_hash, transactions):
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.this_hash = hash(transactions + (previous_hash,))


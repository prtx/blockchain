import unittest
import datetime

import blockchain


class BlockchainTests(unittest.TestCase):

    def test_genesis_block(self):
        genesis_block = blockchain.Block()
        self.assertTrue(genesis_block)
        self.assertEqual(genesis_block.previous_hash, None)
        self.assertEqual(genesis_block.transactions, [])
        self.assertEqual(type(genesis_block.timestamp), datetime.datetime)


    def test_transaction_block(self):
        genesis_block = blockchain.Block()
        transactions = [1, 2, 3]
        transaction_block = blockchain.Block(genesis_block.this_hash, transactions)

        self.assertTrue(transaction_block)
        self.assertEqual(transaction_block.previous_hash, genesis_block.this_hash)
        self.assertEqual(transaction_block.transactions, transactions)
        self.assertEqual(type(transaction_block.timestamp), datetime.datetime)
        self.assertTrue(transaction_block.timestamp > genesis_block.timestamp)


unittest.main()
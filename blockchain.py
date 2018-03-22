#!/usr/bin/python3

import datetime
import requests
import pickle
import binascii
from urllib.parse import urlparse


class Block:

    def __init__(self, previous_hash=None, proof=0, transactions=[]):
        self.previous_hash = previous_hash
        self.transactions  = transactions
        self.timestamp     = datetime.datetime.now()
        self.proof         = proof
        self.this_hash     = self.generate_hash()
    

    def generate_hash(self):
        return hash("%s-%s-%s-%s" % (self.previous_hash, self.timestamp, self.proof, self.transactions))
   

    def __repr__(self):
        return "transactions: %s\ntimestamp: %s\n" % (str(self.transactions), str(self.timestamp))


class BlockChain:
    
    def __init__(self):
        genesis_block = Block()
        self.unmined_transactions = []
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


    def register_block(self, proof=0, transactions=[]):
        self.chain.append(Block(
            self.chain[-1].this_hash,
            proof        = proof,
            transactions = transactions
        ))
        return len(self.chain)-1
    
    
    def get_data(self):
        return [block.__dict__ for block in self.chain]
    

    def isvalid(self):
        for i, block in enumerate(self.chain):
            if i==0: continue
            if block.previous_hash != self.chain[i-1].generate_hash():
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
        last_proof = self.chain[-1].proof
        last_hash  = self.chain[-1].this_hash
        return not str(hash((last_proof, proof, last_hash)))[-4:]=="0000"


    def consensus(self):
        max_length = len(self.chain)
        new_chain  = None

        for node in self.nodes:
            response = requests.get('http://%s' % node)
            if response.status_code != 200: continue

            str_pickle  = response.json()['pickle']
            byte_pickle = binascii.unhexlify(str_pickle.encode('utf-8'))
            node_chain  = pickle.loads(byte_pickle)
            length      = len(node_chain.chain)
            print(length)
            print(max_length)
            print(length > max_length)
            print(node_chain.isvalid())
            if length > max_length:
                new_chain  = node_chain
                max_length = length

        if new_chain:
            self.chain = new_chain.chain


    def pickle(self):
        bytestream = pickle.dumps(self)
        hex_data = binascii.hexlify(bytestream)
        return hex_data.decode('utf-8')


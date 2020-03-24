import hashlib
import json
from time import time

class Blockchain(object):
	def __init__(self):
		self.chain = []
		self.current_transactions = []
		# Creates the genesis block
		self.new_block(previous_hash = 1, proof = 100)

	def new_block(self, proof, previous_hash = None):
		'''
		Creates a new Block in blockchain
		paremeters -
		proof - Proof given by proof of work algorithm
		previous_hash - Hash of the previous block
		return new block 
		'''
		block = {
			'index' : len(self.chain) + 1,
			'timestamp' : time(), 
			'transactions' : self.current_transactions,
			'proof' : proof,
			'previous_hash' : previous_hash or self.hash(self.chain[-1])
		}
		# Reset current list of transactions
		self.current_transactions = []
		
		self.chain.append(block)
		return block

	def new_transaction(self, sender, recipient, amount):
		'''
		Adds a new transaction to the list of transactions
		parameters:
		sender - Address of the sender
		recipient - Address of the recipient
		amount - Amount sent
		returns index of the block holding this transaction
		'''
		self.current_transactions.append({
			'sender' : sender,
			'recipient' : recipient,
			'amount' : amount,
		})
		return self.last_block['index'] + 1

	def proof_of_work(self, last_proof):
		'''
		-Find a number q such that hash(pp') contains 4 leading zeros
		-p is the previous proof, p' is the new proof
		parameters-
		last_proof - p as mentioned above
		returns new proof
		'''
		proof = 0
		while self.valid_proof(last_proof, proof) is False:
			proof += 1

		return proof

	@static_method
	def valid_proof(last_proof, proof):
		'''
		Validated the proof:Checks if hash(last_proof, proof)
		contains 4 leading zeros
		parameters-
		last_proof - previous proof
		proof - new proof
		returns True if hash(last_proof, proof) contains 4 leading zeros
		otherwise False 
		'''

	@property
	def last_block(self):
		# Returns the last block in the chain
		return self.chain[-1]

	@static_method
	def hash(block):
		'''
		Creates a SHA-256 hash of block
		parameters - 
		block - Block to be hashed
		return string denoting hash of the block		
		'''
		block_string = json.dumps(block, sort_keys = True).encode()
		return hashlib.sha256(block_string).hexdigest()
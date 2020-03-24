import hashlib
import json
from time import time
from urllib.parse import urlparse

class Blockchain(object):
	def __init__(self):
		self.chain = []
		self.current_transactions = []
		self.nodes = set()
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

	def register_node(self, address):
		'''
		Add a new node to the list of nodes
		parameters-
		address - Address of the node
		'''
		parsed_url = urlparse(address)
		self.nodes.add(parsed_url.netloc)

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

	def valid_chain(self, chain):
		'''
		Determine if given blockchain is valid
		parameters-
		chain - A blockchain
		return True if chain is valid, otherwise False
		'''
		last_block = chain[0]
		current_index = 1

		while current_index < len(chain):
			block = chain[current_index]
			print(f'{last_block}')
			print(f'{block}')
			print('\n-------------------\n')
			# Check if the hash of the block is correct
			if block['previous_hash'] != self.hash(last_block):
				return False

			# Check if proof of work is correct
			if not self.valid_proof(last_block['proof'], block['proof']):
				return False

			last_block = block
			current_index += 1

		return True

	def resolve_conflicts(self):
		'''
		Resolves conflicts by replacing our chain with the longest one
		in the network
		returns true if chain was replaced, otherwise false
		'''

		neighbours = self.nodes
		new_chain = None
		max_length = len(self.chain)

		# Verify the chains from all nodes in the network
		for node in neighbours:
			response = requests.get(f'http://{node}/chain')

			if response.status_code == 200:
				length = response.json()['length']
				chain = response.json()['chain']

				# Check if current chain is longer and valid 
				if length > max_length and self.valid_chain(chain):
					max_length = length
					new_chain = chain

		if new_chain:
			self.chain = new_chain
			return True

		return False
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

	@staticmethod
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
		guess = f'{last_proof}{proof}'.encode()
		guess_hash = hashlib.sha256(guess).hexdigest()
		return guess_hash[:4] == "0000"

	@property
	def last_block(self):
		# Returns the last block in the chain
		return self.chain[-1]

	@staticmethod
	def hash(block):
		'''
		Creates a SHA-256 hash of block
		parameters - 
		block - Block to be hashed
		return string denoting hash of the block		
		'''
		block_string = json.dumps(block, sort_keys = True).encode()
		return hashlib.sha256(block_string).hexdigest()
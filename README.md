# Blockchain

Basic implementation of blockchain.

## Requirements

Refer to [requirements.txt](https://github.com/h-sinha/Blockchain/blob/master/requirements.txt)

## How to use?
* Start the server using 
```
python api.py
```
* Use cURL/Postman to interact with the server

## API Endpoints
### GET
* [/nodes/resolve](#get-nodesresolve)
* [/mine](#get-mine)
* [/chain](#get-chain)
### POST
* [/transactions/new](#post-transactionsnew)
* [/nodes/register](#post-nodesregister)


#### GET /nodes/resolve 
resolves any conflicts to ensure a node has the correct chain
```
curl -X GET 'http://127.0.0.1:5000/nodes/resolve'
```
#### GET /mine
Tells the server to mine a new block
```
curl -X GET 'http://127.0.0.1:5000/mine'      
```
#### GET /chain 
Returns the full blockchain
```
curl -X GET 'http://127.0.0.1:5000/chain'      
```
#### POST /transactions/new
Adds transaction to the block
```
curl -d '{"sender":"9054bcbc206f4302b24e444cf14fbbf2", "recipient":"4082372a3ae14e9f8269d5a3f5635dad", "amount":5}' \
-H "Content-Type: application/json" \
-X POST "http://localhost:5000/transactions/new" 
```
#### POST /nodes/register
Accepts a list of new nodes in the form of URL
```
curl -d '{"nodes":"[http://127.0.0.1:5000]"}' \
-H "Content-Type: application/json" \
-X POST http://localhost:5000/nodes/register
```

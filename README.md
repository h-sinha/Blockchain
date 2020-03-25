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
Resolves any conflicts to ensure a node has the correct chain
<br/>
**Response** -
```
  // If chain is replaced
  {
      "message":"Our chain was replaced",
			"new_chain": {
            "index": 1,
            "previous_hash": 1,
            "proof": 100,
            "timestamp": 1585109749.6412468,
            "transactions": []
        },
        {
            "index": 2,
            "previous_hash": "09ca41697b5302feb1adee193aea709d50e90d88a5ca457990c6ed200673f740",
            "proof": 35293,
            "timestamp": 1585109762.8534253,
            "transactions": [
                {
                    "amount": 1,
                    "recipient": "a805d46ad4db4503974ab87eb8b9baf1",
                    "sender": "0"
                }
            ]
        }
  }
  // Chain is not replaced
  {
      "message":"Our chain is authoritative",
			"new_chain": {
            "index": 1,
            "previous_hash": 1,
            "proof": 100,
            "timestamp": 1585109749.6412468,
            "transactions": []
        },
        {
            "index": 2,
            "previous_hash": "09ca41697b5302feb1adee193aea709d50e90d88a5ca457990c6ed200673f740",
            "proof": 35293,
            "timestamp": 1585109762.8534253,
            "transactions": [
                {
                    "amount": 1,
                    "recipient": "a805d46ad4db4503974ab87eb8b9baf1",
                    "sender": "0"
                }
            ]
        }
  }
```
#### GET /mine
Tells the server to mine a new block.
<br/>
**Response** -
```
  {
       "index": 2,
       "message": "New Block Forged",
       "previous_hash": "09ca41697b5302feb1adee193aea709d50e90d88a5ca457990c6ed200673f740",
       "proof": 35293,
       "transactions": [
        {
            "amount": 1,
            "recipient": "a805d46ad4db4503974ab87eb8b9baf1",
            "sender": "0"
        }
      ]
  }
```
#### GET /chain 
Returns the full blockchain.
<br/>
**Response**
```
  {
      "chain": [
          {
              "index": 1,
              "previous_hash": 1,
              "proof": 100,
              "timestamp": 1585109749.6412468,
              "transactions": []
          },
          {
              "index": 2,
              "previous_hash": "09ca41697b5302feb1adee193aea709d50e90d88a5ca457990c6ed200673f740",
              "proof": 35293,
              "timestamp": 1585109762.8534253,
              "transactions": [
                  {
                      "amount": 1,
                      "recipient": "a805d46ad4db4503974ab87eb8b9baf1",
                      "sender": "0"
                  }
              ]
          }
      ],
      "length": 2
  }
```
#### POST /transactions/new
Adds transaction to the block.
<br/>
**Parameters**
<br/>
|          Name | Required |  Type   | Description                                                                                                                                                           |
| -------------:|:--------:|:-------:| --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|     `sender` | required | string  | Address of the sender (eg-*"9054bcbc206f4302b24e444cf14fbbf2"*)|
|        `recipient` | required | string  | Address of the recipient (eg-*"9054bcbc206f4302b24e444cf14fbbf2"*) |
| `amount` | optional | integer | Amount of money transferred.|

**Response**
 ``` 
  {
    "message": "Transaction will be added to Block 3"
  }
 ```
#### POST /nodes/register
Accepts a list of new nodes in the form of URL.
<br/>
**Parameters**
<br/>
|          Name | Required |  Type   | Description                                                                                                                                                           |
| -------------:|:--------:|:-------:| --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|     `nodes` | required | list of strings  | Each string in the list denotes a node.<br/> eg - "nodes":["http://127.0.0.1:5000", "http://127.0.0.1:5001"]|


**Response**
 ``` 
  {
      "message": "New nodes have been added",
      "total_nodes": [
          "127.0.0.1:5000",
          "127.0.0.1:5001"
      ]
  }
 ```

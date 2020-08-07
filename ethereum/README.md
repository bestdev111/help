### Install the correct version of Truffle

```
npm un -g truffle
npm i -g truffle@nodeLTS
```

### List available truffle console commands

```
help ?
```

### List accounts

```
accounts
> [
    '0xbBE9936F8e3A6A72E2B22485a5c481F09A98102c',
    '0xCaD247fCd9e808C139E52d9886a8d39D119470c0',
    etc...
  ]
```

### List networks and deployed contract addresses within

```
networks

> Network: development (id: 1590486038876)
    Migrations: 0x13269027cB270BfBbF989DC12dB73a6B31DB4304
    MyContract: 0xfA72444090CA289c615F2A0b81A2f4a8ae32140A
```


### Get general info

```
web3.eth.getNodeInfo() // Gets info about the node connected to
web3.eth.getBlockNumber() // Gets the latest block number
web3.eth.getBlock('latest') // Gets the latest block info
web3.eth.getTransactionFromBlock(10) // Gets the transaction in block #
```

### Migrate contracts from a project

```
truffle console
compile
migrate
```

### Deploy a new contract instance manually

```
let newInstance = await MyContract.new()
```

### Use a contract at a specific address

```
let specificInstance = await MyContract.at("0x1234...");
```

### Get contract instance in truffle console

```
let instance = await MyContract.deployed()
Object.keys(instance)
instance.address
instance.name.call()

// Call method on a public uint256 => ... mapping
instance.tokenIdToStarInfo.call('123129')
```

### Get transaction details

```
let tx = await web3.eth.getTransaction('0x0de...')
web3.utils.isHex(tx.input) // true
web3.utils.hexToAscii(tx.input)
```

### Debug a transaction

```
debug 0x0de8a5ce364e86ea5e50d9c4f0df6faab0594a2ef222dafa39274f72dd0ef717
```

### Get the next nonce for an account

```
web3.eth.getTransactionCount(accounts[0])
```

### Convert BN (BigNumber) object to a readable value

You may get a BN (BigNumber) object returned in the truffle console.
To convert it to a readable string representation do the following:

```
> price = await i.starsForSale(1)

undefined

> price

BN {
  negative: 0,
  words: [ 5177344, 20581667, 33, <1 empty item> ],
  length: 3,
  red: null
}

> price.toString(10) // convert the number to base 10 and return as a string

'150000000000000000'
```

### Get contract events in truffle console

```
var instance = await FlightSuretyApp.deployed()
instance.getPastEvents('OracleRequest', {fromBlock: 6}, function(error, events){ console.log(events); })
```

### Add breakpoint in a separate contract while debugging

This will place a breakpoint at line 4 for SquareLib.sol contract.

```
b SquareLib:5
```

### Load a contract via web3js api in the truffle console

```
artifact = require('./build/contracts/SimpleStore.json')
meta = new web3.eth.Contract(artifact.abi, '0x7aa0b9C10E73E1732cBf84cEaE5635A39ab76E3B')
```

### Using web3 in a node js repl

```
const Web3 = require('web3')
web3 = new Web3('http://localhost:8545')
web3.eth.getTransaction('0x37ee16fc9e1b471b9b3d6323cec1b899cb6c3340379b5c5d2ff28eed067ff10a').then((_tx) => tx = _tx)
web3.eth.call({to: tx.to, data: tx.input}).then((e, r) => console.log(e)).catch((e) => console.log("Looks like a problem: ", e.message))
```
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
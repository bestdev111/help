### Install the correct version of Truffle

```
npm uninstall -g truffle
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

Use `networks --clean` to clean up!

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

### Recover / Export a Private Key from a Geth Keystore file

```
// to use this utility point the `datadir` to the parent folder of the
// geth keybase directory, set the password and the address and run the file
// `node utils/export-pk`

var keythereum = require("keythereum");
var datadir = "./";
const password = "mypass";
let address = '0x123...'

var keyObject = keythereum.importFromFile(address, datadir);
var privateKey = keythereum.recover(password, keyObject);
console.log(privateKey.toString('hex'));
```

### String comparison using keccak256

Solidity doesn't have native string comparison, so we compare their keccak256 hashes to see if the strings are equal:

```
// check the _name param is the same as 'DADOU'
require(keccak256(abi.encodePacked(_name)) == keccak256(abi.encodePacked("DADOU")));
``

### Time in solidity

Solidity also contains the time units seconds, minutes, hours, days, weeks and years. These will convert to a uint of the number of seconds in that length of time. So 1 minutes is 60, 1 hours is 3600 (60 seconds x 60 minutes), 1 days is 86400 (24 hours x 60 minutes x 60 seconds), etc.

```
uint lastUpdated;

// Set `lastUpdated` to `now`
function updateTimestamp() public {
  lastUpdated = now;
}

// Will return `true` if 5 minutes have passed since `updateTimestamp` was
// called, `false` if 5 minutes have not passed
function fiveMinutesHavePassed() public view returns (bool) {
  return (now >= (lastUpdated + 5 minutes));
}
```

### Passing structs and arrays by reference to other functions as storage

You can pass a storage pointer to a struct as an argument to a private or internal function. This is useful, for example, for passing around our Zombie structs between functions.

```
function _doStuff(Zombie storage _zombie) internal {
  // do stuff with _zombie
}
```

### Function modifiers with arguments

```
// Modifier that requires this user to be older than a certain age:
modifier olderThan(uint _age, uint _userId) {
  require(age[_userId] >= _age);
  _;
}

// Must be older than 16 to drive a car (in the US, at least).
// We can call the `olderThan` modifier with arguments like so:
function driveCar(uint _userId) public olderThan(16, _userId) {
  // Some function logic
}
```

### Calldata data location

`Calldata` is somehow similar to `memory`, but it's only available to external functions.

```
function changeName(uint _zombieId, string calldata _newName) external aboveLevel(2, _zombieId) {};
```

### Function modifiers

* **private** means it's only callable from other functions inside the contract;
* **internal** is like private but can also be called by contracts that inherit from this one;
* **external** can only be called outside the contract;
* **public** can be called anywhere, both internally and externally.

### State modifiers

* **view** tells us that by running the function, no data will be saved/changed.
* **pure*** tells us that not only does the function not save any data to the blockchain, but it also doesn't read any data from the blockchain.

Both of these don't cost any gas to call if they're called externally from outside the contract (but they do cost gas if called internally by another function).

### Withdraw ether function

Example of a function to withdraw ether from a smart contrqact.

```
contract GetPaid is Ownable {
  function withdraw() external onlyOwner {
    address payable _owner = address(uint160(owner()));
    _owner.transfer(address(this).balance);
  }
}
```

### Random numbers

Example below using `keccak256`. Note, of course, this method is vulnerable to attack by a dishonest node.

```
// Generate a random number between 1 and 100:
uint randNonce = 0;
uint random = uint(keccak256(abi.encodePacked(now, msg.sender, randNonce))) % 100;
randNonce++;
uint random2 = uint(keccak256(abi.encodePacked(now, msg.sender, randNonce))) % 100;
```

How could this be exploited?

If I were running a node, I could publish a transaction only to my own node and not share it. I could then run the coin flip function (for example) to see if I won — and if I lost, choose not to include that transaction in the next block I'm solving. I could keep doing this indefinitely until I finally won the coin flip and solved the next block, and profit.

### Generate MD5 of all .sol files in a contracts directory

```
find contracts -name *.sol -exec md5 {} \;
```
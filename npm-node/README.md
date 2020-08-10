## npm

List all local packages

```
npm list
```

List all global packages

```
npm list -g
```

List a specific global package (e.g. serverless)

```
npm list -g serverless
```

List available versions of a package:

```
npm view @openzeppelin/contracts versions
```

List / View details about a specific package (note `view`, `show` & `info` are all alias):

```
npm view @openzeppelin/contracts
```

Set the default version of node for the system (e.g. version 12.x)

```
nvm alias default 12
```

Use a specific version of node (e.g. version 12)

```
nvm use 12
```

View the global node_modules path

```
npm root -g
```

Linking a local module into a local project

For example, you want to load a locally cloned module into a local project so that you can easily test changes to that module

Taken from [this article](https://medium.com/@alexishevia/the-magic-behind-npm-link-d94dcb3a81af)

```
# Clone some random node module like randomstring!
cd ~/Desktop
git clone git@github.com:klughammer/node-randomstring.git

# Run npm link in that modules folder
cd ~/Desktop/node-randomstring
npm link

# In your local project run npm link linked-module-name e.g.
cd ~/Desktop/my-project
npm link randomstring

# Now require that module like normal:
# ~/Desktop/my-project/app.js
const randomstring = require("randomstring");
console.log(randomstring.generate());
```

### Execute js inline

`node -p "'Dadou'.padEnd(8,'*')"`

### View versions of everything:

`node -p "process.versions"`

### Check V8 version used by Node JS

`node -p 'process.versions.v8'`

### List all V8 options

`node --v8-options | more`

### Check V8 Options that are in progress

`node --v8-options | grep "in progress"`

### Check V8 Options available for the Garbage Collector

`node --v8-options | grep "gc"`

### Check the GC object in a Node REPL (Read Eval Print Loop) session

```js
➜  workspace node
Welcome to Node.js v12.14.1.
Type ".help" for more information.
> v8
{
  cachedDataVersionTag: [Function: cachedDataVersionTag],
  getHeapSnapshot: [Function: getHeapSnapshot],
  getHeapStatistics: [Function: getHeapStatistics],
  getHeapSpaceStatistics: [Function: getHeapSpaceStatistics],
  getHeapCodeStatistics: [Function: getHeapCodeStatistics],
  setFlagsFromString: [Function: setFlagsFromString],
  Serializer: [Function: Serializer],
  Deserializer: [Function: Deserializer],
  DefaultSerializer: [Function: DefaultSerializer],
  DefaultDeserializer: [Function: DefaultDeserializer],
  deserialize: [Function: deserialize],
  serialize: [Function: serialize],
  writeHeapSnapshot: [Function: writeHeapSnapshot]
}
```

### Autocomplete in the Node REPL

```js
> global. <-- Hit TAB key to get all methods availabel !!
global.__defineGetter__      global.__defineSetter__      global.__lookupGetter__      global.__lookupSetter__
global.__proto__ etc...
```

### Access the last result

```js
> _     <-- just use the underscore (_)
```

### Special REPL commands via dot (.)

```js
> . 		<-- Now press TAB to reveal the availabile 'dot' commands
break   clear   editor  exit    help    load    save
```

### Useful dot Node REPL commands

```js
> .help 	<-- Pulls up help screen
> .save 	<-- Save the current REPL session to a text file
> .load 	<-- Load a JS file from the filesystem into the current REPL session
> .editor 	<-- Puts the REPL into an 'editor' multiline mode. Press `CTL + D `when done.
```

### Show the number of processors available to Node

```js
➜  node -p "os.cpus()"
[
  {
    model: 'Intel(R) Core(TM) i5-7360U CPU @ 2.30GHz',
    speed: 2300,
    times: { user: 39954170, nice: 0, sys: 31352730, idle: 137960190, irq: 0 }
  },
  ...etc
]
```

### Reference arguments passed to Node CLI

```js
➜  node -p "process.argv" test dadou
[
  '~/.nvm/versions/node/v12.14.1/bin/node',
  'test',
  'dadou'
]
```

### List ENV variables available to Node

```js
node -p "process.env"
```

### List all outdated modules

```
npm outdated
```

### Serve a folder over http

```
npx serve -s folder
```
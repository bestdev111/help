### Convert a date into a unix epoch timestamp in milliseconds

```
Date.parse('18 Aug 2020 12:00:00 GMT')  // 1597752000000
```

### Convert ms timestampt to date

```
ts_seconds = 1611092338
ts_miliseconds = 1611092338 * 1000
date = new Date(ts_miliseconds)
// 2021-01-19T21:38:58.000Z
```

### Writiing to console on same line

Use `process.stdout` like so (note the `\r` at the end which is the carrage return)

```
process.stdout.write(`tx found ${found} in TTL: \t${ttl}. Slowest TTL: \t${slowestTTL}\r`)
```

### Global Environemnt

The `global` variable what the `window`.

In a node terminal run the following command

```
global
```

### var, let & const keywords

One thing to note is when using `var` the variable is *hoisted*. This means that it will be set to `undefined` at the top of our execution context. This can sometimes cause the runtime output to be unpredicatable / unexpected. Its better to avoid that and use `comst` \ `let` instead.

Another thing is `let` and `const` are **block scoped** rather than **function scoped**. So `let` and `const` are essentially block scoped alternatives to `var` for variabkle declaration. For example:

```
// Function scoped (on global context)
if(2>1) { var secret = '12345'}
console.log(secret) // > '12345'

// Block scoped using let / const
if(2>1) { let secret = '12345'}
console.log(secret) // > ReferenceError: secret is not defined
```

### Function Declaraion

These functions are defined during *parse* time i.e. when the compiler parses the code and begins the hoisting process.

```
function india() {
  console.log('warm')
}
```

### Function invokaton/call/execution

```
india() // here an **execution context** is created!
```

### Function arguments keyword

A reserved keyword that provides a list of arguments passed to a function

```
function marry(person1, person2) {
  console.log('arguments: ', arguments)
}

marry('Danny', 'Sharron')
// arguments:  [Arguments] { '0': 'Danny', '1': 'Sharron' }
```

NOTE: Its not advised to use the `arguments` keyword like this but instead to either convert it to an array using `Array.from` method or to use spread operator as args and then use that in the function. For example:

```
function marry(person1, person2) {
  console.log('arguments: ', arguments)
  console.log(Array.from(arguments)) // [ 'Danny', 'Sharron' ]
}

function marry2(...args) {
  console.log('args', args)
  console.log(Array.from(arguments))
  return args[0] // 'Dadou'
}

marry2('Dadou', 'Jane')
```

### Use strict

The `use strict` declaration acts as a helper to developers to avoid the pitfalls due to the early (bad/confusing) design decisions of javascript that often trip up developers. Adding it causes compiler errors rather than run time errors or runtime bugs!

Put the `use strict` statement at the top of a file so the the JS engine will avoid global variable leakage issues and require that you define lexical variables using `var`, `let` or `const`.

```
'use strict'

function wierd() {
  height = 10
}
```

Another thing use strict prevents is the use of the `this` keyword within a function that belongs to the global scope:

```
function a() {
  console.log(this) // global
}

function b() {
  'use strict'
  console.log(this) // undefined
}
```

### IIFE - Immediately Invoked Function Expression

Useful for creating a custom separate execution context - perhaps for booting an application or a library. Example:

```
(function() {
  // code
})();
```

### this keyword

The main two reasons for the `this` keyword are:

1. Gives methods access to their containing object
1. Execute same code for miltiple objects

The `this` keyword refers to whatever the function belongs to. So just typing `this` in an empty file refers to the global context. In an object it refers to the object like so:

```
const obj = {
  name: 'Darren',
  sing() {
    return 'lalala ' + this.name // this is the instance of obj
  },
  singAgain() {
    return this.sing() + '!!'
  }
}

obj.sing() // lalala Darren
obj.singAgain() // lalala Darren !!
```

The second property we can write a function once using `this` and wherever it is run will determin what `this` is! Example:

```
function importantPserson() {
  return this.name
}

obj1 = {
  name: 'Darren',
  importantPserson: importantPserson
}

obj2 = {
  name: 'Mike',
  importantPserson: importantPserson
}

obj1.importantPserson() // Darren
obj2.importantPserson() // Mike
```

IMPORTANT: `this` is not lexically scoped its dynamically scoped meaning it based on where it is called. See this example:

```
const obj = {
  name: 'Dadou',
  sing() {
    console.log('a', this)
    var anotherFunc = function() {
      console.log('b', this)
    }
    anotherFunc()
  }
}

obj.sing() // a: obj scope, b: global scope (!!)
```

We see that the scope of `this` when `anotherFunc` is called is surprisingly the global scope! Its due to the fact that the `this` keyword is dynamically scoped. So `sing()` is called on the obj and `anotherFunc` is called within sing which binds this to the global scope!

The way to fix this is to use arrow function notation:

```
var anotherFunc = () => {
  console.log('b', this)
}
```

### call() apply() bind()

Use `call()` and `apply()` to 'borrow' a function from another object. For example:

```
const wizard = {
  name: 'Dumbledore',
  health: 100,
  heal() {
    return this.health +=100;
  }
}

const archer = {
  name: 'Robin Hood',
  health: 30
}

wizard.heal()
// Here we call the wizards heal function using call and pass in the archer so that he is healed
wizard.heal.call(archer)
```

If the function has params these can be passed in too. Apply is the same as call but takes its parms as an array:

```
const wizard = {
  name: 'Dumbledore',
  health: 100,
  heal(a,b) {
    return this.health +=100 + a + b;
  }
}

wizard.heal.call(archer, 10, 20)
wizard.heal.apply(archer, [10, 20])
```

### function currying

Currying refers to giving a function just a partial set of parameters so that you can create more specific versions of the same function for use later on.

For example:

```
function multiply(a,b) {
  return a*b
}

const multiplyByTwo = multiply.bind(this,2)
multiplyByTwo(4)
```

### Clone objects

Its necessary to use `Object.assign` (or the spread operator) to clone objects since objects are passed by reference in Javascript.

```
let obj = {a: 'a', b: 'b', c: 'c'}
let clone = Object.assign({}, obj)

// Now obj and clone are separate objects
obj.c = 5
clone.c = 10
```

Using the spread operator

```
let clone = {...obj}
```

### Deep clone of objects

The above is just a shallow clone. A deep clone can be achived in the following way:

```
let deepClone = JSON.parse(JSON.stringify(obj))
```

NOTE: For large objects this can be quite intensive!

### Clone arrays

Its necessary to use `array.concat` (or the spread operator) to make a copy of an array since arrays are objects and objects are passed by reference in Javascript.

```
let arrA = [1,2,3]
let arrB = arrA.concat([])

arrA.push(1600050000)
arrB.push(1800000000)

console.log(arrA)
console.log(arrB)
```

Using the spread operator also works like this:

```
let arrB = [...arrA]
```

### Object.create

Use `Object.create` to create the `__proto__` link between hierarchay of objects.

```
const elfFunctions = {
  attack: function() {
    return 'atack with ' + this.weapon
  }
}
function createElf(name, weapon) {
  //Object.create creates __proto__ link
  newElf = Object.create(elfFunctions)
  newElf.name = name;
  newElf.weapon = weapon
  return newElf
}
```

### ES6 Classes

Syntactic sugar classes in Javascript.

```
class Elf {
  constructor(name, weapon) {
    this.name = name;
    this.weapon = weapon;
  }
  attack() {
    return 'atack with ' + this.weapon
  }
}
```

### this keyword bindings

4 ways to bind the `this` keyword.

```
// new binding
function Person(name, age) {
  this.name = name;
  this.age =age;
  console.log(this);
}

const person1 = new Person('Xavier', 55)

//implicit binding
const person = {
  name: 'Karen',
  age: 40,
  hi() {
    console.log('hi' + this.name)
  }
}

person.hi()

//explicit binding
const person3 = {
  name: 'Karen',
  age: 40,
  hi: function() {
    console.log('hi' + this.setTimeout)
  }.bind(window)
}

person3.hi()

// arrow functions (lexically bind and without it 'this' would be the window object)
const person4 = {
  name: 'Karen',
  age: 40,
  hi: function() {
    var inner = () => {
      console.log('hi ' + this.name)
    }
    return inner()
  }
}

person4.hi()
```

### Inheritance

Using the `extends` keyword and the `super` keyword in the consttructor function we are able to create inheritance like so:

```
class Character {
  constructor(name, weapon) {
    this.name = name;
    this.weapon = weapon;
  }
  attack() {
    return 'atack with ' + this.weapon
  }
}

class Elf extends Character {
  constructor(name, weapon, type) {
    super(name, weapon)
    this.type = type;
  }
}
```

### Spread operators

With array spread operators we can do this:

```
arr = [1,2,3,4,5]

function add(a,b,c,d,e) {
  return a+b+c+d+e;
}

add(...arr)
```

With Object spread operators we can do this:

```
animals = {
  monkey: 1,
  bird: 20,
  tiger: 6,
  lion: 8
}

const { monkey, ...rest } = animals

console.log(monkey) // 1
console.log(rest) // { bird: 20, tiger: 6, lion: 8}
```

### Promises

Promises act as an improvment on callbacks.

A basic promise definition looks like this:

```
promise = new Promise((resolve, reject) => {
  if(true) {
    resolve('Hi')
  } else {
    reject('Error!')
  }
})
```

A promise is called with the `then` function and also optionally with a `catch`. Promises can also be changed with multiple calls to then, as you can see below:

```
promise
  .then((result) => result + '!')
  .then((result) => result + '?')
  .then(console.log) // 'Hi!?'
  .catch(console.error('Something went wrong'))
```

Resolving in multiple promises using `Promise.all`. In the below example, all the promises must complete before being returned as an array of results. So in this case, even though promise1 completes in 1 second, the output will resolve in 3 seconds because of promise2. Thank.

```
promise1 = new Promise((resolve, reject) => {
  setTimeout(resolve, 1000, 'Ello?')
})

promise2 = new Promise((resolve, reject) => {
  setTimeout(resolve, 3000, 'Ello, My Friend??')
})

Promise.all([promise1, promise2])
  .then(console.log) //[ 'Ello?', 'Ello, My Friend??' ]
```

### Fetch API Example

The browser [Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API) is promise based and works just the same way, for example:

```
fetch('https://jsonplaceholder.typicode.com/todos/10')
  .then(response => response.json())
  .then(json => console.log(json))
```

If need to fetch data from several APIs, then it is possible like so:

```
urls = [
  'https://jsonplaceholder.typicode.com/users',
  'https://jsonplaceholder.typicode.com/posts',
  'https://jsonplaceholder.typicode.com/albums'
]

Promise.all(urls.map(url =>
  fetch(url).then(resp => resp.json())
)).then(array => {
  console.log('Users: ', array[0])
  console.log('Posts: ', array[1])
  console.log('Albums: ', array[2])
})
```

### Async / Await

Async / Await is part of ES8 and is built on top of `Promises` (see above). Below is an example of using the same Fetch API example above using Async / Await:

```
async function fetchUsers() {
  const resp = await fetch('https://jsonplaceholder.typicode.com/users')
  const data = await resp.json()
  console.log(data)
}

fetchUsers()
```

Below is an example using the multiple url fetching example from above:

```
async function getData() {
  const [ users, posts, albums ] = await Promise.all(urls.map(url =>
    fetch(url).then(resp => resp.json())
  ))
  console.log('Users ', users)
  console.log('Posts ', posts)
  console.log('Albums ', albums)
}

getData()
```

### For await of

Allows to loop through an array of promises. Below is an example:

```
// use the urls array from above example..
const getData = async function() {
  const arrayOfPromises = urls.map(url => fetch(url))
  for await (let request of arrayOfPromises) {
    const data = await request.json()
    console.log(data)
  }
}
```
### Parallel / Sequential / Race Promise operations

A full example below showing each type of execution

```
const promisify = (item, delay) =>
  new Promise((resolve) =>
    setTimeout(() =>
      resolve(item), delay));

const a = () => promisify('a', 100);
const b = () => promisify('b', 5000);
const c = () => promisify('c', 3000);

async function parallel() {
  const promises = [a(), b(), c()];
  const [output1, output2, output3] = await Promise.all(promises);
  return `prallel is done: ${output1} ${output2} ${output3}`
}

async function race() {
  const promises = [a(), b(), c()];
  const output1 = await Promise.race(promises);
  return `race is done: ${output1}`;
}

async function sequence() {
  const output1 = await a();
  const output2 = await b();
  const output3 = await c();
  return `sequence is done ${output1} ${output2} ${output3}`
}

sequence().then(console.log)
parallel().then(console.log)
race().then(console.log)
```

### Handling errors in Async / Await using Try / Catch blocks

**Always** use try/catch blocks in your Async / Await code! For example:

```
(async function() {
  try {
    await Promise.reject('oopsie')
  } catch (err) {
    console.error(err)
  }
  console.log('This is still good!')
})()
```

If you don't have the catch then you will see `UnhandledPromiseRejectionWarning` when running this in Node JS.

### Modules

In JS applications there is scope which is structured like so:

* Global Scope
* * Module Scope
* * * Function Scope
* * * * Block Scope (let / const)

### Revealing module pattern

Below is what was done before the introduction of modules in JS:

```
var globalParams = 'other modules, variables, data etc...'

var myModule = (function() {
  var harry = 'potter'
  var vold = 'mort'

  function fight(char1, char2) {
    return `Hahaha ${char1} wins!`
  }
  // note we only export / return the fight function and keep everything else private
  return {
    fight: fight
  }
})(params) // note how we can pass in params to the scope and keep it separate from global

myModule.fight('dadou', 'nesnej')
```

### CommonJS

This is a way to require modules that loads them in syncronously. This makes it more useful with Node JS and looks like this:

```
var module1 = require('module1') //.fight optionally select the methods

function myFunction() {}

module.exports = {
  fn: myFunction
}
```

To use CommonJS in a browser / web app, developers would typically use [browerify](http://browserify.org/) or [webpack](https://webpack.js.org/) to bundle all the modules together into a single `bundle.js` file that has the dependencies already correctly managed within.

So when writing Node JS apps that run on a server or desktop (i.e. not in a browser) then we will use the CommonJS approach.

### ES6 modules

In your module file, use the [`export` statement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/export) or `export default` statement for the items you want to make available to others from your module.

In the consuming file, use the [`import` statement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import) to import the desired items from your module.

Example module (called script.js)

```
const harry = 'potter'
const voldmort = 'he who cannot be named'

export function jump() {
  return 'high!'
}

export default function fight(char1, char2) {
  return 'who will win?'
}
```

Example usage (import the default only):

```
import fight from 'script'
```

Example usage (import the default and the non-defaults):

```
import fight, { jump } from 'script'
```

### Convert decimal to hex and back to decimal

```
decimal = 100
hexStr = decimal.toString(16) // '64'
yourNumber = parseInt(hexStr, 16) // 10
```

### Useful Javascript sleep function

Basically using a Promise to resolve in a certain number of ms by using setTimeout to call the Promise resolve.

```
function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}
```
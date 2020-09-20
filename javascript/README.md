### Convert a date into a unix epoch timestamp in milliseconds

```
Date.parse('18 Aug 2020 12:00:00 GMT')  // 1597752000000
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

### Function Expression

These functions are defined during *run* time. This is becuase anything declared using `var` keyword is hoisted and set to `undefined`.

```
var canada = function() {
  console.log('cold')
}
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

Another thing use strict prevents is the use of the `this` key word within a function that belongs to the global scope:

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

To take the example further, in a namespeaced library you might use:

```
var fancylib = (function() {
  function doSomethingFancy() {
    return 'looking good!'
  }
  return {
    doSomethingFancy: doSomethingFancy
  }
})()

// Use like so:
fancylib.doSomethingFancy()
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

### Closures

A closeure is a fucntion that keeps its scope available for future invokation:

```
const foo = (string) => (name1) => (name2)=> { console.log(`${string} ${name1} ${name2}`) }

foo('hi')('darren')('nesnej')

const fooString = foo('hi')
// fooString is a clousere with the string param set

// it can be called anytime like this:
fooString('darren')('nesnej')
```

Classic example. Note if we change var to let above then the let keyword creates a variable scope for the variable and fixies the issue.

```
// hete the output will be 4,4,4,4
const array = [1,2,3,4];
for(var i=0; i < array.length; i++) {
  setTimeout(function(){
    console.log('I am at index ' + i)
  }, 3000)
}
```
Of couerse, another way to fix this is wtih closures:

```
// here the output is as expected 1,2,3,4
const array = [1,2,3,4];
for(var i=0; i < array.length; i++) {
  (function(closureI) {
    setTimeout(function(){
      console.log('I am at index ' + array[closureI])
    }, 3000)
  })(i)
}
```

### Prototypal Inheritance

Use `__proto__` to add to the chain - this is just for an example. There are more efficient ways of doing this (see later).

Remember that `__proto__` is a pointer to the `prototype` object up chain. So the functions like `bind()` are actually declared in the `Function` prototype (notice the capital 'F'). Only functions have the `prototype` object and these are used as constructors to create instances that point to the prototype and inherit the properties of it.

```
let dragon = {
  name: 'Tanya',
  fire: true,
  fight() {
    return 5
  },
  sing() {
    if (this.fire) {
      return `I am ${this.name}, the breather of fire`
    }
  }
}

let lizard = {
  name: 'Kiki',
  fight() {
    return 1
  }
}

// Don't do this, bad performance. Show with bind.
lizard.__proto__ = dragon;
dragon.isPrototypeOf(lizard);
console.log(lizard.fire)
console.log(lizard.sing())
const lizardFire =dragon.sing.bind(lizard)
console.log(lizardFire())
```

The correct way to do inheritance is to use `Object.create` like so:

```
// Create our own prototypes:
var human = {mortal: true}
var socrates = Object.create(human);
human.isPrototypeOf(socrates); // true
```

Using Prototypal Inheritance to add functionality to existing Javascript functions. Below are a couple of examples.

NOTE: using `prototype` like this is not the easiest way to do this. See later for me OO styles!


```
//Date object => to have method .lastYear() which shows you yesterday's day in 'YYYY-MM-DD' format.
Date.prototype.lastYear = function(){
  return this.getFullYear() - 1;
}

new Date('1900-10-10').lastYear()
```

And another example changing the behavior of map. NOTE: this is 'monkey patching' and not recommended to do with core Javascript methods like this! This is just for example.

```
//Array.map() => to print '🗺'
Array.prototype.map = function()  { // what happens with arrow function here?
  arr = [];
  for (let i = 0; i < this.length; i++) {
    arr.push((this[i]+'🗺'));
  }
  return arr;
}
console.log([1,2,3].map())

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

### Constructor Functions

Are just like constructors that you might normally see in an OO `Class` definition. Some considerations are that Constructor Functions in JavaScript do not have a `return` statement and must always start with a capital letter so that its clear to other developers that this is a constructor function and needs to be called with `new`.

```
//Constructor Functions
function Elf(name, weapon) {
  this.name = name;
  this.weapon = weapon;
}

Elf.prototype.attack = function() {
  return 'atack with ' + this.weapon
}

const sam = new Elf('Sam', 'bow');
const peter = new Elf('Peter', 'bow');
sam.attack()
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

Resolving in multiple promises using `Promise.all`. In the blow example, all the promises must complete before being returned as an array of results. So in this case, even though promise1 completes in 1 second, the output will resolve in 3 seconds because of promise2. Thank.

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



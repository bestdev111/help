### Function Expression

These functions are defined during *run* time. This is becuase anything declared using `var` keyword is hoisted and set to `undefined`.

```
var canada = function() {
  console.log('cold')
}
```

### Using IIFE for creating namespaced libraries

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
// here the output will be 4,4,4,4
const array = [1,2,3,4];
for(var i=0; i < array.length; i++) {
  setTimeout(function(){
    console.log('I am at index ' + i)
  }, 3000)
}
```
Of course, another way to fix this is wtih closures:

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
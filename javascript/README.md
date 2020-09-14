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
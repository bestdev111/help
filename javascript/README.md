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
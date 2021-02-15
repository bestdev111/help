## Functional Programming

Try out this cool game, [Cube Composer](https://david-peter.de/cube-composer/), to learn functional programming.

Use functionst that:

* Perform a single task only
* Return data (input -> process -> output)
* Are Pure Functions (see below)
* Do not share state
* Immutable state
* Composable
* Predictable

### Pure Functions

No side effects and given the same input returns the same output.

### Idempotence

Ability to call the function many times with the same input and recive the same output. Helps make code predictable.

### Imperative vs. Declerative

A good example is a for loop is *Imperative* because its quite detatiled in its instructions.

```
for(let i=0; i< 1000; i++>) {
  console.log(i)
}
```

A forEach array method is more *Declerative* since we are not telling the computer what to do exactly:

```
[1,2,3].forEach(item => console.log)
```

Another example of *Imperative* programming use is `jQuery` and another example *Declerative* would be `React`.

### Immutablility

Should not change the state. Always copy the state and return the copy.

### Partial Application

### Closures as private variables

One common use case for clousres is to encapsultae a private variable and expose it via a getter method, like so:

```
const closure = function() {
  let count = 55;
  return function getCounter() {
    return count;
  }
}

const getCounter = closure()
getCounter() // 55
```

### Currying

The action of taking a function and breaking it down into multiple functions each with a single argument. For example:

```
const multiply = (a, b) => a * b
const curriedMultiply = (a) => (b) => a * b
curriedMultiply(5)(20)
const multiplyBy5 = curriedMultiply(5)
multiplyBy5(20) // 100
```

### Partial Application

The act of breaking a function down so that there some of the parameters wrapped as a closure and the remaining parameters are kept. So applying some of the parameters and use a partial set of these, for example if we have a function with 3 params like so:

```
const multiply = (a, b, c) => a * b * c
const partialMultiplyBy5 = multiply.bind(null, 5)
partialMultiplyBy5(10, 20)
```

By the way, the *curried* version of this would be to break this down into several functions *each with a single param* so it would look like this:

```
const curriedMultiply = (a) => (b) => (c) => a*b*c
curriedMultiply(3)(4)(10)
```

### Functional Programming example: Amazon Shopping Cart

Below is a simple example that uses functional programming to update the users cart, add them to the purchases, add tax and empty the cart - all using a compose function.

```
const user = {
  name: 'Kim',
  active: true,
  cart: [],
  purchases: []
}

// Note you can also use a library such as Ramda (https://ramdajs.com/)
const compose = (f, g) => (...args) => f(g(...args))

const purchaseItem  = (...fns) => fns.reduce(compose);

purchaseItem(
  emptyUserCart,
  buyItem,
  applyTaxToItems,
  addItemToCart
)(user, {name: 'laptop', price: 50})


//https://wiki.developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/assign
function addItemToCart(user, item) {
  const updatedCart = user.cart.concat(item)
  return Object.assign({}, user, {cart: updatedCart});
}

function applyTaxToItems(user) {
  const {cart} = user;
  const taxRate = 1.3;
  const updatedCart = cart.map(item => {
    return {
      name: item.name,
      price: item.price*taxRate
    }
  })
  return Object.assign({}, user, { cart: updatedCart });
}

function buyItem(user) {
  const itemsInCart = user.cart;
  return Object.assign({}, user, { purchases: itemsInCart });
}
function emptyUserCart(user) {
  history1.push(user)
  return Object.assign({}, user, { cart: [] });
}
```

## Examples

Taken from [this freecodecamp post](https://www.freecodecamp.org/news/functional-programming-principles-in-javascript-1b8fc6c3563f/).

### Pure functions

Remember that pure functions:

* Return the same result if given the same arguments (it is also referred as deterministic)
* Do not cause any observable side effects

Below is an example for returning the same result given the same args:

```
const calculateArea = (radius, pi) => radius * radius * pi;
calculateArea(10, PI); // returns 314.0
```

Below is an example for not mutating external variables:

```
let counter = 1;

const increaseCounter = (value) => value + 1;

increaseCounter(counter); // 2
console.log(counter); // 1
```

### Immutability

The following mutates the state:

```
var values = [1, 2, 3, 4, 5];
var sumOfValues = 0;

for (var i = 0; i < values.length; i++) {
  sumOfValues += values[i];
}

sumOfValues // 15
```

For each iteration, we are changing the i and the sumOfValue state. But how do we handle mutability in iteration? Recursion.

```
let list = [1, 2, 3, 4, 5];
let accumulator = 0;

function sum(list, accumulator) {
  if (list.length == 0) {
    return accumulator;
  }

  return sum(list.slice(1), accumulator + list[0]);
}

sum(list, accumulator); // 15
list; // [1, 2, 3, 4, 5]
accumulator; // 0
```

Another example using function chaining:

```
const string = " I will be a url slug   ";

const slugify = string =>
  string
    .toLowerCase()
    .trim()
    .split(" ")
    .join("-");

slugify(string); // i-will-be-a-url-slug
```

### Referential transparency

Given the function:

```
const square = (n) => n * n;
```

We always get the same output for a given input:

```
square(2); // 4
square(2); // 4
square(2); // 4
```

So basically: `pure functions + immutable data = referential transparency` which means we can memoize some of the parameters to create new functions (see above for examples).

### Functions as first-class entities

Functions as first-class entities can:

* refer to it from constants and variables
* pass it as a parameter to other functions
* return it as result from other functions

Lets say we have two functions like so:

```
const doubleSum = (a, b) => (a + b) * 2;
const doubleSubtraction = (a, b) => (a - b) * 2;
```

Notice that they both multiply the result by 2.

We can extract this logic out into a new function and then we have a more fine grained set of composable functions that we can use to create the same logic.

Below we have a sun function, subtaction function and a doubleOperator function that takes a function, two inputs and applys the function to the two inputs and then doubles the result:

```
const sum = (a, b) => a + b;
const subtraction = (a, b) => a - b;

const doubleOperator = (f, a, b) => f(a, b) * 2;

doubleOperator(sum, 3, 1); // 8
doubleOperator(subtraction, 3, 1); // 4
```

### Higher-order functions

When we talk about higher-order functions, we mean a function that either:

* takes one or more functions as arguments, or
* returns a function as its result

#### Filter

For example the Array.filter() function is a higher-order function:

```
const even = n => n % 2 == 0;
const listOfNumbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
listOfNumbers.filter(even); // [0, 2, 4, 6, 8, 10]
```

#### Map

Below example, builds a sentence from an array of objects:

```
var people = [
  { name: "TK", age: 26 },
  { name: "Kaio", age: 10 },
  { name: "Kazumi", age: 30 }
];

const makeSentence = (person) => `${person.name} is ${person.age} years old`;

const peopleSentences = (people) => people.map(makeSentence);

peopleSentences(people);
```

Another example to return an array with only its absolute values:

```
let values = [1, 2, 3, -4, 5];

const updateListMap = (values) => values.map(Math.abs);

updateListMap(values); // [1, 2, 3, 4, 5]
```

#### Reduce

Common example to calculate the sum of items in a shopping basket:

```
let shoppingCart = [
  { productTitle: "Product 1", amount: 10 },
  { productTitle: "Product 2", amount: 30 },
  { productTitle: "Product 3", amount: 20 },
  { productTitle: "Product 4", amount: 60 }
];

const sumAmount = (currentTotalAmount, order) => currentTotalAmount + order.amount;

const getTotalAmount = (shoppingCart) => shoppingCart.reduce(sumAmount, 0);

getTotalAmount(shoppingCart); // 120
```

### Combining Map + Reduce

```
const getAmount = (order) => order.amount;
const sumAmount = (acc, amount) => acc + amount;

function getTotalAmount(shoppingCart) {
  return shoppingCart
    .map(getAmount)
    .reduce(sumAmount, 0);
}

getTotalAmount(shoppingCart); // 120
```
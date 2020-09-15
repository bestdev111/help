## Functional Programming

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
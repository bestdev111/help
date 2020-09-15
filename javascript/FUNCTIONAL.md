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


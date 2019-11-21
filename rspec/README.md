# Rspec

...

# Rspec-mocks

Check out full docs [here](https://github.com/rspec/rspec-mocks)

## Mock any instnace of a method

```
allow_any_instance_of(SomeClass).to receive(:some_method).and_return("Wibble")
```

## Check specific parameters are received

```
expect(SomeClass).to receive(:some_method).with(param1, param2 etc)
```
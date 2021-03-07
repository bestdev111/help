### Lists and Recursion

Some examples:

```
defmodule MyList do
  def len([]),               do: 0
  def len([ _head | tail ]), do: 1 + len(tail)

  def square([]),              do: []
  def square([ head | tail ]), do: [ head*head | square(tail) ]

  def add_1([]),              do: []
  def add_1([ head | tail ]), do: [ head+1 | add_1(tail) ]

  def map([], _func),             do: []
  def map([ head | tail ], func), do: [ func.(head) | map(tail, func) ]

  def sum([], total),              do: total
  def sum([ head | tail ], total), do: sum(tail, head+total)

  def reduce([], value, _) do
    value
  end

  def reduce([head | tail], value, func) do
    reduce(tail, func.(head, value), func)
  end
end
```

### Swapping Example

```
defmodule Swapper do
  def swap([]), do: []
  def swap([ a, b | tail ]), do: [ b, a | swap(tail) ]
  def swap([_]), do: raise "Can't swap a list with an odd number of elements"
end
```

### Recursive pattern matching and lists of lists

```
defmodule WeatherHistory do

  def test_data do
    [
     [1366225622, 26, 15, 0.125],
     [1366225622, 27, 15, 0.45],
     [1366225622, 28, 21, 0.25],
     [1366229222, 26, 19, 0.081],
     [1366229222, 27, 17, 0.468],
     [1366229222, 28, 15, 0.60],
     [1366232822, 26, 22, 0.095],
     [1366232822, 27, 21, 0.05],
     [1366232822, 28, 24, 0.03],
     [1366236422, 26, 17, 0.025]
    ]
  end

  def for_location([], _target_loc), do: []

  def for_location([ head = [_, target_loc, _, _ ] | tail], target_loc) do
    [ head | for_location(tail, target_loc) ]
  end

  def for_location([ _ | tail], target_loc), do: for_location(tail, target_loc)

end
```

Concatenate Lists

```
iex> [1,2,3] ++ [3,4,5]
[1, 2, 3, 3, 4, 5]
```

Flatten Lists

```
iex> List.flatten([[[1], 2], [[[3]]]])
[1, 2, 3]
```

### Folding (similar to reduce, but can choose direction)

Folds (reduces) the given list from the left with a function. Requires an
accumulator.

```
iex> List.foldl([1, 2, 3, 4], 0, fn x, acc -> x - acc end)
iex> 2
```

### List.replace_at

Returns a list with a replaced value at the specified index.

```
iex> List.replace_at([1, 2, 3], 0, 0)
iex> [0, 2, 3]
```

### List.keyfind

Receives a list of tuples and returns the first tuple where the element at
position in the tuple matches the given key.

```
iex> keypairlist = [{:name, "DADOU"}, {:job, "Progrmmer"}, {:location, "Phnom Penh", "Cambodia"}]
iex> List.keyfind(keypairlist, "DADOU", 1)
iex> {:name, "DADOU"}
iex> List.keyfind(keypairlist, "Cambodia", 2)
iex> {:location, "Phnom Penh", "Cambodia"}
iex> List.keyfind(keypairlist, "Cambodia", 1)
iex> nil
iex> List.keyfind(keypairlist, "Cambodia", 1, "Cambodia does not have a city called Cambodia")
iex> "Cambodia does not have a city called Cambodia"
```
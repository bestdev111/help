# Ruby Programming Tips

https://blog.arkency.com/2014/07/hidden-features-of-ruby-you-may-dont-know-about/?utm_source=Arkency+Newsletter&utm_campaign=d0d1efa031-Welcome_in_Arkency_Newsletter9_5_2014&utm_medium=email&utm_term=0_4cee302d8a-d0d1efa031-104134847

Tested using Ruby version 2.6.4p104

```
ruby --version
ruby 2.6.4p104 (2019-08-28 revision 67798)
```

## Binary Numbers

Representing binary in Ruby terminal (prefix with `0b`)

```
irb(main):0> 0b110111
=> 55
```

Using the `str.to_i(base=10)` method.

```
irb(main):0> "110111".to_i(2)
=> 55
```

Usiing the `int.to_s(base=10)` method.

```
irb(main):0> 55.to_s(2)
=> "110111"
```

# Number 0

Checking if a number is zero or not.

```
irb(main):0> 0 == 0
=> true
irb(main):0> 0.zero?
=> true
irb(main):0> 1.zero?
=> false

# nonzero? returns self unless it is zero in which case nil is returned

irb(main):0> 0.nonzero?
=> nil
irb(main):0> 1.nonzero?
=> 1
```

# Random numbers and dates

Get a random integer within a specific range e.g between 1 and 100

```
irb(main):0> rand(1..100)
=> 6
```

...or a random birth date with an age between 20 and 40

```
irb(main):0> require 'active_support/core_ext'
irb(main):0> rand(40.years.ago..20.years.ago).to_date
=> Mon, 14 Jun 1993
```

# Introspection / meta programming

A method that returns its own name!

```
def introduce1
  __method__
end

def introduce2
  __callee__
end

irb(main):0> introduce1
=> :introduce1
irb(main):0> introduce2
=> :introduce2
```

# Hash / Array / Zip

Some examples of creating a Hash from an Array.

```
irb(main):0> ("a".."c").zip(1..3)
=> [["a", 1], ["b", 2], ["c", 3]]
irb(main):0> _.to_h
=> {"a"=>1, "b"=>2, "c"=>3}

irb(main):0> colors = ["cyan", "magenta", "yellow", "white"];
=> ["cyan", "magenta", "yellow", "white"]
irb(main):0> Hash[*colors]
=> {"cyan"=>"magenta", "yellow"=>"white"}
```
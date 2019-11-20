## Passing Arguments

Pass args via the command line is the easiest as follows

```
> make some_task foo=bar
> bar
```

The `some_task` task is defined as follows

```
some_task:
	@echo $(foo)
```
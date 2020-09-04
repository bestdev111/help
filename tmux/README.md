## Tmux

Note: Tmux uses prefix and command key style so this means to split your single pane into a left and a right pane you press Ctrl and b at the same time, release both, and then type the % key (see below for list of commands).

Tmux is useful for being able to manage terminal windows by splitting and creating new windows. The advantage is when connecting to a remote server via SSH its possible to start a tmux session and split windows and create windows all within the single SSH session!

Its also possible to manage sessions by detaching and attaching to existing sessions. Useful for long running processes or if the connection drops and you want to get back into a previously started session.

### Start a Tmux session

```
tmux
```

### Split panes (Left/Right)

```
C-b %
```

### Split panes (Top/Bottom)

```
C-b "
```

### Kill / remove a pane

```
C-b x
```

### Switching panes

```
C-b (arrow keys)
```

### Make current pane full screen

```
C-b z
```

### New Session Window / Tab

```
C-b c
```

### Switch windows

```
# Pervious windwow
C-b p
# Next window
C-b n
# Nth window
C-b <number>
```

### Detach from a current session

```
C-b d
```

### List available sessions

```
tmux ls
```

### Attach to the first session

Note that the -t 0 is the parameter that tells tmux which session to attach to. “0” is the first part of your tmux ls output.

```
tmux attach -t 0
```

### Create named sessions

```
tmux new -s gethsync
```

### Rename an exisitng session

```
tmux rename-session -t 0 gethsync
```

### Attach to a named session

```
tmux attach -t gethsync
```

### Display help in a Tmux session

```
C-b ?
```
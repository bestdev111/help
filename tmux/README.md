## Tmux

Note: Tmux uses prefix and command key style so this means to split your single pane into a left and a right pane you press Ctrl and b at the same time, release both, and then type the % key (see below for list of commands).

Tmux is useful for being able to manage terminal windows by splitting and creating new windows. The advantage is when connecting to a remote server via SSH its possible to start a tmux session and split windows and create windows all within the single SSH session!

Its also possible to manage sessions by detaching and attaching to existing sessions. Useful for long running processes or if the connection drops and you want to get back into a previously started session.

## Session Managment

### Start a Tmux session

```
tmux
```

### Create named sessions

```
tmux new -s gethsync
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

### Rename an exisitng session

```
tmux rename-session -t 0 gethsync
```

### Attach to a named session

```
tmux attach -t gethsync
```

### Kill / delete a detached session

```
tmux kill-session -t geth
```

### Display help in a Tmux session

```
C-b ?
```

## Pane / Window Managment

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

### Resize the pane

 To resize tmux panes, you’ll first want to hit your prefix — ctrl + b by default — and then the colon key :. What this does is brings up a prompt at the bottom of your screen.

 Now you’ll want to type in resize-pane in the prompt, followed by a hyphen - and either D, U, L, R.

 ```
:resize-pane -D (Resizes the current pane down)
:resize-pane -U (Resizes the current pane upward)
:resize-pane -L (Resizes the current pane left)
:resize-pane -R (Resizes the current pane right)
:resize-pane -D 10 (Resizes the current pane down by 10 cells)
:resize-pane -U 10 (Resizes the current pane upward by 10 cells)
:resize-pane -L 10 (Resizes the current pane left by 10 cells)
:resize-pane -R 10 (Resizes the current pane right by 10 cells)
 ```

 Check this for more information on [resizing Tmux Panes](https://michaelsoolee.com/resize-tmux-panes/#:~:text=To%20resize%20tmux%20panes%2C%20you,%2C%20U%2C%20L%2C%20R%20.).

### Saving / Restoring tmux sessions

You need [two tools](https://arcolinux.com/everything-you-need-to-know-about-tmux-reconstructing-tmux-sessions-after-restarts/) to help with this:

* Use [tmux-resurrect](https://github.com/tmux-plugins/tmux-resurrect) for manual save / restore
* Use [tmux-continuum](https://github.com/tmux-plugins/tmux-continuum) for auto save and restor on server reboot

Use the following commands to save / restore on demand:

* Save - `prefix + Ctrl-s`
* Restore - `prefix + Ctrl-r`
* Install - `prefix + I`
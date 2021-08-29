# Visual Studo Code for Mac Tips

## Searching

* `Ctrl + P` - Search for files

* `Ctrl + T` - Search for symbols in open files

* `FN + SHIFT + F12` - Search for all references of a symbol in all open files

## Multi Cursor

* `Ctrl + D` - Apply a cursor to the _next instance_ of the current selected text in the current file

* `Ctrl + U` - UNDO the last selected cursor

* `Ctrl + Shift + L` - Apply a cursor to every instance of the selected text in this current file

## File Navigation

* `CTRL + TAB` - switch between open files by selection

* `FN + F8` - navigate between errors / problems (as reported under the 'PROBLEMS' tab) in all files

* `Ctrl + OPT +T` - close all other files

## Breakpoints

* `FN + F9` - set a breakpoint

* For an example of debugging in VSCode check out [this repo](https://github.com/jensendarren/private-blockchain-star-ownership-tracking#vscode-debugging-the-app-or-with-jest)

## Text editing

* `Ctrl + C` - (_without_ selecting text) will copy the _entire_ line of text where the cursor is currently at. Cutting text works the same.

* `Ctrl + /` - comment out the current line

* `Ctrl + [ or ]` - indent / un-indent current line based on filetype rules

## Find / Text Search

* `Ctrl + F` - find a string in current file.

* `FN + F3` - move to the next occurance of matched string using the Find command as noted above.

* `CTRL + G` - goto a specific line

## Toggle terminal window

1. Open the search bar and type ''
1. Add the following config to the `keybindings.json` file in the array:

```
  {
    "key": "cmd+alt+m",
    "command": "workbench.action.toggleMaximizedPanel",
    "when": "!terminalFocus"
  }
```

1. Now you can use the "cmd+alt+m" shortcut to toggle the VS Code terminal window to fullscreen and pane.

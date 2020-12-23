# Cheat Sheet

Notes, tips and commands.


## File Management


### Open modes

Modes available for `open()` function:

| Character | Meaning                                                                              |
| --------- | -------                                                                              |
| `r`       | Open for reading (default).                                                          |
| `w`       | Open for writing, truncating (clearing) the file first.                              |
| `x`       | Open for exclusive creation, failing if the file already exists.                     |
| `a`       | Open for writing, appending to the end of the file if it already exists.             |
| `b`       | Set mode to binary - used in combination with other modes, eg: `rb` for read binary. |
| `t`       | Text mode (default) - like `b`, this can be used in combination with other modes.    |
| `+`       | Open for updating (reading and writing)                                              |

 > Note: Above table is based on the one from the official documentation for [open()](https://docs.python.org/3/library/functions.html#open).

### Paths

Useful features of the `os` library.

`os.makedirs`


## VSCode

Open command pallet:
 * Windows - `CTRL` + `SHIFT` + `p`
 * macOS - `CMD` + `SHIFT` + `p`


## Python Debugger

Set breakpoint manually in code, add `breakpoint()` to the line you wish to pause exeuction on.

Once in debugger mode, see the below commands to interact with debugger.

 * `step` - Step Into - Move to the next line of code (inside function if necessary)
 * `next` - Step Over - Run the next line of code without moving into functions
 * `continue` - Run all code and step at next breakpoint
 * `quit` - Stop debugging

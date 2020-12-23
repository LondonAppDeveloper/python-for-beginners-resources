# Cheat Sheet

Notes, tips and commands.


## Command Line

Tips for using the Terminal on macOS and Command Prompt on Windows.

### Command Prompt (Windows)

To open the Command Prompt:
 
 1. Click on **Start**.
 2. Type **cmd** in search.
 3. Click on the Command Prompt icon (black box).
 
> Tip: Right click and add a shortcut to either the Task Bar, Start Menu or Desktop for easier access in the future.


### Terminal (macOS)

To open the Terminal:

 1. Open the **Finder** application.
 2. Select **Applications** on the left.
 3. Navigate to **Utilities**.
 4. Double click **Terminal** to open it.
 
> Tip: Drag the appliction to your launcher, or press `CMD + SPACR` and type *Terminal* for easier access in the future.


### Commands

List of common commands:

 * `cd <path>`: Change directory, for example to change to a directory called `code` you would type `cd code/`.
 * `cd ..`: Change to the parent directory.
 * `ls` (macOS) or `dir` (Windows): List all the files and directories are the current location.
 * `pwd`: Print Working Dir - Output the current path that you are working from.
 * `python <path>`: Run a Python script, for example, to run a script called `hello.py` you would run `python helloy.py`.
 * `mkdir <name>`: Created a directory with a given name.

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

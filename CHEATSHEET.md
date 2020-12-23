# Cheat Sheet

Notes, tips and commands which are useful to know when learning Python.

> Note: To open links a new tab, use use `CMD + LEFT CLICK` (macOS) or `CTRL + LEFT CLICK` (Windows).


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


## VSCode

Open command pallet:

 * Windows - `CTRL` + `SHIFT` + `p`
 * macOS - `CMD` + `SHIFT` + `p`


## Basic Python Syntax

It's important to remember that Python uses blank spaces (tabs) to distinguish blocks of code.

This is typically done using statemens. Some examples of common statements are described below.


### Comments

Comments are used to add notes to code. It's useful for describing a particular piece of logic if it's not clear by reading it.

To define a comment, prefix the line with a `#`. For example:

```python
# This is a comment
```

Any lines prefixed with `#` are exclusively for information purposes and will not be executed by the Python interpreter (which runs your code).

**When should you use comments?** 

If you are writing code simply for learning, then go wild and add as many comments as you need. However, if you are creating code used for real applications, it's best to limit the use of comments to times when it is needed to explain something that may not be obvious to other developers at first glance. For example, if you need to write some code to work around an issue which may not be obvious, you can use a comment to explain the reason.


### Defining a Function

Functions are used to create blocks of code that can be re-used with different inputs (optional) and product an output (optional).

See an example of a simple function below:

```python
def my_function():
    """My function description."""
    # CODE.
```

The above code defines a function called `my_function`. After it's defined, you can use it by typing `my_function()`, and the code indenteded under the function will be executed.

Functions may accept inputs in the form of parameters. For example:

```python
def my_function(param1, param2, param3):
    """Function which does something with 3 parameters."""
    # Code
```

In the above example, you can pass values (arguments) to the function when you call it. These arguments values are then accessible inside the function code. This enables you to re-use the same code with different inputps.

Function may generate a value which is output from the code inside the function using the `return` statement. For example:

```python
def add_numbers(a, b):
    """Add a and b and return result."""
    result = a + b
    
    return result
```

In the above example, you can add two numbers together and get the result by writing the following code:

```python
total = add_numbers(2, 2)
```

This will set `total` to `4`.

The code inside the function will stop executing as soon as the first `return` statement is reached.

### Operators

Python supports a number of "operators" for performing different calculations and checks. Some of common ones are described below:

 * `==`: Check for equality, in other words, you can use this to check if one value if equal to another. For example, `1 == 1` will be `True` and `1 == 2` will be `False`. It's useful for comparing variables etc...
 * `!=`: Inverse of `==`, checking that one value does not equal the other. For example `1 != 1` will be `False`, and `1 != 2` will be `True`. 
 * `>=`: Greater than or equal to
 * `<=`: Less than or equal to
 * `<`: Less than
 * `>`: Greater than


## Python Debugger

Set breakpoint manually in code, add `breakpoint()` to the line you wish to pause exeuction on.

Once in debugger mode, see the below commands to interact with debugger.

 * `step` - Step Into - Move to the next line of code (inside function if necessary)
 * `next` - Step Over - Run the next line of code without moving into functions
 * `continue` - Run all code and step at next breakpoint
 * `quit` - Stop debugging


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

 * `os.makedirs(name, mode=0o777, exist_ok=False)`: Make all directories in the path (provided as name). For example, if you run `os.makedirs('one/two/three/')`, then three directories will be created: `one`, `two` and `three` being being added in the previous parent. Also see [official docs](
https://docs.python.org/3/library/os.html#os.makedirs).
 * `os.path.join(path, *paths)`: Join paths together in a platform agnostic manor. This is useful for creating paths our of multiple path segments without hard coding the path style to a particular OS format. For example, if you call `os.path.join('one', 'two', 'three.txt')`, then on Windows the path willbe `one\two\three.txt` and on macOS it will be `one/two/three.txt`. This is useful for creating code that works on all platforms. (Also see [official docs](https://docs.python.org/3/library/os.path.html#os.path.join)).
 * `os.path.expanduser(path)`: Create a path relative to the users home directory. One Windows, the users home directory us usually `C:\Users\<name>` and on macOS machines the home directory is usually `/Users/<name>/`. This function gives you the ability to generate the correct path regardless of what operating system you run your code on. (See [official docs](https://docs.python.org/3/library/os.path.html#os.path.expanduser)).
 
 

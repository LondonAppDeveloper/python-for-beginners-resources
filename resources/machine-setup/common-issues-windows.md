# Common Issues (Windows)

This document describes common installation issues and solutions.

## Command `python` not found

The command reasons for this are:

 1. Python is not installed.
 2. Python is not added to the system `PATH`.
 
I suggest uninstalling Python and re-installing from scratch, ensuring you check the **Add to PATH** button on the first screen.


## Incorrect version of Python

If you run `python --version` and get a response such as `2.7.x`, this is usually because you have an older version of Python installed on your machine.

I suggest trying the following:
 1. Open **Add/Remove Programs** (found in **Control Panel**).
 2. Uninstall all versions of Python listed.
 3. Download **Python 3.9** from [python.org](https://www.python.org/).
 4. Install **Python 3.9**.

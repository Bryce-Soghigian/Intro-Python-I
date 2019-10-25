"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""


# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE

# Print out the OS platform you're using:
# YOUR CODE HERE

# Print out the version of Python you're using:
# YOUR CODE HERE

import sys
import os
print("\n***CL ARGUMENTS***\n", sys.argv[0])
print("\n***OS PLATFORM***\n", sys.platform)
print("\n***PYTHON VERSION***\n", sys.version)
print("\n***PROCESS ID***\n", os.getpid())
print("\n***CURRENT WORKING DIRECTORY***\n", os.getcwd())
print("\n***LOGIN NAME***\n", os.getlogin())
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE

# Print the current working directory (cwd):
# YOUR CODE HERE

# Print out your machine's login name
# YOUR CODE HERE

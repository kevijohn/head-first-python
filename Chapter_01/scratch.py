# Author: Kevin Johnson
# Created date: JAN 17 2022

# This file is for running code that's scattered through the text

from os import getcwd
import sys

where_am_I = getcwd()
print("I am here:", where_am_I)

print("platform is:", sys.platform)
print("version is:", sys.version)

# This is interesting, didn't get this from Zed's book
for ch in "Hi!":
    print(ch)

for num in range(5):
    print("Head First rocks!", num)

print(list(range(5)))

# To list out functions for a given object/module:
# Import the module FIRST!
# dir(module_name_goes_here)


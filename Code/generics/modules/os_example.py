"""
TASK:
Write to file next:
1) System name like:
    "You use Linux based system" if it is posix or "You use windows based system" if it is nt.
    "This system is not supported" if it is something else
2) Path from where executable is running
3) List of all entries in the current directory
4) Check each entry if it is a directory or file
    entity1: directory
    entiry2: file
5) Randomly got to any directory and write to file a name of a path and a list of all entries in this path
"""

import os
import random

f = open("os_info.txt", "w")

# task 1
f.write("TASK 1\n")

name = os.name
if name == "nt":
  f.write("You use windows based system\n")
elif name == "posix":
  f.write("You use linux based system\n")
else:
  f.write("This system is not supported\n")
###

# task 2
f.write("TASK 2\n")

f.write(f"{os.getcwd()}\n")
###

# task 3
f.write("TASK 3\n")

for entity in os.listdir():
  f.write(f"{entity}, ")
f.write("\n")
###

# task 4
f.write("TASK 4\n")

for entity in os.listdir():
  if os.path.isfile(entity):
    f.write(f"{entity}: File\n")
  else:
    f.write(f"{entity}: Directory\n")
###

# task 5
f.write("TASK 5\n")

directories = []

for entity in os.listdir():
  if os.path.isdir(entity):
    directories.append(entity)

os.chdir(random.choice(directories))

f.write(f"{os.getcwd()}\n")

for entity in os.listdir():
  f.write(f"{entity}, ")
f.write("\n")

###

f.close()

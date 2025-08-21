# Introduction 

Having a file that has been changed by multiple branches may trigger a merging conflict, which pauses the merge process until the conflict is resolved. This activity illustrates scenarios that may or may not trigger a merging conflict. If there is a merging conflict, you are asked to decide how to resolve the conflict. 

# Scenario 1

Create a local repository named "sc1" and a file named **main.py** with the following content (do not correct the code): 

```
def feet_to_meters(value):
    retun value * 0.3048

feet = float(input('? '))
print(f'{feet}ft = {feet_to_meters(feet)}mt')
```

Next, commit the repository with **main.py** and message "initial commit". 

Now switch to a new branch named "bugfix" to fix the error in **main.py**. Commit the changes with the message "fix return mispell in feet_to_meters". 

Switch back to the "main" branch and add the following function: 

```
def meters_to_feet(value):
    return value / 0.3048
```

Also, update the "main" code to: 

```
choice = input('f2m or m2f? ')
value = float(input('? '))
if choice == 'f2m':
    print(f'{value}ft = {feet_to_meters(value)}mt')
else: 
    print(f'{value}mt = {meters_to_feet(value)}ft')
```

Commit the changes using the message "meters_to_feet function added". 

Perform a merge using "bugfix" as the source. Did any merge conflict happen? Explain. Was the "bugfix" update incorporated in **main.py**? 

if you need to add message if you get a conflict
1. type i
2. enter message then enter
3. type :wq

# Scenario 2

Create a local repository named "sc2" and a file named **main.py** with the content from scenario 1: 

```
def feet_to_meters(value):
    return value * 0.3048

def meters_to_feet(value):
    return value / 0.3048

choice = input('f2m or m2f? ')
value = float(input('? '))
if choice == 'f2m':
    print(f'{value}ft = {feet_to_meters(value)}mt')
else: 
    print(f'{value}mt = {meters_to_feet(value)}ft')
```

Commit the updates. 

Branch out to "quick_and_dirty" and modify both functions in the following way: 

```
def feet_to_meters(value):
    return round(value * 0.3048, 2)

def meters_to_feet(value):
    return round(value / 0.3048, 2)
```

Commit the changes and switch back to main. Update the same functions but now in the following way: 

```
import math 

def feet_to_meters(value):
    return math.ceil(value * 0.3048 * 100) / 100

def meters_to_feet(value):
    return math.ceil(value / 0.3048 * 100) / 100
```

Commit the changes and then try to merge from "quick_and_dirty". Did you get a merge conflict? Explain. 
There were conflicts with merging the two files together. One used round python function and other used the math library to round the value

Open the file and see the differences from **main**. Use "Accept Incoming Changes", add the file and make a commit. That's it! You resolved the merging conflict. 
# Exception Handling
def sum(num1, num2):
# Error Handing
    try:
        print(num1+num2)
    except:
        print("there was an error!")
    finally:
        print("this will always to run")



number = input("enter a number")

sum(12,12)


# File IO with Exception Handling
my_file = None
try:
    my_file = open('',mode='r')
    print(my_file.read())
except IOError:
    print("Issus with working with the file")
finally:
    if my_file != None:
        my_file.close()
    print("This will run whether we have an exception or not")

# OS Module

import os

print(os.getcwd())

# Change directory
os.chdir("/user/imtiazahmad/Desktop")

# Get current working directory
print(os.getcwd())

# List contents of directory
print(os.listdir())

if "myfolder" not in os.listdir():
    os.mkdir("myfolder")

# It Creating the folder
os.makedirs("myfolder/subfolder/datafolder")

# Delete specific file
os.remove("myfolder/subfolder/datafolder/myfile.txt")

# Delete specific folder
os.rmdir("myfolder/subfolder/datafolder")

# this is dangerous, removes entiire directory structure
os.removedirs("myfolder/subfolder")

# Traversing Directories

import os

for a, b, c in os.walk("path name"):
    print(a)
    print(b)
    print(c)
    print(" ------------- ")

# OS Module Continued

import os

for a, b, c in os.walk("path name"):
    pass

# Get basename.. that's the file at the directory location given
print(os.path.basename("path name"))

# Get the directory name only, not the file
print(os.path.dirname("path name"))

# Will given directory name and basenaaqme in a tuple
print(os.path.split("path name"))


"""list"""
# List is ordered and changeable
# Creating a List of numbers
listone = [3,7,3,6]
print(listone)

"""Tuples"""
# Tuple ordered and unchangeable
# Creating a Tuple
my_tuple = (0, 5, 8, 2)
print(my_tuple)

"""set"""
# Set is unordered, unchangeable
# Creating a set
my_set = {"a", "b", "c"}
print(my_set)

""" dictionaries"""
# Dictionary is ordered and changeable
def dict_manipulation():
    my_dict = {
        "name": "guhan",
        "year": 2001
    }

    # insert a new key/value
    my_dict["dob"] = "23-10-2001"
    print(my_dict)

    # delete a key
    my_dict.pop("year")
    print("my_dict output after popping year: " + my_dict)


"""for"""
def _for():
    """ Get range and print 1 to 20 """
    arr = range(20)
    for i in arr:print(i)
    return "Guhan"

print(_for())

"""while"""
i = 1
# Using while loop
while i < 6:
  print(i)
  if (i == 3):
      # insert a new break
    break
  i =i+ 1

"""if"""
i=10
j=20
if i<j:
    print("Holle World")

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

"""function"""
def My_function():
    print("Hello World")

My_function()

"""function calling"""
def My_function1(fname):
    print(fname)

My_function1("guhan")
My_function1("Arun")

"""Number of Arguments in the function """
def My_functiontwo(fname,lname):
    print(fname+" "+lname)
My_functiontwo("guhan1","guhan3")

""" Array """
arr = [2,4,7,5]
# insert a new pop
arr.pop(0)
# insert a new length
print(len(arr))
print(arr)

""" return """
# we are useing return statement
def Myname():
    return 3+2
print(Myname())


if __name__ == "__main__":
    # dict manip
    dict_manipulation()


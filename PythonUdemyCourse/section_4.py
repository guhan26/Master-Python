# if and else
if 5 <6:
    print("year 5 is less than 6")
else:
    print("this will never be printed")

# Elif statement

animal = "cow"

if animal == "cow":
    print("eats grass")
elif animal == "bird":
    print("eats seeds")
elif animal == "monkey":
    print("eats bananas")
else :
    print("we don't know what the animal eats")

# For loop
farm_animals = ['goat','horse','chicken','cow','dog']

for animal in farm_animals:
    print(animal)

greeting = "hello"
counter = 0
for char in greeting:
    if char == "l":
        continue
    print(char)
print("loop is terminated by this point")

#pass statement

mylist = ['computer', 'car','bottle','tv']
for item in 'this is a string':
    print(item)

# while loops
x = 0
while x < 10:

    # x = x + 1
    x += 3
    if x == 6:
        continue
    print(x)
else:
    print("x is not less than 10")

# looping and unpacking
employees = {'mike': 27000,'john':23456,'rebeca':60000,'tom':100000}

for key,value in employees.items():
    print(key)
    print(value)

# Range, zip
word = "hello"
for num in range(2, 10, 2):
    print(num)

mynum = [1,2,3,4,5]
words = ['hello', 'my','name','is']
for item in zip(mynum, words):
    print(item)

# Accepting input from user

name = input('enter the name')
print(5 + int(name))


# Assignment-1
"""
Create a method called twelver that accepts 2 integer arguments: a and b.
The method should return True if one of the arguments is 12
or if the sum of both arguments equals 12.
"""
def twelver(a,b):
    if (a == 12 or b == 12 or a+b == 24):
        return True
    else:
        return False

print(twelver(12,12))

# output:- True

# Assignment-2
"""
Create a method called pay_extra that accepts 2 parameters:
 working, and hour. This method will be used to decide whether
 an employee will receive extra pay or not. If an employee is working
 during the hrs of 8pm until 8am in the morning, that means they
 should be paid extra. In that situation the method should return true,
 otherwise it should return false.
"""
def pay_extra(working, hour):
    if(working  and (hour < 8 or hour > 20)):
        return True
    else:
        return False

print(pay_extra(2,10))

# output:- False

# Assignment-3

"""
Given a list of ints, return True if the sequence of numbers 1, 2, 3
appears in the list anywhere, false otherwise.
"""
def sequence(num_list):
    for i in range(len(num_list) - 2):
        if num_list[i] == i and num_list[i+1] == 2 and num_list[i+2] ==3:
            return True

    return False
print(sequence([1,2,3,1,1]))

# output:- False

# Assignment-4
"""
Given a non-empty string like "Code" return a string like "CCoCodCode".
"""
def grow_string(str):
    result =""
    for i in range(len(str)):
        result = result + str[:i +1]

    return result
print(grow_string("code"))

# output:- ccocodcode

# Assignment-5
"""
Define a method that accepts a list as an argument
and returns True if one of the first_folder 4 elements
in the list is a 6. The list length may be less than 4.
"""
def first3(numbers):
    end = len(numbers)
    if end > 4:
        end = 4
    for i in range(end): # loop over index 0,1,2,3
        if numbers[i]==6:
            return True
    # if we get here, the loop is over and we didn't find a 6
    return False

print(first3([1,2,6,3,0,0]))
print(first3([1,2,3,3,0,6]))

# output:- True
#          False

# Assignment-6
"""
Create a function called last2 that accepts a string argument.
The function should return the count of the number of times that the last
2 characters appear in the rest of the string. You should not count
the last 2 characters as an occurrence. The last 2 characters is just the
sequence your function should look for in the remaining string.
"""
def last2(str):
    if len(str) <= 2:
        return 0

    last2 = str[len(str)-2:]
    count = 0

    for i in range(len(str) - 2):
        sub = str[i : i+2]
        if sub == last2:
            count = count+1

    return count

print(last2('xxhixxhixxhixx'))

# output:- 3

# Assignment-7
"""
Given 2 strings, a and b, return the number of the positions where
they contain the same length 2 substring. So "xxcaazz" and "xxbaaz"
yields 3, since the "xx", "aa", and "az" substrings appear in the same
place in both strings.
"""
def string_match(a,b):
    # figure out the which string shorter
    shorter = min(len(a),len(b))

    count =0
    for i in range(shorter -1):
        a_sub = a[i: i+2] # gives us substring of size 2
        b_sub = b[i: i+2]
        if a_sub == b_sub:
            count = count + 1

    return count

print(string_match('abc' , 'abc'))
print(string_match('abc' , 'xyz'))

# output:- 2
#          0

# Assignment-8
"""
Return the sum of the numbers in the list, except ignore sections of
numbers starting with a 7 and extending to the next 8
(every 7 will be followed by at least one 8).
Return 0 for no numbers.
"""

def sum78(nums):
    sum = 0
    in_range = False

    for i in range(len(nums)):
        if nums[i] == 7:
            in_range = True

        if in_range == False:
            # sum = sum + nums[i]
            sum = sum + nums[i]

        if nums[i] == 8:
            in_range = False

    return sum

print(sum78([1,2,2]))
print(sum78([1,2,2,7,99,99,8]))

# output:- 5
#          5

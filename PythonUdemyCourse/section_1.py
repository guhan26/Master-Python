# Assignment -1

"""
    We would like to get the remainder of 15 divided by 4.
    The calculation below does not seem to give us this result.
    How would you change the code to meet the requirement?

"""
remainder = 15 % 4
print(remainder)

# output:- 3

# Assignment -2

"""
Use of the below format() method is incorrect for what we are trying to do.
We actually have 10 small, 12 large, and 12 medium boxes.
Write code to correct this:
"""

print("we have {2} small boxes, {2} large boxes, {2} medium boxes".format(10, 12, 12))

# output:- we have 12 small boxes, 12 large boxes, 12 medium boxes

# Assignment -3
"""
    Given 2 variables chars and word, write code to move
    the data contained in the variable word in the exact middle of
    the characters contained in the variable chars and save this
    in a new variable called result and print it.

    NOTE: chars variable will contain only 4 characters
"""
char = "[[]]"
word = "cool"
print(char[:2] + word + char[2:])

# output:- [[cool]]

# Assignment -4
"""
    Given 2 variables word1 and word2, write code to
    print the concatenation of the 2 words omitting the
    first_folder letter of the string saved in word1 and the second_folder
    letter of the string saved in word2.
"""
word1 = "Computer"
word2 = "Truck"
result = word1[1:] + word2[0:1] + word2[2:]
print(result)

# output:- omputerTuck

# Assignment -5
"""
    Given 2 variables chars and word, write code to move
    the data contained in the variable word in the exact middle of
    the characters contained in the variable chars and save this
    in a new variable called result and print it.

    NOTE: chars variable can contain any even number of characters.
          the len() function can be used to figure out the length of a string
"""
chars = "<<[]]]"
word = "cool"
size = len(chars)
idx = int(size/2)

results = chars[:idx] + word + chars[idx:]
print(results)

# output:- <<[cool]]]

# Introduction programming

# Immutable

my_var = "abcdefg"
my = my_var[0]
print(my)

# Basic string Methods

sentence = "this is a sentence"
sen = sentence.capitalize()
print(sen)

#Formatting String

sentence = "I am coming home"
print(sentence[5])
print(sentence[5:10])

# Basic Datatypes

num1 = 2
num2 = 3
num3 = num1 % num2
print(num3)

age =True
data_type = type(age)
print(data_type)

# Basic of variables

print("Hello World")
print("this is the next statement")
number = 77
print("number")
weigth = 88
print(number)
answer = number + weigth
print(answer)

f_name="guhan "
l_name="guru"
name=f_name+l_name
print(name)

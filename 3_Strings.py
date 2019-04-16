# Strings represent text, enclosed in either single quotes or double quotes.

# Some examples:
print("Bucky Roberts is awesome!")
print("I don't think she's 18")
print('She said, "What part of the cow is the meatloaf from?"')

# Escape character with blackslash(\)
print('I don\'t think she\'s 18')

# print() is a built-in Python function
print("hey now brown cow")

# filepath - characters such as \n, \t etc. can't be escaped by default
print("Broken Filepath = ", "C:\Abhijit\temp\nothing")

# Raw string
print("Filepath =  " , r"C:\Abhijit\temp\nothing")

# Like numbers, strings can also be stored in variables
firstName = "Bucky "
lastName = "Roberts"

# Adding two strings have the same effect as concatenating them
print("firstName + lastName = ", firstName + lastName)

# Multiplying a string by an integer is equivalent to self-concatenation with
# itself the said number of times; it can be used to avoid writing repeated print() statements
'''
   * yields an empty string if the multiplier is a non-positive integer
   * throws TypeError if the multiplier is a decimal number
'''
print("firstName * 5 = ", firstName * 5)

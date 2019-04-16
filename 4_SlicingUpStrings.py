# We get one or more characters upon slicing a string!

user = "Tuna McFish"
print("user=", user)

# Indexing in Python is zero-based
print("user[0]=", user[0])

# Retrieving the n-th character
print("user[5]=", user[5])

# Retrieving the last character
print("user[-1]=", user[-1])

# Retrieving the 3rd character from right
print("user[-3]=", user[-3])

# A slice of a string
print("user[2:7]=", user[2:7])

# If start or stop index is not mentioned, extremes are included
print("user[:7]=", user[:7])
print("user[2:]=", user[2:])
print("user[:]=", user[:])

# Another built-in function len() gives the number of characters(length) in a string
print("Length of user:", len(user))

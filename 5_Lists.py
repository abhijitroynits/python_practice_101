# Lists

# Comma-separated elements in square brackets
players = [29, 58, 66, 71, 87]

# Printing the complete list
print("players=", players)

# Printing a list element; a list is zero-indexed
print("players[2]=", players[2])

# Re-assigning an element a different value
# Lists are mutable
players[2] = 68
print("Set players[2] = 68, then players=", players)

# Adding another list to a given list
print("players + [90, 91, 98]=", players + [90, 91, 98])
print("Adding another list on the fly doesn't change the given list permanently!")
print("players=", players)

# Using append() function on a list changes the list in-place(permanently)
players.append(120)
print("After players.append(120), players=", players)

# Slicing can be performed on lists too
print("players[:2]=", players[:2])

# Slicing + Re-assignment to a non-empty list
players[:2] = [0, 0]
print("Set players[:2] = [0, 0]; players=", players)

# Slicing + Re-assignment to an empty list
players[:2] = []
print("Set players[:2] = []; players=", players)

# Emptying a list; deleting all contents but NOT the list
players[:] = []
print("Set players[:] = []; players=", players)


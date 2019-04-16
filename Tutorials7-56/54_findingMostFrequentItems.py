from collections import Counter

text = " We hope to one day become the world's leader " \
       "in free educational resources. " \
       "We are constantly discovering and adding more " \
       "free content to the website everyday. " \
       "There is already an enormous \
        amont of resources online that can be accessed " \
       "for free by anyone in " \
       "the world, the main issue right now is " \
       "that very little of it is organized " \
       "or structured in any way. " \
       "We want to be the solution to that problem."

# Create a list of words
words = text.split()

# Create a Counter object
counter = Counter(words)

# Find the 3 most frequent words
top_three = counter.most_common(3)
print('Three most frequent words:\n ', top_three)

# Experiment on a number list
n_list = [7, 8, 6, 4, 5, 5, 8, 9, 21, 7, 0, 0, 0]
counter = Counter(n_list)
top_four = counter.most_common(4)
print('Four most freq numbers:\n ', top_four)

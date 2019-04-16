# A dictionary is an unordered yet indexed collection of key-value pairs.
# Values in a dictionary are accessed via their keys.
import pprint


classmates = {
    'Tony': 'intelligent but arrogant',
    'Emma': 'sits behind me',
    'Lucy': 'asks too many questions',
    'Bill': 'develops apps'
}

print('Dictionary- ')
pprint.pprint(classmates)

print()
for k, v in classmates.items():
    print(k, '->', v)


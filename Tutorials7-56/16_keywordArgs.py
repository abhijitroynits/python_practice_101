# The idea of keyword args has to do with passing fewer arguments
# Having default args is imperative in such scenarios


def dumb_sentence(subj='Dog', vb='chases', obj='cat'):
    print(subj + ' ' + vb + ' ' + obj)


dumb_sentence()
dumb_sentence(subj='Cats', vb='attack', obj='mice')

# With fewer args, default args in the function definition become more useful
# Also, we can change the order of the named args
dumb_sentence(subj='Raccoon')
dumb_sentence(obj='another dog', vb='kills')

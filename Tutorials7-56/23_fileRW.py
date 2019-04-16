# File Write operation

with open('sample.txt', 'w') as fw:
    fw.write('Writing some text\n')
    fw.write('Added one more line\n')


# File Read Operation

with open('sample.txt', 'r') as fr:
    text = fr.read()
    print(text)



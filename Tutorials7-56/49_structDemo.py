# struct pkg is applied to convert bytes to human-readable format

from struct import *

# Store as bytes data
packed_data = pack('iif', 6, 19, 4.73)
print('\npacked_data=', packed_data)

print('\n#Bytes required to store an integer: ', calcsize('i'))
print('#Bytes required to store a float: ', calcsize('i'))
print('#Bytes required to store an integer-integer-float : ', calcsize('iif'))


# To convert to human-readable format
original_data = unpack('iif', packed_data)
print('\noriginal_data=', original_data)
print('\noriginal data=',
      unpack('iif', b'\x06\x00\x00\x00\x13\x00\x00\x00)\\\x97@'))


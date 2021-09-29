import sys
from ctypes import CDLL, c_uint32

c_lib = CDLL("decoder_lib\\Release\\decoder_lib.dll")
file_name = sys.argv[1]

file_in = open(file_name, 'rb')
file_out = open(file_name + ".out", 'wb')
header = file_in.read(1024)

result = (c_uint32 * 256)()
block = file_in.read(256)
while len(block) == 256:
    block_len = (block[7]-1)*4
    c_lib.decode(block, result)
    file_out.write(bytes(result)[0:block_len])
    block = file_in.read(256)

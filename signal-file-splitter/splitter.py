import binascii

from splitter_fun import find_all, split_data

new_files_ends = ['_Ex.bin', '_Ey.bin', '_Hx.bin', '_Hy.bin']

file_name = '2166116A'
fileExt = 'TS3'
new_file_suffix = fileExt.lower()

file = open(file_name + '.' + fileExt, 'rb')
data = file.read()

marker = data[8:24]
headers = [x-8 for x in find_all(data, marker)]
result = split_data(data, headers, 32)

for index, file_end in enumerate(new_files_ends):
    new_file = open(file_name+new_file_suffix+file_end, 'wb')
    new_file.write(result[index])

# print(binascii.hexlify(marker))
print(headers)

file.close()




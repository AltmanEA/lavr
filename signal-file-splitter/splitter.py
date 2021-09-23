import sys

from splitter_fun import find_all, split_data

files_ext = ['TS3', 'TS4', 'TS5']
# files_ext = ['TS5']
new_files_ends = ['_Ex.bin', '_Ey.bin', '_Hx.bin', '_Hy.bin', '_Hz.bin']
file_name = sys.argv[1]

for ext in files_ext:
    file = open(file_name + '.' + ext, 'rb')
    data = file.read()

    new_file_suffix = ext.lower()
    marker = data[8:12]
    headers = [x-8 for x in find_all(data, marker)]

    result = split_data(data, headers, 32)

    for index, file_end in enumerate(new_files_ends):
        new_file = open(file_name+new_file_suffix+file_end, 'wb')
        new_file.write(result[index])
        new_file.close()

    file.close()


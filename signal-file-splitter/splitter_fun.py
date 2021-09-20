from typing import List


def find_all(string: bytes, pattern: bytes) -> List[int]:
    # find all position pattern in string
    result = []
    i = string.find(pattern)
    while i != -1:
        result.append(i)
        i = string.find(pattern, i + 1)
    return result


def convert_int(source: bytes) -> bytes:
    if source[0] > 127:
        new_byte = 255
    else:
        new_byte = 0
    return bytes([new_byte, source[0], source[1], source[2]])


def split_data(data: bytes, starts: List[int], size: int) -> List[bytearray]:
    # split data, pass size byte for each starts
    new_size = (len(data) - 32 * len(starts)) // 3
    result = [bytearray(new_size), bytearray(new_size), bytearray(new_size), bytearray(new_size)]
    start_iter = iter(starts)
    current_start = next(start_iter)
    i = 0
    j = 0
    while i < len(data):
        if i == current_start:
            i = i + size
            current_start = next(start_iter, -1)
        else:
            result[0][j:j + 4] = convert_int(data[i + 0:i + 3])
            result[1][j:j + 4] = convert_int(data[i + 3:i + 6])
            result[2][j:j + 4] = convert_int(data[i + 6:i + 9])
            result[3][j:j + 4] = convert_int(data[i + 9:i + 12])
            i = i + 12
            j = j + 4
    return result


#       Test
#
# test_marker = bytes([2 * i for i in range(24)])
# test_data = bytes(bytes([100 + i for i in range(8)]) + test_marker + bytes([128+i for i in range(3 * 12)]) +
#                   bytes([110 + i for i in range(8)]) + test_marker + bytes([8 + i for i in range(2 * 12)]))
# test_headers = [i - 8 for i in find_all(test_data, test_marker)]
# print(test_headers)
# test_result = split_data(test_data, test_headers, 32)
# print(test_result)

#!/usr/bin/python3

"""
Module 0-validate_utf8
"""


def validUTF8_v1(data):
    """
    Determines if a given data set
    represents a valid UTF-8 encoding
    """
    count = 0

    if not data:
        return False

    for num in data:
        bin_rep = format(num, '#010b')[-8:]

        if count == 0:
            for bit in bin_rep:
                if bit == '0':
                    break
                count += 1

            if count == 0:
                continue

            if count == 1 or count > 4:
                return False
        else:
            if not (bin_rep[0] == '1' and bin_rep[1] == '0'):
                return False
    return count == 0


def validUTF8(data):
    count = 0

    if data is None:
        return False

    for num in data:
        if count == 0:
            if num & 128 == 0:
                count = 0
            elif num & 224 == 192:
                count = 1
            elif num & 240 == 224:
                count = 2
            elif num & 248 == 240:
                count = 3
            else:
                return False
        else:
            if num & 192 != 128:
                return False
    if count == 0:
        return True
    return False


def validUTF8_v4(data):
    n_bytes = 0

    mask1 = 1 << 7
    mask2 = 1 << 6

    for num in data:
        mask = 1 << 7
        if n_bytes == 0:
            while mask & num:
                n_bytes += 1
                mask = mask >> 1

            if n_bytes == 0:
                continue

            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            if not (num & mask1 and not (num & mask2)):
                return False
        n_bytes -= 1
        return n_bytes == 0

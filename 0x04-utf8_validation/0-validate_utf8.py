#!/bin/usr/python3

def validUTF8(data):
    num_following_bytes = 0

    for byte in data:

        if 128 <= byte <= 191:
            if num_following_bytes == 0:
                return False
            num_following_bytes -= 1
        else:
            if num_following_bytes > 0:
                return False

            if byte < 128:
                num_following_bytes = 0
            elif 192 <= byte <= 223:
                num_following_bytes = 1
            elif 224 <= byte <= 239:
                num_following_bytes = 2
            elif 240 <= byte <= 247:
                num_following_bytes = 3
            else:
                return False


    return num_following_bytes == 0

"""
    Given two binary strings, return their sum (also a binary string).
    The input strings are both non-empty and contains only characters 1 or 0.
"""

def addBinary(a, b):
    """
    :param a: str
    :param b: str
    :return: str
    """
    """
    
    if len(a) < len(b):
        aux = a
        a = b
        b = aux
    a = a[::-1]
    b = b[::-1]
    mind = 0
    c = ""
    for i in range(len(a)):
        if i < len(b):
            sum = int(a[i]) + int(b[i]) + mind
        else:
            sum = int(a[i])  + mind
        if sum == 0:
            c += "0"
        elif sum == 1:
            c += "1"
            mind = 0
        elif sum == 2:
            c +="0"
            mind = 1
        else:
            c += "1"
            mind = 1

    if mind > 0:
        c += "1"
    c = c[::-1]
    return c
    """
    carry = 0
    result = ""
    a = a[::-1]
    b = b[::-1]
    if len(a) < len(b):
        c = a
        a = b
        b = c

    for index in range(len(b)):
        add = int(a[index]) + int(b[index]) + carry
        if add == 0 or add == 1:
            result += str(add)
            carry = 0
        elif add == 2:
            result += str(0)
            carry = 1
        else:
            result += str(1)
            carry = 1
    index = len(b)
    while carry and index < len(a):
        add = int(a[index]) + carry
        if add == 0 or add == 1:
            result += str(add)
            carry = 0
        elif add == 2:
            result += str(0)
            carry = 1
        index += 1
    if carry:
        result += str(1)
    if index < len(a):
        result += a[index:]

    return result[::-1]


print(addBinary("111001", "1101011"))


# a = "mara"
# a = a[::-1]
# print(a)

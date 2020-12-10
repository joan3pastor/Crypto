def bytes_to_int(bytes):
    result = 0
    for b in bytes:
        result = result * 256 + int(b)
    return result

def int_to_bytes(value, length):
    result = []
    for i in range(0, length):
        result.append(value >> (i * 8) & 0xff)
    result.reverse()
    return bytes(result)

def print_block(block):
    for i in range(4):
        for j in range(4):
            print(hex(block[i+j*4]), end=" ")
        print()

def count_modified_bits(a, b):
    count = 0
    for i in range(128):
        bita = (bytes_to_int(a) >> i) % 2
        bitb = (bytes_to_int(b) >> i) % 2
        if (bita != bitb): count = count + 1
    return count

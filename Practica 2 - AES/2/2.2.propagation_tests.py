import aes as AES
from helpers import bytes_to_int, int_to_bytes, count_modified_bits

key = b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f'
message = b'\x00\x11\x22\x33\x44\x55\x66\x77\x88\x99\xAA\xBB\xCC\xDD\xEE\xFF'

def test_number_bits_changed_K():
    aes = AES.AES(key)
    ciphertext = aes.encrypt_block(message)
    modifiedbits = [0]*128
    for i in range(128):
        modifiedKey = int_to_bytes(bytes_to_int(key) ^ (1 << i), 16)
        aes = AES.AES(modifiedKey)
        ci = aes.encrypt_block(message)
        modifiedbits[count_modified_bits(ciphertext, ci)] += 1
    print(modifiedbits)

def test_number_bits_changed_M():
    aes = AES.AES(key)
    ciphertext = aes.encrypt_block(message)
    modifiedbits = [0]*128
    for i in range(128):
        modifiedMessage = int_to_bytes(bytes_to_int(message) ^ (1 << i), 16)
        ci = aes.encrypt_block(modifiedMessage)
        modifiedbits[count_modified_bits(ciphertext, ci)] += 1
    print(modifiedbits)

def test_position_of_bits_changed_K():
    aes = AES.AES(key)
    c = aes.encrypt_block(message)
    modifiedbits = [0]*128
    sum = 0
    for i in range(128):
        modifiedKey = int_to_bytes(bytes_to_int(key) ^ (1 << i), 16)
        aes = AES.AES(modifiedKey)
        ci = aes.encrypt_block(message)
        for j in range(128):
            bitc = (bytes_to_int(c) >> j) % 2
            bitci = (bytes_to_int(ci) >> j) % 2
            if (bitc != bitci): 
                modifiedbits[j] += 1
                sum += 1
    print(modifiedbits)
    print("mean = ", sum/128)

def test_position_of_bits_changed_M():
    aes = AES.AES(key)
    c = aes.encrypt_block(message)
    modifiedbits = [0]*128
    sum = 0
    for i in range(128):
        modifiedMessage = int_to_bytes(bytes_to_int(message) ^ (1 << i), 16)
        ci = aes.encrypt_block(modifiedMessage)
        for j in range(128):
            bitc = (bytes_to_int(c) >> j) % 2
            bitci = (bytes_to_int(ci) >> j) % 2
            if (bitc != bitci): 
                modifiedbits[j] += 1
                sum += 1
    print(modifiedbits)
    print("mean = ", sum/128)


if __name__ == "__main__":
    test_number_bits_changed_K()
    #test_number_bits_changed_M()
    #test_position_of_bits_changed_K()
    #test_position_of_bits_changed_M()
    print("End of tests")


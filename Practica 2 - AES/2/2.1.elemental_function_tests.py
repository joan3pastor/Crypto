import aes as AES
import aes_withoutByteSub as AESByteSub
import aes_withoutShiftRows as AESShiftRows
import aes_withoutMixColumns as AESMixColumns
from helpers import bytes_to_int, int_to_bytes, print_block

key = b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f'
message = b'\x00\x11\x22\x33\x44\x55\x66\x77\x88\x99\xAA\xBB\xCC\xDD\xEE\xFF'

def test_no_ByteSub():
    aes = AESByteSub.AES(key)
    ciphertext = aes.encrypt_block(message)
    compleixPropietat = True
    for i in range(128):
        for j in range(128):
            ci = aes.encrypt_block(int_to_bytes(bytes_to_int(message) ^ (1 << i), 16))
            cj = aes.encrypt_block(int_to_bytes(bytes_to_int(message) ^ (1 << j), 16))
            cij = aes.encrypt_block(int_to_bytes(bytes_to_int(message) ^ ((1 << i) ^ (1 << j)), 16))
            if (bytes_to_int(ciphertext) != bytes_to_int(ci) ^ bytes_to_int(cj) ^ bytes_to_int(cij)): compleixPropietat = False
    if (compleixPropietat): print("La propietat C = Ci XOR Cj XOR Cij per a tot i, j es compleix.") 
    else: print("La propietat  C = Ci XOR Cj XOR Cij per a tot i, j no es compleix.")

def test_no_ShiftRows():
    aes = AESShiftRows.AES(key)
    ciphertext = aes.encrypt_block(message)
    for i in range(4):
        ci = aes.encrypt_block(int_to_bytes(bytes_to_int(message) ^ (1 << i*32), 16))
        print("Original ciphertext:")
        print_block(ciphertext)
        print("1 bit modified:")
        print_block(ci)
        print()

def test_no_MixColumns():
    aes = AESMixColumns.AES(key)
    ciphertext = aes.encrypt_block(message)
    for i in range(4):
        ci = aes.encrypt_block(int_to_bytes(bytes_to_int(message) ^ (1 << i*32), 16))
        print("Original ciphertext:")
        print_block(ciphertext)
        print("1 bit modified:")
        print_block(ci)
        print()

if __name__ == "__main__":
    # test_no_ByteSub()
    # test_no_ShiftRows()
    # test_no_MixColumns()
    print("End of tests")


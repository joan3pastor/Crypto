import aes as AES
from helpers import bytes_to_int, int_to_bytes

key = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
cipher = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

aes = AES.AES(key)
message = aes.decrypt_block(cipher)
print(hex(bytes_to_int(message)))
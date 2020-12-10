from Crypto.Cipher import AES

key = open("2019_09_25_17_02_22_joan.marc.pastor.key", 'rb').read()
enc = open("2019_09_25_17_02_22_joan.marc.pastor.enc", 'rb').read()

iv = enc[:AES.block_size]
aes = AES.new(key, AES.MODE_CBC, iv)
message = aes.decrypt(enc[AES.block_size:])

open('2019_09_25_17_02_22_joan.marc.pastor.dec', 'wb').write(message)
open('2019_09_25_17_02_22_joan.marc.pastor.dec.jpg', 'wb').write(message)


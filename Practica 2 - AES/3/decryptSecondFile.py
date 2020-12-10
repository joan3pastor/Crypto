import multiprocessing
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from helpers import bytes_to_int, int_to_bytes

def decryptSet(preMasterKeys, coreNum):
    print("set", coreNum, "contains", len(preMasterKeys), "preMasterKeys")
    cipher = open("2019_09_25_17_02_22_joan.marc.pastor.puerta_trasera.enc", 'rb').read()
    for preKey in preMasterKeys:
        preKeyInBytes = int_to_bytes(preKey,16)
        hashkey = bytes_to_int(hashlib.sha256(preKeyInBytes).digest())
        KEY = int_to_bytes(hashkey >> 128, 16)
        IV = int_to_bytes(hashkey & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF, 16) # 32x F
        aes = AES.new(KEY, AES.MODE_CBC, IV)
        paddedMessage = aes.decrypt(cipher)
        try:
            message = unpad(paddedMessage, AES.block_size, style='pkcs7') #Rises error if wrong format
            print("possible preMasterKey: ", hex(preKey))
            open('out/' + hex(preKey).replace("0x", "") + '.mp4', 'wb').write(message)
        except:
            pass
    print("Core", coreNum, "finished")

if __name__ == '__main__':
    #preMasterKeys = [set()]*8 
    # One set for each process 
    pmkCore1 = set()
    pmkCore2 = set()
    pmkCore3 = set()
    pmkCore4 = set()
    pmkCore5 = set()
    pmkCore6 = set()
    pmkCore7 = set()
    pmkCore8 = set()
    # Generate preMasterKeys
    for xorC1 in range(0x80): # [0x00, 0x7F]
        core = xorC1 % 8
        for xorC2 in range(0x80): # [0x00, 0x7F]
            left = 0
            right = 0
            for i in range(8):
                left = (left << 8) + xorC1
                right = (right << 8) + xorC2
            key = (left << 64) + right
            #preMasterKeys[xorC1 % 8].add(key)
            if (core == 1): pmkCore1.add(key)
            if (core == 2): pmkCore2.add(key)
            if (core == 3): pmkCore3.add(key)
            if (core == 4): pmkCore4.add(key)
            if (core == 5): pmkCore5.add(key)
            if (core == 6): pmkCore6.add(key)
            if (core == 7): pmkCore7.add(key)
            if (core == 0): pmkCore8.add(key)
    processes = []
    processes.append(multiprocessing.Process(target=decryptSet, args=(pmkCore1, 1)))
    processes.append(multiprocessing.Process(target=decryptSet, args=(pmkCore2, 2)))
    processes.append(multiprocessing.Process(target=decryptSet, args=(pmkCore3, 3)))
    processes.append(multiprocessing.Process(target=decryptSet, args=(pmkCore4, 4)))
    processes.append(multiprocessing.Process(target=decryptSet, args=(pmkCore5, 5)))
    processes.append(multiprocessing.Process(target=decryptSet, args=(pmkCore6, 6)))
    processes.append(multiprocessing.Process(target=decryptSet, args=(pmkCore7, 7)))
    processes.append(multiprocessing.Process(target=decryptSet, args=(pmkCore8, 8)))
    # Start processes
    for p in processes:
        p.start()



    # TESTS

    # for key in pmkCore1:
    #     if (len(hex(key)) != 34):
    #         print(hex(key))

    # xorC1 = 0x01
    # xorC2 = 0X02
    # left = 0
    # right = 0
    # for i in range(8):
    #     left = (left << 8) + xorC1
    #     right = (right << 8) + xorC2
    # key = (left << 64) + right
    # print(hex(key))
    # print(len(int_to_bytes(key,16)))
    # print(hex(bytes_to_int(hashlib.sha256(int_to_bytes(key,16)).digest())))


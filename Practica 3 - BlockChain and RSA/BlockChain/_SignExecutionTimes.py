from rsa_key import rsa_key
import time

if __name__ == '__main__':
    times = []
    bits_modulos = [512, 1024, 2048, 4096]
    for bits_modulo in bits_modulos:
        RSAkey = rsa_key(bits_modulo=bits_modulo)
        base_message = 1111111111111111111111111111111111111

        current_message = base_message
        start = int(round(time.time() * 1000))
        for i in range(0,100):
            RSAkey.sign(current_message)
            current_message += base_message
        end = int(round(time.time() * 1000))
        time_sign = end-start

        current_message = base_message
        start = int(round(time.time() * 1000))
        for i in range(0,100):
            RSAkey.sign_slow(current_message)
            current_message += base_message
        end = int(round(time.time() * 1000))
        time_sign_slow = end-start

        print("bits_modulo: " + str(bits_modulo) + " -> x100 sign = " + str(time_sign) + " ms")
        print("bits_modulo: " + str(bits_modulo) + " -> x100 sign_slow = " + str(time_sign_slow) + " ms")

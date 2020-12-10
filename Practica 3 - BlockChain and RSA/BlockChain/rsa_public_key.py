# publicExponent -> L'exponent public de la clau rsa key
# modulus -> El modul de la clau rsa key

#from Crypto.Hash import SHA256
from rsa_key import rsa_key

class rsa_public_key:
    def __init__(self, rsa_key):
        self.publicExponent = rsa_key.publicExponent
        self.modulus = rsa_key.modulus

    def verify(self, message, signature):
        '''
        retorna el boolea True si "signature" es correspon amb una
        signatura de "message" feta amb la clau RSA associada a la clau
        publica RSA.
        En qualsevol altre cas retorma el boolea False
        '''
        unsigned = pow(signature, self.publicExponent, self.modulus)
        if (message == unsigned):
            return True
        return False


# ****** TESTS ******
if __name__ == '__main__':
    message = 12345
    rsak1 = rsa_key(bits_modulo=2048)
    rsak2 = rsa_key(bits_modulo=2048)
    signature = rsak1.sign(message)
    rsapk1 = rsa_public_key(rsak1)
    rsapk2 = rsa_public_key(rsak2)
    assert rsapk1.verify(message, signature), "Firmar un mensaje y verificarlo con la misma llave RSA resulta en discordancia de mensajes"
    assert not rsapk2.verify(message, signature), "Firmar un mensaje y verificarlo con una llave RSA distinta resulta en igualdad de mensajes"
    print("Tests superados")
    
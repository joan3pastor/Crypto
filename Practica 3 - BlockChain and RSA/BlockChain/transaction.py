# public_key -> Clau publica RSA corresponent a RSAkey
# RSAKey -> Clau RSA amb que es signa la transaccio
# message -> Document que es signa a la transaccio representat per un enter
# signature -> Signatura de message feta amb la clau RSAkey representada per un enter

from rsa_key import rsa_key
from rsa_public_key import rsa_public_key

class transaction:
    def __init__(self, message, RSAkey):
        '''
        genera una transaccio signant "message" amb la clau "RSAkey"
        '''
        self.public_key = rsa_public_key(RSAkey)
        self.message = message
        self.signature = RSAkey.sign(message)

    def verify(self):
        '''
        retorna el boolea True si "signature" es correspon amb una
        signatura de "message" feta amb la clau publica "public_key".
        En qualsevol altre cas retorma el boolea False
        '''
        return self.public_key.verify(self.message, self.signature)


# ****** TESTS ******
if __name__ == '__main__':
    RSAkey = rsa_key()
    message = 12345
    t = transaction(message, RSAkey)
    assert t.verify(), "'signature' no se corresponde con la firma de 'message' realizada con la llave publica 'public_key'"
    print("Test superado")
    
# block_hash -> SHA256 del bloc actual representat per un enter
# previous_block_hash -> SHA256 del bloc anterior representat per un enter
# transaction -> Es una transaccio valida
# seed -> Es un enter

from transaction import transaction
from rsa_key import rsa_key
from rsa_public_key import rsa_public_key
import hashlib
import random

class block:
    def __init__(self):
        '''
        crea un bloc (no necesariamnet valid)
        '''

    def genesis(self,transaction):
        '''
        genera el primer bloc d'una cadena amb la transaccio "transaction" que es caracteritza per:
        - previous_block_hash=0
        - ser valid
        '''
        self.previous_block_hash = 0
        self.transaction = transaction
        self.generate_valid_hash()

    def next_block(self, transaction):
        '''
        genera el seguent block valid amb la transaccio "transaction"
        '''
        newB = block()
        newB.previous_block_hash = self.block_hash
        newB.transaction = transaction
        newB.generate_valid_hash()
        return newB

    def verify_block(self):
        '''
        Verifica si un bloc es valid:
        *1-Comprova que el hash del bloc anterior cumpleix las condicions exigides
        *2-Comprova la transaccio del bloc es valida
        *3-Comprova que el hash del bloc cumpleix las condicions exigides
        Si totes les comprovacions son correctes retorna el boolea True.
        En qualsevol altre cas retorma el boolea False
        '''
        #*1
        if (self.previous_block_hash >= 2**(256-16)): 
            return False
        #*2
        if (self.transaction.verify() == False): 
            return False
        #*3
        if (self.block_hash >= 2**(256-16)): 
            return False
        #*4 Comprova que el hash estigui ben contruit
        entrada = str(self.previous_block_hash)
        entrada = entrada+str(self.transaction.public_key.publicExponent)
        entrada = entrada+str(self.transaction.public_key.modulus)
        entrada = entrada+str(self.transaction.message)
        entrada = entrada+str(self.transaction.signature)
        entrada = entrada+str(self.seed)
        blockHash = int(hashlib.sha256(entrada.encode()).hexdigest(),16)
        if (blockHash != self.block_hash): 
            return False
        return True
    
    def generate_valid_hash(self):
        valid = False
        while (not valid):
            self.seed = random.randrange(1, 2**32)
            entrada = str(self.previous_block_hash)
            entrada = entrada+str(self.transaction.public_key.publicExponent)
            entrada = entrada+str(self.transaction.public_key.modulus)
            entrada = entrada+str(self.transaction.message)
            entrada = entrada+str(self.transaction.signature)
            entrada = entrada+str(self.seed)
            self.block_hash = int(hashlib.sha256(entrada.encode()).hexdigest(),16)
            if (self.block_hash < 2**(256-16)): valid = True


# ****** TESTS ******
if __name__ == '__main__':
    RSAkey = rsa_key()
    message = 12345
    t = transaction(message, RSAkey)
    b1 = block()
    b1.genesis(t)
    assert b1.verify_block(), "Bloque b1(Genesis Block) no es valido"
    b2 = b1.next_block(t)
    assert b2.verify_block(), "Bloque b2(Siguiente bloque a b1) no es valido"
    print("Tests superados")


from block import block
from transaction import transaction
from rsa_key import rsa_key
from rsa_public_key import rsa_public_key

class block_chain:
    def __init__(self,transaction):
        '''
        genera una cadena de blocs que es una llista de blocs,
        el primer bloc es un bloc "genesis" generat amb la transaccio "transaction"
        '''
        self.list_of_blocks = []
        b = block()
        b.genesis(transaction)
        self.list_of_blocks.append(b)

    def add_block(self,transaction):
        '''
        afegeix a la llista de blocs un nou bloc valid generat amb la transaccio "transaction"
        '''
        b = self.list_of_blocks[-1].next_block(transaction)
        self.list_of_blocks.append(b)

    def verify(self):
        '''
        verifica si la cadena de blocs es valida:
        *1- Comprova que tots el blocs son valids
        *2- Comprova que el primer bloc es un bloc "genesis"
        *3- Comprova que per cada bloc de la cadena el seguent es el correcte
        Si totes les comprovacions son correctes retorna el boolea True.
        En qualsevol altre cas retorma el boolea False i fins a quin bloc la cadena es valida
        '''

        #*2
        if (self.list_of_blocks[0].previous_block_hash != 0): 
            return (False, 0)
        index = 0
        for block in self.list_of_blocks:
            # *1
            if (block.verify_block() == False): 
                return (False, index)

            #*3
            if (index != 0):
                b1 = self.list_of_blocks[index-1]
                b2 = self.list_of_blocks[index]
                if (b1.block_hash != b2.previous_block_hash): 
                    return (False, index)
                #La comprovacio de que el hash estigui ben contruit ja es realitza a la clase block
            index += 1
        return (True, len(self.list_of_blocks))


# ****** TESTS ******
if __name__ == '__main__':
    import pickle

    RSAkey = rsa_key()
    message1 = 12345
    message2 = 67890
    t1 = transaction(message1, RSAkey)
    t2 = transaction(message2, RSAkey)
    bc = None
    try:
        bc = block_chain(t1)
    except:
        assert False, "No a añadido el bloque Genesis correctamente"
    try:
        bc.add_block(t2)
    except:
        assert False, "No a añadido el bloque correctamente a un Blockchain no vacio"

    with open('./bin/Cadena_bloques_valida.block', 'rb') as file:
        bc = pickle.load(file)
        x, y = bc.verify()
        assert x, "Cadena_bloques_valida.block no es valido"

    with open('./bin/Cadena_bloques_transaccion_falsa.block', 'rb') as file:
        bc = pickle.load(file)
        x, y = bc.verify()
        assert (not x) and y == 19, "Cadena_bloques_valida.block no deja de ser valido en el bloque #20 (debido a transaccion falsa)"

    with open('./bin/Cadena_bloques_seed_falsa.block', 'rb') as file:
        bc = pickle.load(file)
        x, y = bc.verify()
        assert (not x) and y == 23, "Cadena_bloques_valida.block no deja de ser valido en el bloque #24 (debido a seed falsa)"

    with open('./bin/Cadena_bloques_bloque_falso.block', 'rb') as file:
        bc = pickle.load(file)
        x, y = bc.verify()
        assert (not x) and y == 17, "Cadena_bloques_valida.block no deja de ser valido en el bloque #18 (debido a seed falsa)"

    print("Tests superados")

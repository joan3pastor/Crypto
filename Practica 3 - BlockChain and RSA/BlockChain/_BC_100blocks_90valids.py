from block_chain import block_chain
from block import block
from transaction import transaction
from rsa_key import rsa_key
from rsa_public_key import rsa_public_key
import pickle
import random

# DNI == 49765290

def creation():
    bc = None
    RSAkey = rsa_key()
    for i in range(0, 100):
        message = random.randrange(1, 2**10)
        t = transaction(message, RSAkey)
        if (i == 90): t.message = t.message+1
        if (i == 0): bc = block_chain(t)
        else: bc.add_block(t)
        print(i+1)

    valid, index = bc.verify()
    print("valid:", valid)
    print("index:", index)
    assert not valid and index == 90, "Blockchain no deja de ser valido en el bloque #91"
    assert len(bc.list_of_blocks) == 100, "Blockchain no contiene 100 bloques"
    with open("./out/BC_100blocks_90valids.block", 'wb') as file:
        pickle.dump(bc, file)
    print("BlockChain serializado en /out/BC_100blocks_90valids.block")

def file_verification():
    with open('./out/BC_100blocks_90valids.block', 'rb') as file:
        bc = pickle.load(file)
        x, y = bc.verify()
        print(x, y)
        assert not x and y == 90, "BC_100blocks_90valids.block no deja de ser valido en el bloque #91"
        assert len(bc.list_of_blocks) == 100, "BC_100blocks_90valids.block no contiene 100 bloques"
        print("Tests superados")
        
if __name__ == '__main__':
    creation()
    file_verification()

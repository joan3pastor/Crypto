from Crypto.PublicKey import RSA
from sympy.ntheory.factor_ import totient, factorint
from decimal import Decimal

def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
        gcd = b
    return gcd, x, y

if __name__ == '__main__':
    f = open("./bin/joan.marc.pastor_pubkeyRSA_pseudo.pem")
    key = RSA.import_key(f.read())
    f.close()

    n = key.n
    e = key.e

    # totient() implementation: https://docs.sympy.org/latest/_modules/sympy/ntheory/factor_.html#totient
    phiN = totient(n)
    gcd, a, b = egcd(e, phiN)
    if (a >= 0): 
        d = a
    else:
        d = a + phiN

    key = RSA.construct((n, e, d), consistency_check=False)
    f = open("./out/RSAprivateKey.pem", "wb")
    f.write(key.export_key("PEM"))
    f.close()

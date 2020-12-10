from Crypto.PublicKey import RSA
from math import gcd
import os

def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
        gcd = b
    return gcd, x, y

if __name__ == '__main__':
    f = open("./bin/joan.marc.pastor_pubkeyRSA_RW.pem")
    key = RSA.import_key(f.read())
    f.close()

    n = key.n
    e = key.e 
    print("N =", n)

    path = './bin/'
    files = []
    with os.scandir(path) as entries:
        for entry in entries:
            if (".pem" in entry.name and not "joan.marc.pastor" in entry.name):
                files.append(path + entry.name)

    first = True
    for file in files:
        f = open(file)
        key = RSA.import_key(f.read())
        f.close()
        if gcd(n, key.n) != 1:
            if (first): 
                p1 = gcd(n, key.n)
                print("P1 =", p1)
                first = False
            else:
                p2 = gcd(n, key.n)
                print("P2 =", p2)

    assert type(p1) == int and type(p2) == int, "No se encontron 2 primos comunes"
    assert p1*p2 == n, "Los primos p1 y p2 no forman el modulo"

    phiN = (p1 - 1) * (p2 - 1)
    gcd, a, b = egcd(e, phiN)
    d = a

    key = RSA.construct((n,e,d))
    f = open("./out/RSAprivateKey.pem", "wb")
    f.write(key.export_key("PEM"))
    f.close()

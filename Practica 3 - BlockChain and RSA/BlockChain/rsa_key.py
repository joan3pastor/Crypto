# publicExponent, privateExponent, modulus, primeP, primeQ estan representats per enters
# privateExponentModulusPhiP -> Es congruent amb privateExponent modul primeP-1 representat per un enter
# privateExponentModulusPhiQ -> Es congruent amb privateExponent modul primeQ-1 representat per un enter
# inverseQModulusP -> L'invers de primeQ modul primeP representat per un enter

import random
from Crypto.Util import number
#from Crypto.Hash import SHA256

import sys
sys.setrecursionlimit(10000)

class rsa_key:
    def __init__(self, bits_modulo=2048, e=2**16+1): # TODO
        '''
        genera una clau RSA (de 2048 bits i amb exponent public 2**16+1 per defecte)
        '''
        self.primeP = number.getPrime(bits_modulo)
        self.primeQ = number.getPrime(bits_modulo)
        while(self.primeP == self.primeQ):
            self.primeQ = number.getPrime(bits_modulo)

        self.modulus = self.primeP * self.primeQ
        #print("modulus = ", self.modulus)

        phiN = ((self.primeP - 1) * (self.primeQ - 1))
        if (e != None and self.__gcd(e, phiN) == 1):
            self.publicExponent = e
        else:
            print("el argumento 'e' no es elegible como exponente publico. Se generará uno nuevo...")
            self.publicExponent = self.__findE(phiN)
        #print("publicExponent(e) = ", self.publicExponent)

        gcd, x, y = self.__egcd(self.publicExponent, phiN)
        if (x >= 0): 
            self.privateExponent = x
        else: 
            self.privateExponent = x + phiN
        #print("privateExponent(d) = ", self.privateExponent)

        self.privateExponentModulusPhiP = self.privateExponent % (self.primeP-1)
        self.privateExponentModulusPhiQ = self.privateExponent % (self.primeQ-1)

        gcd, x, y = self.__egcd(self.primeQ, self.primeP)
        if (x >= 0): 
            self.inverseQModulusP = x
        else: 
            self.inverseQModulusP = x + self.primeP

        gcd, x, y = self.__egcd(self.primeP, self.primeQ)
        if (x >= 0): 
            self.inversePModulusQ = x
        else: 
            self.inversePModulusQ = x + self.primeQ

    def sign(self,message): # TODO
        '''
        retorma un enter que es la signatura de "message" feta amb la clau RSA fent servir el TXR
        '''
        d1 = self.privateExponentModulusPhiP
        d2 = self.privateExponentModulusPhiQ
        p1 = self.inversePModulusQ
        q1 = self.inverseQModulusP
        c1 = pow(message, d1, self.primeP)
        c2 = pow(message, d2, self.primeQ)
        signature = (c1*q1*self.primeQ + c2*p1*self.primeP) % self.modulus
        return signature

    def sign_slow(self,message):
        '''
        retorma un enter que es la signatura de "message" feta amb la clau RSA sense fer servir el TXR
        '''
        signature = pow(message, self.privateExponent, self.modulus)
        return signature
    
    def __findE(self, phiN):
        while (True):
            e = random.randrange(2, phiN)
            if (self.__gcd(e, phiN) == 1):
                return e

    def __gcd(self, a, b):
        if (b == 0):
            return a
        else:
            return self.__gcd(b, a % b)

    def __egcd(self, a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            gcd, x, y = self.__egcd(b % a, a)
            return (gcd, y - (b // a) * x, x)


# ****** TESTS ******
if __name__ == '__main__':
    rsak = rsa_key(bits_modulo=2048)
    slow = rsak.sign(12345)
    fast = rsak.sign_slow(12345)
    assert slow == fast, "Firmar un mismo mensaje con sign() y sign_slow() resulta en firmas distintas"
    print("Test superado")

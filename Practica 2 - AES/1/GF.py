m = 0b100011101

def mult_x(a):
    res = a << 1
    if (res >> 8 == 0b1):
        res = res ^ m
    return res

def mult_x_n_times(a, n):
    if (n == 0):
        return 0
    res = a
    for i in range (1, n):
        res = mult_x(res)
    return res
    # 1 -> a
    # 2 -> mult_x(a)
    # 3 -> mult_x(mult_x(a))
    # 4 -> mult_x(mult_x(mult_x(a)))

def GF_product_p(a, b):
    #in: a i b elements del cos representat per enters entre 0 i 255.
    #out: un element del cos representat per un enter entre 0 i 255 que 
    # es el producte en el cos de a i b fent servir la definicio en termes de polinomis.
    prod = 0
    for i in range(8): # 0..7
        if ((b >> i) % 2):
            prod = prod ^ mult_x_n_times(a, i+1)
    return prod

def GF_es_generador(a):
    #in: a element del cos representat per un enter entre 0 i 255;
    #out: True si a es generador del cos, False si no ho es.
    r = mult_x_n_times(a, 255)
    if (r == 1):
        return True
    else:
        return False

def GF_tables():
    #out: dues taules (exponencial i logaritme), una que a la posicio i tingui a = gi 
    # i una altra que a la posicio a tingui i tal que a = gi. (g generador del cos 
    # finit del cos representat pel menor enter entre 0 i 255.)
    taulaExp = [None]*256
    taulaLog = [None]*256
    taulaExp[0] = 1
    taulaExp[1] = 2
    taulaLog[1] = 2
    taulaLog[2] = 1
    prodP = 2
    for i in range(2, 256):
        prodP = GF_product_p(prodP, 2)
        taulaExp[i] = prodP
        taulaLog[prodP] = i
    return taulaExp, taulaLog

def GF_product_t(a, b, taulaExp, taulaLog):
    #in: a i b elements del cos representat per enters entre 0 i 255;
    #out: un element del cos representat per un enter entre 0 i 255 que es el 
    # producte en el cos de a i b fent servir la les taules exponencial i logaritme.
    i = (taulaLog[a] + taulaLog[b]) % 255
    return taulaExp[i]

def GF_invers(a, taulaExp, taulaLog):
    #in: a element del cos representat per un enter entre 0 i 255;
    #out: 0 si a=0x00, invers d'a en el cos si a!=0x00 representat per un enter entre 1 i 255.
    i = (255 - taulaLog[a]) % 255
    return taulaExp[i]


if __name__ == "__main__":
    # print(GF_es_generador(2))
    [exp, log] = GF_tables()
    print(exp)
    print("")
    print(log)
    # print(GF_invers(4, exp, log))
    # print(GF_product_t(20, 40, exp, log))

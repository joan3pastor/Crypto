import GF as GF
import time

blist = [0x02, 0x03, 0x09, 0x0B, 0x0D, 0x0E]

print("** TESTING: GF_product_p **\n")
for b in blist:
    sum = 0
    start = time.time()
    for a in range(1, 256):
        f = GF.GF_product_p(a, b)
        sum = sum + f
    end = time.time()
    elapsed = end*1000-start*1000 #milliseconds
    print("b = ", b)
    print("sum = ", sum)
    print(elapsed, "milliseconds")

print("\n** TESTING: GF_product_t with generation of tables**\n")
for b in blist:
    sum = 0
    start = time.time()
    [exp, log] = GF.GF_tables()
    for a in range(1, 256):
        f = GF.GF_product_t(a, b, exp, log)
        sum = sum + f
    end = time.time()
    elapsed = end*1000-start*1000 #milliseconds
    print("b = ", b)
    print("sum = ", sum)
    print(elapsed, "milliseconds")

print("\n** TESTING: GF_product_t with tables previously generated**\n")
[exp, log] = GF.GF_tables()
for b in blist:
    sum = 0
    start = time.time()
    for a in range(1, 256):
        f = GF.GF_product_t(a, b, exp, log)
        sum = sum + f
    end = time.time()
    elapsed = end*1000-start*1000 #milliseconds
    print("b = ", b)
    print("sum = ", sum)
    print(elapsed, "milliseconds")



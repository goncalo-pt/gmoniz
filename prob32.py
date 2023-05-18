from math import factorial as fl
from time import perf_counter

t0 = perf_counter()

def is_pandigital(a,b,c):
    n = str(a)+str(b)+str(c)
    if len(n) != 9 or "0" in n:
        return False
    for i in range(0, 8):
        d = n[i]
        for j in range(i+1, 9):
            if n[j] == d:
                return False
    return True

products_list = [int]*int(fl(9)/fl(5))
a = 1
# len(a)+len(b)+len(c) = 9

for i in range(0, int(fl(9)/fl(5))):
    prod = [int]*4
    digits = [1,2,3,4,5,6,7,8,9]

    d0 = fl(8)/fl(5)    
    index0 = int(i/d0)
    prod[0] = digits.pop(index0)
    k1 = index0 * d0

    d1 = d0 / 8
    index1 = int((i-k1)/d1)
    prod[1] = digits.pop(index1)
    k2 = k1 + index1 * (d1)
    
    d2 = d1 / 7
    index2 = int((i-k2)/d2)
    prod[2] = digits.pop(index2)
    k3 = k2 + index2 * d2

    d3 = d2 / 6
    index3 = int((i-k3)/d3)
    prod[3] = digits[index3]
    
    product = int(str(prod[0])+str(prod[1])+str(prod[2])+str(prod[3]))
    products_list[i] = product

def decompose_and_check(d):
    for i in range(2, int(d**0.5)):
        if d%i == 0 and is_pandigital(d, int(d/i), i):
            return True, int(d)
    return False, False

list_ = []
sum = 0
for n in range(0, len(products_list)):
    if decompose_and_check(products_list[n])[0] and n not in list_:
        sum += decompose_and_check(products_list[n])[1]
print(sum)
print("Time: "+str(perf_counter()-t0) )

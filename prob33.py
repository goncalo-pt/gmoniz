from numpy import isclose
from time import perf_counter
t = perf_counter()
def check(n, d):
    result = n/d
    n_ = float(str(n)[0])
    d_ = float(str(d)[1])
    if isclose(d_, 0) or str(n)[0]==str(n)[1] or str(d)[0]==str(d)[1] or str(n)[1]!=str(d)[0]: return False
    if isclose(result, n_/d_):
        return True
    return False

list_ = []

for n in range(10, 99):
    for d in range(n+1, 100):
        if check(n, d):
            list_.append([n,d])

a = list_[0][0]*list_[1][0]*list_[2][0]*list_[3][0]
b = list_[0][1]*list_[1][1]*list_[2][1]*list_[3][1]

product = [a, b]

def find_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5+1)):
        if n%i == 0:
            divisors.append(int(i))
            divisors.append(int(n/i))
    return divisors 

def find_common_divisor(a, b):
    A = set(find_divisors(a))
    B = set(find_divisors(b))
    common = A & B
    if common is None:
        return None
    return max(common)

print(b/find_common_divisor(a, b))
print("time: "+str(perf_counter()-t))
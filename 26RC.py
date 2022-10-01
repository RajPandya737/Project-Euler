from decimal import *

def len_rep(n):
    n = list(map(int, list(str(n*10**100))))
    i = 1
    while True:
        
        pass

getcontext().prec = 1000
longest = 5
for i in range(2,10):
    dec = Decimal(1)/Decimal(i)
    if len(str(dec)) < longest or len(set(list(str(dec))))<3:
        pass
    else:
        l = len_rep(dec)
        if l>longest:
            longest = l

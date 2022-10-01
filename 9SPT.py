a,b,c,asq,bsq,csq = 0,0,0,0,0,0

for al in range(1, 332):
    for bl in range(2, 499):
        c = 1000 - al - bl
        asq = al * al
        bsq = bl * bl
        csq = c * c

        if asq + bsq == csq:
            print(al*bl*c)
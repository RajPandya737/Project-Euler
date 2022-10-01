t = 11

for i in range(1,5):
    ones = 0
    tens = 0
    hundreds = 0
    l = list(str(i))
    if i<10:
        ones = int(l[0])
    elif i <100:
        ones = int(l[1])
        tens = int(l[0])
    else:
        ones = int(l[2])
        tens = int(l[1])
        hundreds = int(l[0])
    
    if i%100 != 0:
        t+=3
    if tens == 1 and ones == 1:
        t+=6
    if tens == 1 and ones == 2:
        t+=6
    if tens == 1 and ones == 3:
        t+=8
    if tens == 1 and ones == 4:
        t+=8
    if tens == 1 and ones == 5:
        t+=7
    
    print(hundreds , tens, ones, t)



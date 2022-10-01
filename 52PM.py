#ready to submit
i = 2
while True:

    hash = {}
    pt = list(str(i))
    p = list(map(int, pt))
    for j in p:
        hash[j] = 0
    for j in p:
        hash[j] += 1

    hash2 = {}
    pt2 = list(str(i*2))
    p2 = list(map(int, pt2))
    for j in p2:
        hash2[j] = 0
    for j in p2:
        hash2[j] += 1

    hash3 = {}
    pt3 = list(str(i*3))
    p3 = list(map(int, pt3))
    for j in p3:
        hash3[j] = 0
    for j in p3:
        hash3[j] += 1
    
    hash4 = {}
    pt4 = list(str(i*4))
    p4 = list(map(int, pt4))
    for j in p4:
        hash4[j] = 0
    for j in p4:
        hash4[j] += 1

    hash5 = {}
    pt5 = list(str(i*5))
    p5 = list(map(int, pt5))
    for j in p5:
        hash5[j] = 0
    for j in p5:
        hash5[j] += 1

    hash6 = {}
    pt6 = list(str(i*6))
    p6 = list(map(int, pt6))
    for j in p6:
        hash6[j] = 0
    for j in p6:
        hash6[j] += 1
    if hash == hash2 == hash3 == hash4 == hash5 == hash6:
        print(i)
        break
    i+=1
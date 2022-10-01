d1 = 1
d2 = 1
d3 = 2

seq = [1,1,2]


while len(list(str(seq[-1]))) <1000:
    d1 = d2
    d2 = d3
    d3 = d1+d2
    seq.append(d3)
print(len(seq)-1)

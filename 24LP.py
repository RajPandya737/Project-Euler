from itertools import permutations
perms = [''.join(p) for p in permutations('0123456789')]

p = list(map(int, perms))
f = sorted(p)
print(f[999999])
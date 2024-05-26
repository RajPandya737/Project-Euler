from collections import defaultdict
def primes_sieve(limit):
    limitn = limit+1
    primes = list(range(2, limitn))

    for i in primes:
        factors = range(i, limitn, i)
        for f in factors[1:]:
            if f in primes:
                primes.remove(f)
    
    return primes

old = primes_sieve(10000)
primes = []
for p in old:
    if p > 1000:
        primes.append(p)
hash = defaultdict(list)
for i, v in enumerate(primes):
    hash[''.join(sorted(str(v)))].append(v)

old_keys = hash.keys()
keys = []
for key in old_keys:
    if len(hash[key]) >= 3:
        keys.append(key)


for key in keys:
    nums = hash[key]
    differences = set()
    for i, v in enumerate(nums):
        for j in range(i, len(nums)):

            diff = nums[j] - v
            if diff != 0 and nums[j] + diff in nums:
                print(nums[j] - diff, nums[j], nums[j] + diff)

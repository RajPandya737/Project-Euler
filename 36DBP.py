def is_p(n):
  if n == int("".join((list(str(n)))[::-1])):
    return True
  return False
    
sum = 0
for i in range(1,1000000):
  print(i)
  if is_p(i) and is_p(int(bin(i)[2:])):
    sum+=i
print(sum)
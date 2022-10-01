max = 0
num = 0
for i in range(2, 1000000):
  c = [i]
  l = 1
  n = i+1-1
  while n != 1:
    if n %2 == 0:
      n = n/2
    else:
      n = 3*n+1
    c.append(n)
    l+=1
  if l>max:
    max = l
    num = c[0]
print(num)
print(max)
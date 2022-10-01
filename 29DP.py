n = []
for i in range(2, 101):
  for j in range(2,101):
    n.append(i**j)
print(len(set(n)))
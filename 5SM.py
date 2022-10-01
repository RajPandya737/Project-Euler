nums = [11,12,13,14,15,16,17,18,19,20]

n = 20
f = 0
while True:
  for i in range(11):
    if i == 10:
      f = n
    elif n%nums[i]!=0:
      break
  n+=20
  if f !=0:
    break
print(f)
    
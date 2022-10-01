from collections import defaultdict
nums = []

with open ("67MPS.txt") as file:
  count= 0
  while True:
    count+=1
    line = file.readline()
    if not line:
      break
    nums.append(list(map(int, line.split())))

for row in range(len(nums)-2, -1, -1):
  for col in range(0, row+1):
    if nums[row+1][col]>nums[row+1][col+1]:
      nums[row][col] +=nums[row+1][col]
    else:
      nums[row][col]+=nums[row+1][col+1]

print(nums[0][0])




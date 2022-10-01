from collections import defaultdict
nums = [[75], [95, 64], [17, 47, 82], [18, 35, 87, 10], [20, 4, 82, 47, 65], [19, 1, 23, 75, 3, 34], [88, 2, 77, 73, 7, 63, 67], [99, 65, 4, 28, 6, 16, 70, 92], [41, 41, 26, 56, 83, 40, 80, 70, 33], [41, 48, 72, 33, 47, 32, 37, 16, 94, 29], [
    53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14], [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57], [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48], [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31], [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]

"""with open ("18MPS.txt") as file:
  count= 0
  while True:
    count+=1
    line = file.readline()
    if not line:
      break
    new_nums.append(list(map(int, line.split())))"""
"""
graph = defaultdict(list)
# v are vertices
# e are edges
v, e = 120, 210

for row in range(len(new_nums)-1):
    for col in range(row+1):
        graph[str(new_nums[row][col]) + " " + 
              str(row)].append(str(new_nums[row+1][col]) + " " + str(row+1))
        graph[str(new_nums[row][col]) + " " +
              str(row)].append(str(new_nums[row+1][col+1]) + " " + str(row + 1))

"""

for row in range(len(nums)-2, -1, -1):
  for col in range(0, row+1):
    if nums[row+1][col]>nums[row+1][col+1]:
      nums[row][col] +=nums[row+1][col]
    else:
      nums[row][col]+=nums[row+1][col+1]
print(nums[0][0])




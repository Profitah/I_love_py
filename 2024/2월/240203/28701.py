x = int(input())

total_sum = 0  
cube_sum = 0  

for i in range(1, x+1):
  total_sum += i
  cube_sum += i ** 3

print(total_sum)
print(total_sum ** 2)  
print(cube_sum)

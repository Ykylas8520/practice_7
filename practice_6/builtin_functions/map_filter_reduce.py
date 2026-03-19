from functools import reduce

nums = [1,2,3,4]

# 1 map
print(list(map(lambda x: x*2, nums)))

# 2 map square
print(list(map(lambda x: x*x, nums)))

# 3 filter even
print(list(filter(lambda x: x%2==0, nums)))

# 4 filter >2
print(list(filter(lambda x: x>2, nums)))

# 5 reduce sum
print(reduce(lambda x,y: x+y, nums))
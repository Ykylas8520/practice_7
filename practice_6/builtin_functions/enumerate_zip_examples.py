# 1 enumerate
a = ["a","b","c"]
for i, v in enumerate(a):
    print(i, v)

# 2 enumerate start=1
for i, v in enumerate(a, start=1):
    print(i, v)

# 3 zip
x = [1,2,3]
y = ["a","b","c"]
for i,j in zip(x,y):
    print(i,j)

# 4 zip list
print(list(zip(x,y)))

# 5 zip 3 lists
z = [True, False, True]
print(list(zip(x,y,z)))
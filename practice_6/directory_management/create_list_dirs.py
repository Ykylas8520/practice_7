import os

# 1 create folder
os.mkdir("folder1")

# 2 nested
os.makedirs("a/b/c")

# 3 list files
print(os.listdir())

# 4 current dir
print(os.getcwd())

# 5 change dir
os.chdir("folder1")
print(os.getcwd())
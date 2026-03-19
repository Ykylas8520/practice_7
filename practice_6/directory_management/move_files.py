import shutil

# 1 move file
shutil.move("test.txt", "folder1/test.txt")

# 2 move back
shutil.move("folder1/test.txt", "test.txt")

# 3 copy file
shutil.copy("test.txt", "folder1/copy.txt")

# 4 rename (move)
shutil.move("test.txt", "newname.txt")

# 5 move again
shutil.move("newname.txt", "folder1/newname.txt")
import shutil
import os

# 1 copy
shutil.copy("test.txt", "copy1.txt")

# 2 copy2
shutil.copy("test.txt", "copy2.txt")

# 3 delete
os.remove("copy1.txt")

# 4 safe delete
if os.path.exists("copy2.txt"):
    os.remove("copy2.txt")

# 5 copy again
shutil.copy("test.txt", "backup.txt")
#1
with open("demofile.txt", "a") as f:
  f.write("Now the file has more content!")

#open and read the file after the appending:
with open("demofile.txt") as f:
  print(f.read())
#2
with open("demofile.txt", "w") as f:
  f.write("Woops! I have deleted the content!")

#open and read the file after the overwriting:
with open("demofile.txt") as f:
  print(f.read())
# 3
f = open("test.txt", "a")
f.write("Append line\n")
f.close()

# 4
with open("test.txt", "w") as f:
    f.write("Using with\n")

# 5
with open("test.txt", "a") as f:
    f.write("Another line\n")
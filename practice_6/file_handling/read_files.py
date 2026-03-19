#1
f = open("demofile.txt")
print(f.read())
#2
with open("demofile.txt") as f:
  print(f.read())
#3
f = open("demofile.txt")
print(f.readline())
f.close()
#4
with open("demofile.txt") as f:
  print(f.read(5))
#5
with open("demofile.txt") as f:
  print(f.readline())
#6
with open("demofile.txt") as f:
  print(f.readline())
  print(f.readline())
#7
with open("demofile.txt") as f:
  for x in f:
    print(x)
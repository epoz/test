import random, time, os

# AB
print(time.ctime(), "woot")
open("docs/zarg.html", "w").write(f"{random.random()}")

for dirpath, dirnames, filenames in os.walk("."):
    for filename in filenames:
        print(dirpath, filename)

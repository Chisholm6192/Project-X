f = open("sprout.txt", "r")
lines = f.readlines()
p = []
d = []

for i in range(0,len(lines)):
    name, amount = lines[i].split(" ")
    replace = amount.replace("\n", "")
    p.append(name)
    d.append(replace)
print(p, d)

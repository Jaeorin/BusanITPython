f = open("190128_fileo.txt")
line = f.readline()

while line:
    print(line)
    line = f.readline()

f.close()

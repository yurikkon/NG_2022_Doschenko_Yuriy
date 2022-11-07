size = int(input("write number"))
for size in range(1, size+1):
    for column in range(size, 0, - 1 ):
        print(column, end=' ')
    print("")
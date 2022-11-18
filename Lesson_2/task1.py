stringlvl1 = list(input("write string: "))
stringlvl2 = sorted(set(stringlvl1))
for index in stringlvl2:
    count = stringlvl1.count(index)
    print(count)


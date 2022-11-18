spisok1 = input("Write your spisok: ").split(",")
changedSpisok = []
for elements in spisok1:
    changedSpisok.append(int(elements))
max_chislo = int(max(changedSpisok))
min_chislo = int(min(changedSpisok))
changedSpisok.sort()
summa = sum(changedSpisok[1:-1])
print("summa last" + str(summa))
print("max " + str(max_chislo) + " min " + str(min_chislo))
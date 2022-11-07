spisok = input("Write your spisok: ").split(",")
changedSpisok = []
for elements in spisok:
    changedSpisok.append(int(elements))
max_chislo = max(changedSpisok)
min_chislo = min(changedSpisok)
summa = sum(changedSpisok) - max_chislo - min_chislo
print("summa last" + str(summa))
print("max " + str(max_chislo) + " min " + str(min_chislo))

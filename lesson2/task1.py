string = list(input("write string: "))
list.sort(string)
for elements in range(len(string)):
    count = 0
    if string[elements] != string[elements - 1]:
        for letters in range(len(string)):
            if string[elements] == string[letters]:
                count = count + 1
            if letters + 1 == len(string):

                print(count)

        #abac






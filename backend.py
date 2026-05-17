zoznam = [1,20,4,50,49,1,3,5,63]
zoznam_sorted = []

for b in range(len(zoznam)):

    for i in range(len(zoznam)-1):

        if zoznam[i] > zoznam[i+1]:
            temp = zoznam[i]

            zoznam[i] = zoznam[i+1]
            zoznam[i+1] = temp

print(zoznam)

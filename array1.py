myarr = [2,7,5]

for i in range(0,len(myarr)):
    for j in range(i,len(myarr)):
        for k in range(i,j+1):
            print(myarr[k],end = " ")
        print()

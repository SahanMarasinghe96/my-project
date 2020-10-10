
residentArr = [10,3,2,5,7,1]

copyResidentArr = residentArr.copy()

length = len(residentArr)

total = 0

for n in copyResidentArr:
    total += n
    x = residentArr.index(n)
    p = x-1
    q = x+1
    if p >= 0:
        if residentArr[p] in copyResidentArr:     
            copyResidentArr.remove(residentArr[p])
    if q <= (length - 1):
        if residentArr[q] in copyResidentArr:
            copyResidentArr.remove(residentArr[q])


print(total)

        
    
        



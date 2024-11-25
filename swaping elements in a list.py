l=[11,22,33,44,55,66]
for i in range(0,len(l),2):
    l[i],l[i+1]=l[i+1],l[i]
    
print(l)

'''
 iteration 1: it will extract 0 and replaces 11 with 22 and 22 with 11
 iteration 2: it will extract 2 and replaces 33 with 44 and 44 with 33
 iteration 3: it will extract 4 and replaces 55 with 66 and 66 with 55

'''

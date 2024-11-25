l=eval(input())
i=0
while i<len(l):
    l[i],l[i+1]=l[i+1],l[i]
    i+=2
print(l)

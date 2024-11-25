a=input()
i=0
while i<len(a):
    if a[i].isdigit():
        if i%2!=0 and int(a[i])%2!=0:
            print(a[i])
    i+=1

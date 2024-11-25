cdt=eval(input())
d={}.fromkeys(cdt,0)
for i in cdt:
    d[i]=d[i]+1
for k,v in d.items():
    print(k,v)


# another method

cdt=eval(input())
d={}
for i in cdt:
    d[i]=cdt.count(i)
print(d)


#another method
cdt=eval(input())
d={}
for i in cdt:
    if i not in d:
        d[i]=1
    else:
        d[i]=d[i]+1
print(d)
     

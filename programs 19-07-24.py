# prime numbers in a given range


a=int(input())
b=int(input())
for num in range(a,b+1):    if num>1:
        for i in range(2,num//2+1):
            if num%i==0:
                break
        else:
            print(num)


# armstrong numbers in a goven range


a=int(input())
b=int(input())
for num in range(a,b+1):
    l=len(str(num))
    dum=num
    s=0
    while dum>0:
        r=dum%10
        s+=r**l
        dum//=10

    if s==num:
        print(num)
     
        
# Diaarium numbers in a given range


a=int(input())
b=int(input())
for num in range(a,b+1):
    l=len(str(num))
    dum=num
    s=0
    while dum>0:
        r=dum%10
        s+=r**l
        l-=1
        dum//=10
    if s==num:
        print(num)

# harshad numbers in a given range


a=int(input())
b=int(input())
for num in range(a,b+1):
    dum=num
    s=0
    while dum>0:
        r=dum%10
        s+=r
        dum//=10
    if num%s==0:
        print(num)
        

# first 10 prime numbers


i=1
c=0
while i>0 and c<10:
    if i>1:
        for j in range(2,i//2+1):
            if i%j==0:
                break
        else:
            print(i)
            c+=1
    i+=1


# first 10 armstrong numbers


i=1
c=0
while i>0 and c<10:
        
        d=i
        l=len(str(i))
        s=0
        while d>0:
            r=d%10
            s+=r**l
            d//=10
        if s==i:
            print(i)
            c+=1
        i+=1


# first 10 disarium numbers numbers


i=1
c=0
while i>0 and c<10:
        d=i
        l=len(str(i))
        s=0
        while d>0:
            r=d%10
            s+=r**l
            l-=1
            d//=10
        if s==i:
            print(i)
            c+=1
        i+=1

    
# first 10 harshad numbers

i=1
c=0
while i>0 and c<10:
    d=i
    s=0
    while d>0:
        r=d%10
        s+=r
        d//=10
    if i%s==0:
        print(i)
        c+=1
    i+=1
        
    




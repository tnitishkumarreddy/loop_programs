l=list(map(int,input().split()))
c=0
m=0
s=''
for i in l:
    if i==1:
        c+=1
    a=chr(64+c)
    s+=a
    c=0
for i in l:
    if i==0:
        s+=' '
print(s)



'''

input 1: 1 1 0 1 1 1 1 0 1 1

output 1: 4

explanation:  maximum consecutive times of 1 repeated is 4 so output is 4.


input 2: 1 1 0 1

output 2: 2

explanation:  maximum consecutive times of 1 repeated is 2 so output is 2.

'''

s=eval(input())
i=0
while i<len(s):
    if s[i]%2==0:
        s[i]='even'
    else:
        s[i]='odd'
    i+=1
print(s)

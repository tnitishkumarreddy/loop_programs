s=input()
i=0
v='aeiouAEIOU'
n=''
while i<len(s):
    if s[i] in v:
        n+=str(i)
    else:
        n+=s[i]
    i+=1
print(n)

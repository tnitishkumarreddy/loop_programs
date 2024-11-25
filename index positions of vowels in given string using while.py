s=input()
i=0
v='aeiouAEIOU'
while i<len(s):
    if s[i] in v:
        print(i)
    i+=1

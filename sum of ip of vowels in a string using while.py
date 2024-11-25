s=input()
su,i=0,0
v='aeiouAEIOU'
while i<len(s):
    if s[i] in v:
        su+=i
    i+=1

print(su)

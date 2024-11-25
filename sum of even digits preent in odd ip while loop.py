s=input()
su=0
i=0
while i<len(s):
    if s[i].isdigit():
        if int(s[i])%2==0 and i%2!=0:
            su+=int(s[i])
    i+=1
print(su)

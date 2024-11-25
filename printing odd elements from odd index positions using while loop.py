s=input()
i=0
while i<len(s):
    if s[i].isdigit():
        if int(s[i])%2!=0 and i%2!=0:
            print(s[i])

    i+=1

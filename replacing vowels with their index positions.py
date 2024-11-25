s=input()
v='aeiouAEIOU'
n=''
for i in range(len(s)):
    if s[i] in v:
        n+=str(i)
    else:
        n+=s[i]
print(n)


''' s='hello'
iteration 1: it will extract 'h' and check h is in vowels false so concatenate 'h' to n so n='h'
iteration 2: it will extract 'e' and check e is in vowels true so concatenate index position of 'e' to n so n='h1'
iteration 3: it will extract 'l' and check l is in vowels false so concatenate 'l' to n so n='h1l'
iteration 4: it will extract 'l' and check l is in vowels false so concatenate 'l' to n so n='h1ll'
iteration 5: it will extract 'o' and check o is in vowels true so concatenate index position of 'o' to n so n='h1ll5'

'''


# 2) for inside while loop

# case 1) executing both inner and outer loop completely


i=1
while i<4:
    for j in range(1,4):
        print(i,j)
    i+=1

'''

iteration 1 for outer loop:i is intialized with 1 check 1<4 true so enter into inner for loop with i=1
                 iteration 1:i=1,j is intialized with 1 and print i,j =1,1
                 iteration 2:i=1,j becomes 2 and print i,j =1,2
                 iteration 3:i=1,j becomes 3 and print i,j =1,3
iteration 2 for outer loop:now i  is 2 check 2<4 true so enter into inner for loop with i=2
                 iteration 1:i=2,j is intialized with 1 and print i,j =2,1
                 iteration 2:i=2,j becomes 2 and print i,j =2,2
                 iteration 3:i=2,j becomes 3 and print i,j =2,3

iteration 3 for outer loop:now i  is 3 check 3<4 true so enter into inner for loop with i=3
                 iteration 1:i=3,j is intialized with 1 and print i,j =3,1
                 iteration 2:i=3,j becomes 2 and print i,j =3,2
                 iteration 3:i=3,j becomes 3 and print i,j =3,3

iteration 4 for outer loop:now i  is 4 check 4<4 false so execution stops
'''

# case 2) breaking inner loop with inner loop value


i=1
while i<4:
    for j in range(1,4):
        print(i,j)
        if j==2:
            break
    i+=1

'''
iteration 1 for outer loop:i is intialized with 1 check 1<4 true so enter into inner for loop with i=1
                 iteration 1:i=1,j is intialized with 1 and print i,j =1,1 and check j==2 false 
                 iteration 2:i=1,j becomes 2 and print i,j =1,2 and check j==2 true so break the inner loop
iteration 2 for outer loop: now i is 2 check 2<4 true so enter into inner for loop with i=2
                 iteration 1:i=2,j is intialized with 1 and print i,j =2,1 and check j==2 false 
                 iteration 2:i=2,j becomes 2 and print i,j =2,2 and check j==2 true so break the inner loop
iteration 3 for outer loop: now i is 3 check 3<4 true so enter into inner for loop with i=3
                 iteration 1:i=3,j is intialized with 1 and print i,j =3,1 and check j==2 false 
                 iteration 2:i=3,j becomes 2 and print i,j =3,2 and check j==2 true so break the inner loop
iteration 4 for outer loop:now i  is 4 check 4<4 false so execution stops
'''

# case 3) breaking inner loop with outer loop value


i=1
while i<4:
    for j in range(1,4):
        print(i,j)
        if i==2:
            break
    i+=1

'''
iteration 1 for outer loop:i is intialized with 1 check 1<4 true so enter into inner for loop with i=1
                 iteration 1:i=1,j is intialized with 1 and print i,j =1,1 and check i==2 false 
                 iteration 2:i=1,j becomes 2 and print i,j =1,2 and check i==2 false
                 iteration 3:i=1,j becomes 3 and print i,j =1,3 and check i==2 false

iteration 2 for outer loop: now i is 2 check 2<4 true so enter into inner for loop with i=2
                 iteration 1:i=2,j is intialized with 1 and print i,j =2,1 and check i==2 true so break the inner loop 

iteration 3 for outer loop:i is intialized with 3 check 3<4 true so enter into inner for loop with i=3
                 iteration 1:i=3,j is intialized with 1 and print i,j =3,1 and check i==2 false 
                 iteration 2:i=3,j becomes 2 and print i,j =3,2 and check i==2 false
                 iteration 3:i=3,j becomes 3 and print i,j =3,3 and check i==2 false
iteration 4 for outer loop:now i  is 4 check 4<4 false so execution stops
'''

 # case 4) breaking outer loop with inner loop value


i=1
while i<4:
    for j in range(1,4):
        print(i,j)
    if j==3:
        break
    i+=1

''' iteration 1 for outer loop:i is intialized with 1 check 1<4 true so enter into inner for loop with i=1
                 iteration 1:i=1,j is intialized with 1 and print i,j =1,1 
                 iteration 2:i=1,j becomes 2 and print i,j =1,2 
                 iteration 3:i=1,j becomes 3 and print i,j =1,3


                 after completition of inside loop j is 3 and check j==3 true so break outer loop
'''


 # case 5) breaking outer loop with outer loop value


i=1
while i<4:
    if i==2:
        break
    for j in range(1,4):
        print(i,j)
   
    i+=1


'''
iteration 1 for outer loop:i is intialized with 1 check 1<4 true and checks i==2 false enter into inner loop 
                 iteration 1:i=1,j is intialized with 1 and print i,j =1,1 
                 iteration 2:i=1,j becomes 2 and print i,j =1,2 
                 iteration 3:i=1,j becomes 3 and print i,j =1,3
iteration 2 for outer loop: now i is 2 check 2<4 true and checks i==2 true so break the outer loop
'''
                
                 

                

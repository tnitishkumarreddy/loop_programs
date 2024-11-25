#  while inside while loop

# case 1: executing both inner and outer loop completely


i=1
while i<4:
    j=1
    while j<4:
        print(i,j)
        j+=1
    i+=1



'''
outer loop iteration 1:i is intialized with 1,and check 1<4 true and j becomes 1 and enter into inner while loop
           iteration 1:j=1 check 1<4 true and print i,j=1,1 now j becomes 2
           iteration 2:j=2 check 2<4 true and print i,j=1,2 now j becomes 3
           iteration 3:j=3 check 3<4 true and print i,j=1,3 now j becomes 4
           iteration 4:j=4 check 4<4 false 
outer loop iteration 2:i become 2 and check 2<4 true and j becomes 1 and enter into inner while loop
           iteration 1:i=2,j=1 check 1<4 true and print i,j=2,1 now j becomes 2
           iteration 2:i=2,j=2 check 2<4 true and print i,j=2,2 now j becomes 3
           iteration 3:i=2,j=3 check 3<4 true and print i,j=2,3 now j becomes 4
           iteration 4:i=2,j=4 check 4<4 false
outer loop iteration 3:i become 3 and check 3<4 true and j becomes 1 and enter into inner while loop
           iteration 1:i=3,j=1 check 1<4 true and print i,j=3,1 now j becomes 2
           iteration 2:i=3,j=2 check 2<4 true and print i,j=3,2 now j becomes 3
           iteration 3:i=3,j=3 check 3<4 true and print i,j=3,3 now j becomes 4
           iteration 4:i=2,j=4 check 4<4 false
outer loop iteration 4:now i becomes 4 and check 4<4 false so not enter  into inner loop.


# case 2: break inner loop with inner loop value

i=1
while i<4:
    j=1
    while j<4:
        if j==3:
            break
        print(i,j)
        j+=1
    i+=1


outer loop iteration 1:i is intialized with 1,and check 1<4 true and j becomes 1 and enter into inner while loop
           iteration 1:i=1,j=1 check 1<4 true and check j==3,1==3 false so print i,j=1,1 and j becomes 2
           iteration 2:i=1,j=2 check 2<4 true and check j==3,2==3 false so print i,j=1,2 and j becomes 3
           iteration 3:i=1,j=3 check 3<4 true and check j==3,3==3 true so break the inner loop now i incremented to 2
outer loop iteration 2:i becomes 2,and check 2<4 true and j becomes 1 and enter into inner while loop
           iteration 1:i=2,j=1 check 1<4 true and check j==3,1==3 false so print i,j=2,1 and j becomes 2
           iteration 2:i=2,j=2 check 2<4 true and check j==3,2==3 false so print i,j=2,2 and j becomes 3
           iteration 3:i=2,j=3 check 3<4 true and check j==3,3==3 true so break the inner loop now i incremented to 3
outer loop iteration 3:i becomes 3,and check 3<4 true and j becomes 1 and enter into inner while loop
           iteration 1:i=3,j=1 check 1<4 true and check j==3,1==3 false so print i,j=3,1 and j becomes 2
           iteration 2:i=3,j=2 check 2<4 true and check j==3,2==3 false so print i,j=3,2 and j becomes 3
           iteration 3:i=3,j=3 check 3<4 true and check j==3,3==3 true so break the inner loop now i incremented to 4
outer loop iteration 4:now i=4 and check 4<4 false not enter .
'''


# case 3: break inner loop with outer loop value

i=1
while i<4:
    j=1
    while j<4:
        if i==3:
            break
        print(i,j)
        j+=1
    i+=1


'''outer loop iteration 1:i is intialized with 1,and check 1<4 true and j becomes 1 and enter into inner while loop
           iteration 1:i=1,j=1 check 1<4 true and check i==3,1==3 false so print i,j=1,1 and j becomes 2
           iteration 2:i=1,j=2 check 2<4 true and check i==3,1==3 false so print i,j=1,2 and j becomes 3
           iteration 3:i=1,j=3 check 3<4 true and check i==3,1==3 false so print i,j=1,3 and j becomes 4
           iteration 4:now j=4 and check 4<4 false .
outer loop iteration 2:i becomes 2,and check 2<4 true and j becomes 1 and enter into inner while loop
           iteration 1:i=2,j=1 check 1<4 true and check i==3,2==3 false so print i,j=2,1 and j becomes 2
           iteration 2:i=2,j=2 check 2<4 true and check i==3,2==3 false so print i,j=2,2 and j becomes 3
           iteration 3:i=2,j=3 check 3<4 true and check ==3,2==3 false so print i,j =2,3 and j becomes 4
           iteration 4:now j=4 and check 4<4 false.
outer loop iteration 3:i becomes 3,and check 3<4 true and j becomes 1 and enter into inner while loop
           iteration 1:i=3,j=1 check 1<4 true and check i==3,3==3 true so break inner loop
outer loop iteration 4:now i=4 check 4<4 false not work.

           

'''
# case 4: break outer loop with outer loop value

i=1
while i<4:
    if i==2:
        break
    j=1
    while j<4:
        print(i,j)
        j+=1
    i+=1

'''
outer loop iteration 1:i is intialized with 1,and check 1<4 true and checks i==2,1==2 false so j =1
           iteration 1:i=1,j=1 check 1<4 true and print i,j=1,1 now j becomes 2
           iteration 2:i=1,j=2 check 2<4 true and print i,j=1,2 now j becomes 3
           iteration 3:i=1,j=3 check 3<4 true and print i,j=1,3 now j becomes 4
           iteration 4:i=1,j=4 check 4<4 false now i incremented to 2

outer loop iteration 2:i becomes 2,and check 2<4 true and check i==2,2==2 true so break the outer loop so not works outer loop'''
# case 5: break outer loop with inner loop value

i=1
while i<4:
    j=1
    while j<4:
        print(i,j)
        j+=1
    if j==4:
        break
    i+=1
'''
outer loop iteration 1:i is intialized with 1,and check 1<4 true and j becomes 1 and enter into inner while loop
           iteration 1:j=1 check 1<4 true and print i,j=1,1 now j becomes 2
           iteration 2:j=2 check 2<4 true and print i,j=1,2 now j becomes 3
           iteration 3:j=3 check 3<4 true and print i,j=1,3 now j becomes 4
           iteration 4:j=4 check 4<4 false so check if condition j==4 ,4==4 true so break the outer loop '''


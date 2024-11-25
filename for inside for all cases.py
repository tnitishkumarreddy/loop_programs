#  1) for inside for

# case 1:- executing both inner and outer loop completely

for i in range(1,4):
    for j in range(1,3):
        print(i,j)


'''

iteration 1 for outer loop: first i is initialized with 1 and enters into inner for loop
                            iteration 1: i=1 and j is intialized with 1 and print i,j=1,1
                            iteration 2: i=1 and j becomes 2 and print i,j=1,2
                            iteration 3: i=1 and j becomes 3 and print i,j=1,3
iteration 2 for outer loop: now i becomes 2 and enters into inner for loop
                            iteration 1: i=2 and j is intialized with 1 and print i,j=2,1
                            iteration 2: i=2 and j becomes 2 and print i,j=2,2
                            iteration 3: i=2 and j becomes 3 and print i,j=2,3
iteration 3 for outer loop: now i becomes 3 and enters into inner for loop
                            iteration 1: i=3 and j is intialized with 1 and print i,j=3,1
                            iteration 2: i=3 and j becomes 2 and print i,j=3,2
                            iteration 3: i=3 and j becomes 3 and print i,j=3,3

'''


# case 2 : breaking inner loop with inner loop value


for i in range(1,4):
    for j in range(1,4):
        if j==2:
            break
        print(i,j)


'''
iteration 1 for outer loop: first i is initialized with 1 and enters into inner for loop
                            iteration 1: i=1 and j is intialized with 1 and check j==2 false so print i,j as 1,1
                            iteration 2: i=1 and j is becomes 2 and check j==2 true so break the inner loop
iteration 2 for outer loop: now i becomes 2 and enters into inner for loop
                            iteration 1: i=2 and j is intialized with 1 and check j==2 false print i,j=2,1
                            iteration 2: i=2 and j becomes 2 and check j==2 true so break the inner loop
iteration 3 for outer loop: now i becomes 3 and enters into inner for loop
                            iteration 1: i=3 and j is intialized with 1 and check j==2 false print i,j=3,1
                            iteration 2: i=3 and j becomes 2 and check j==2 true so break the inner loop
'''


# case 3 : breaking inner loop with outer loop value


for i in range(1,4):
    for j in range(1,4):
        if i==2:
            break
        print(i,j)


'''

iteration 1 for outer loop: first i is initialized with 1 and enters into inner for loop
                            iteration 1: i=1 and j is intialized with 1 and check i==2 false print i,j=1,1
                            iteration 2: i=1 and j becomes 2 and check i==2 false printi,j=1,2
                            iteration 3: i=1 and j becomes 3 and check i==2 false print i,j=1,3
iteration 2 for outer loop: now i becomes 2 and enters into inner for loop
                            iteration 1: i=2 and j is intialized with 1 and check i==2 true so break inner loop 
iteration 3 for outer loop: now i becomes 3 and enters into inner for loop
                            iteration 1: i=3 and j is intialized with 1 and check i==2 false print i,j=3,1
                            iteration 2: i=3 and j becomes 2 and check i==2 false printi,j=3,2
                            iteration 3: i=3 and j becomes 3 and check i==2 false print i,j=3,3
'''


# case 4 : breaking outer loop with outer loop value


for i in range(1,4):
    if i==2:
        break
    for j in range(1,4):
        print(i,j)


'''
iteration 1 for outer loop: first i is initialized with 1 and check i==2 false so enter into inner for loop
                        iteration 1: i=1 and j is initialized with 1  and print i,j=1,1
                        iteration 2: i=1 and j becomes 2 and print i,j=1,2
                        iteration 3: i=1 and j becomes 3 and print i,j=1,3
iteration 1 for outer loop: now i becomes 2 and check i==2 true so break the outer loop

'''

# case 5 : breaking outer loop with inner loop value


for i in range(1,4):
    for j in range(1,4):
        print(i,j)
    if j==3:
        break
'''
iteration 1 for outer loop: first i is initialized with 1 and enters into inner for loop
                          iteration 1: i=1 and j is intialized with 1 and check i==2 false print i,j=1,1
                          iteration 2: i=1 and j becomes 2 and check i==2 false printi,j=1,2
                          iteration 3: i=1 and j becomes 3 and check i==2 false print i,j=1,3

                          after complete iterations of inner loop j is coming out with value 3 and after inner loop check j==3 true so break the outer loop

'''

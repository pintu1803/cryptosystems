

#Pintu, 181CO139
#09-02-2021
#Miller-Rabin Primality Test.
#Theory:
# If n is a even number then it is not prime, obviously.for
# Now, n has to be odd to check its primality test.
# So, every odd number can be converted to even, by subtracting 1 from it. Do this: n = n - 1.
# Now, n become a even number. Every even number can be represented as: (n-1) = d.2^s, where d is some odd number.
# Now, we apply fermat's test in a differnt way. Chosse a in range[2, n-2]
# see if a^(n-1) = 1 mod n so, a^(d.2^s)=1 mod n.
# 1st see this: a^d mod n ==1 or == -1, if either satisfies then n is prime. cause, ((a^d)mod n)^(2^s)mod n= a^(d.2^s)mod n = a^(n-1)mod n= 1
# and 2^s is even. THus, fermat's theorem says n is probabalistic prime.
# if neither condition satisfies, then use all powers of 2, except last one.
# so, rest of the code follows.

import random
import time

#Utility function for Miller-Rabin primality test
def miller_rabin_utility(n,k):
    #observe the corner cases
    if(n==4 or n<=1 or n%2==0):
        return False
    elif(n<=3):
        return True
    #go for testing.
    s=0
    d=n-1
    while d%2==0:
        s+=1
        d//=2
    #now you expressed; n-1=2^(d*2^s)
    for i in range(k):
        # select a randon number.
        x = random.randint(2, n - 2)
        # if x^d mod n=1 or -1
        x = pow(x, d, n)
        if (x == 1 or x == n - 1):
            continue
            #return True#if called from a function.
        # now, go for 2^r where 0 =< r =< s-1
        k = 0
        flag=0
        while k != s - 1:
            x = (x * x) % n
            k += 1
            if (x == 1):
                return False
            if (x == n - 1):
                flag=1
                break
                #return True#if called from a function.
        else:
            if flag==1:
                continue
            else:
                return False
    else:
        return True

#####################################
n=int(input("Enter number="))
k=100
t=time.time()
result=miller_rabin_utility(n,k)
print("Number you gave is Prime?",result)
print("Time taken by the algorithm is=",time.time()-t)
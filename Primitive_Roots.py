

#Pintu, 181CO139
#08-02-2021
# Primitive roots of mod n.
# Primitive root of mod n is 'a' if the order of a mod n = phi(n)
# Number of primitive roots of mod n = phi(phi(n))
#The execution time of program is also calculated.

import time

#Function to find GCD of two numbers.
def gcd(a,b):
    if a<b:
        gcd(b,a)
    if a%b==0:
        return b
    else:
        return gcd(b,a%b)

#Function to find the phi(n) and coprimes of n.
def phi_and_coprimes(n):
    phi=0
    coprimes=[]
    for i in range(1,n):
        if gcd(n,i)==1:
            phi+=1
            coprimes.append(i)
    return phi,coprimes

#Function to find the order of a modulo n.
def order(a,n):
    for exp in range(1,n):
        if pow(a,exp,n)==1:
            return exp

#Function to find the primitive_roots of mod N.
def primitive_roots(n,phi,coprimes):
    primitiveroots=[]
    for num in coprimes:
        if order(num,n)==phi:
            primitiveroots.append(num)
    return primitiveroots

#Main function.
def main():
    start_time=time.time()
    n=int(input("Enter value of N="))

    phi, coprimes = phi_and_coprimes(n)
    primitiveroots=primitive_roots(n,phi,coprimes)
    number_of_roots=len(primitiveroots)

    print("Total number of primitive roots of mod {} are= {}".format(n,number_of_roots))
    print("Primitive root(s) are=",primitiveroots)

    choice=input("\nDo you want to see solution(y/n)=")
    if choice=='y':
        print("Given modulo N=",n)
        print("Coprimes from 1 to n-1 are=",coprimes)
        print("Phi of N=",phi)
        for num in coprimes:
            print("Order of {} mod {} is {}".format(num, n, order(num, n)))
        print("Number of roots= Phi of {}= {}".format(phi,number_of_roots))
        print("Primitive root(s) are=", primitiveroots)
    print("Total execution time of program is=%.2f seconds"%(time.time()-start_time))
if __name__ == '__main__':
    main()
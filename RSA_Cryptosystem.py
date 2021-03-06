

#08-02-2021, Pintu
#181CO139
#Our aim is to implement the RSA Cryptosystem in python.

import random

#Function for primality test.
#Fermat's primality test
def isPrime(n,k):
    if n<=1 or n==4:
        return False
    elif n<=3:
        return True
    else:
        for i in range(k):
            a=random.randint(2,n-2)
            if pow(a,n-1,n)!=1:
                return False
    return True

#Function to generate the large prime numbers.
def Generate_Large_Prime(p):
    n=random.randint(pow(10,20),pow(10,30))
    while isPrime(n,1)==False or n==p:
        n = random.randint(pow(10, 20), pow(10, 30))
    return n

#Function to find the gcd of two numbers.
def gcd(a,b):
    if a<b:
        gcd(b,a)
    elif a%b==0:
        return b
    return gcd(b,a%b)

#Function to generate public key.
def Public_Key(phi):
    e=random.randint(2,phi)
    while gcd(e,phi)!=1:
        e=random.randint(2,phi)
    return e

#Function to find the inverse of e modulo phi(n).
def Inverse(a,n):
    t,new_t=0,1
    r,new_r=n,a
    while new_r!=0:
        quotient=r//new_r
        r,new_r=new_r, r-quotient*new_r
        t,new_t=new_t, t-quotient*new_t
    if r>1:
        print("Not invertible")
    if t<0:
        t=t+n
    return t

#FUnction to encrypt the given message.
def encryption(message,e,n):
    enc_msg=[]
    for ch in message:
        enc_msg.append(pow(ord(ch),e,n))
    return enc_msg

#Funtion to decrypt the encrypted message.
def decryption(enc_msg,d,n):
    dec_msg=[]
    for ch in enc_msg:
        dec_msg.append(chr(pow(ch,d,n)))
    dec_msg="".join(ch for ch in dec_msg)
    return dec_msg

#Main Function
def main():
    message=input("Enter the message to encrypt=")
    p=Generate_Large_Prime(1)
    q=Generate_Large_Prime(p)
    n=p*q
    phi=(p-1)*(q-1)
    e=Public_Key(phi)
    d=Inverse(e,phi)

    enc_msg=encryption(message,e,n)
    dec_msg=decryption(enc_msg,d,n)

    print("Your plaintext is=\"{}\"".format(dec_msg))
    print("\nPublic Key Pair=(e={},n={})".format(e,n))
    print("Private Key Pair=(d={},n={})".format(d,n))



if __name__ == '__main__':
    main()

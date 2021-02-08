

#07-02-2021, Pintu, 181CO139
#Our aim is to implement the ELGAMAL cryptosystem in python.

import random

#Function to calculate the GCD.
def gcd(a,b):
    if a<b:
        gcd(b,a)
    if a%b==0:
        return b
    return gcd(b,a%b)

#Function to generated the private keys.
def Gen_Key(q):
    key=random.randint(pow(10,20), q)
    while gcd(key,q)!=1:
        key=random.randint(pow(10,20), q)
    return key

#Function to calculate Modular Exponentiation.
def modexp(a,b,c):
    #return a^b mod c
    return pow(a,b,c)

#Function to encrypt the message.
def encryption(message,g,h,q):
    ciphertext=[]
    k=Gen_Key(q)
    p=modexp(g,k,q)
    s=modexp(h,k,q)
    for ch in message:
        ciphertext.append(ord(ch)*s)
    return ciphertext,p

#Function to decrypt the message.
def decryption(cipher,p,a,q):
    plaintext=[]
    ss=modexp(p,a,q)
    for ele in cipher:
        plaintext.append(chr(int(ele/ss)))
    plaintext="".join(character for character in plaintext)
    return plaintext

#Main function is here.
def main():
    message=input("Enter the message to encrypt=")
    q=random.randint(pow(10,20), pow(10,50))
    a=Gen_Key(q)
    g=random.randint(2,q)
    h=modexp(g,a,q)
    encrypted_message,p=encryption(message,g,h,q)
    decrypted_message=decryption(encrypted_message,p,a,q)
    print("Your Plaintext is=\"{}\"".format(decrypted_message))

    print("Public key is=\nq={}\ng={}\nh={}".format(q, g, h))
    print("Private key is=\na={}".format(a))

if __name__ == '__main__':
    main()

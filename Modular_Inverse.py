

#08-02-2021
#Pintu, 181CO139
#Out aim is to find the modular inverse of: a mod n
#Let v is the inverse of a modulo n, then a.v modulo n = 1

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

def main():
    a=int(input("Enter value of a="))
    n=int(input("Enter value of n="))
    mod_inv=Inverse(a,n)
    print("Multiplicative Inverse of {} modulo {} is= {}".format(a,n,mod_inv))

if __name__=='__main__':
    main()

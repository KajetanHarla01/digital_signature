import random
from sympy import *
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa

def generate_keys_params(trn_list, key_length=1024, e=65537):
    if len(trn_list)*16 < key_length:
        print("Error: source audio file is too short")
        exit()
    q = 0
    p = 0

    #Generate p and q values
    for i in range(int(key_length/8)):
        index = random.randint(0, len(trn_list) - 1)
        if i==0:
           num = trn_list[index]
           while num < 128:
               index = random.randint(0, len(trn_list) - 1)
               num = trn_list[index]
        p += trn_list[index]*(pow(2, (int(key_length/8)-i-1)*8))
        trn_list.pop(index)
    for i in range(int(key_length/8)):
        index = random.randint(0, len(trn_list) - 1)
        if i==0:
           num = trn_list[index]
           while num < 128:
               index = random.randint(0, len(trn_list) - 1)
               num = trn_list[index]
        q += trn_list[index]*(pow(2, (int(key_length/8)-i-1)*8))
        trn_list.pop(index)
    
    # Make sure that p and q are prime numbers
    p = prevprime(p)
    q = nextprime(q)
    
    # Compute private exponent - d
    n = p*q
    phi_n = (p-1)*(q-1)
    d = pow(e, -1, phi_n)

    public_numbers = rsa.RSAPublicNumbers(
        e=e,
        n=n
    )
    private_numbers = rsa.RSAPrivateNumbers(
        p=p,
        q=q,
        d=d,
        dmp1=d%(p-1),
        dmq1=d%(q-1),
        iqmp=pow(q, -1, p),
        public_numbers=public_numbers
    ).private_key(default_backend())

    return private_numbers, public_numbers

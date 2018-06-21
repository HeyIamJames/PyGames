import hashlib, binascii

t='123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'

def numtowif(numpriv):
    step1 = '80'+hex(numpriv)[2:].strip('L').zfill(64)
    step2 = hashlib.sha256(binascii.unhexlify(step1)).hexdigest()
    step3 = hashlib.sha256(binascii.unhexlify(step2)).hexdigest()
    step4 = int(step1 + step3[:8] , 16)
    return ''.join([t[step4/(58**l)%58] for l in range(100)])[::-1].lstrip('1')

def wiftonum(wifpriv):
     return sum([t.index(wifpriv[::-1][l])*(58**l) for l in range(len(wifpriv))])/(2**32)%(2**256)

def validwif(wifpriv):
    return numtowif(wiftonum(wifpriv))==wifpriv

print numtowif(0x0C28FCA386C7A227600B2FE50B7CAE11EC86D3BF1FBE471BE89827E19D72AA1D)
print hex(wiftonum('5HueCGU8rMjxEXxiPuD5BDku4MkFqeZyd4dZ1jvhTVqvbTLvyTJ'))
print validwif('5HueCGU8rMjxEXxiPuD5BDku4MkFqeZyd4dZ1jvhTVqvbTLvyTJ')
print validwif('5HueCGU8rMjxEXxiPuD5BDku4MkFqeZyd4dZ1jvhTVqvbTLvyTK')

private_key = "E9873D79C6D87DC0FB6A5778633389F4453213303DA61F20BD67FC233AA33262"
private_key = BitcoinPrivateKey(E9873D79C6D87DC0FB6A5778633389F4453213303DA61F20BD67FC233AA33262)
private_key.public_key(w).address()

#fib using generators
def fibonacci(n):
    curr = 1
    prev = 0
    counter = 0
    while counter < n:
        yield curr
        prev, curr = curr, prev + curr
        counter += 1

def compress(input_str):
    new_str = ""
    counter = 0
    for i in input_str:
        if new_str[-1:] != i:
            new_str += i
            counter += 1
        elif new_str[-1:] == i:
            counter += 1
            new_str += str(counter)
    return new_str

compress("jjjamesssss")

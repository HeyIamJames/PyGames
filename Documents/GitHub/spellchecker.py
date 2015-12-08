from bitmap  import Bitmap
from hashlib import md5

def makeHashes(word) :
    hex32 = md5(word).hexdigest()
    hashes = []
    for i in range(0,30,5) :
        hashes.append(int(hex32[i:i+5],16))
    return hashes

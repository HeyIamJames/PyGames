from bitmap  import Bitmap
from hashlib import md5

def makeHashes(word) :
    hex32 = md5(word).hexdigest()
    hashes = []
    for i in range(0,30,5) :
        hashes.append(int(hex32[i:i+5],16))
    return hashes

def loadBitmap(file) :
    words = open(file).readlines()
    words = map(lambda x: x.strip(), words) 
    bmap  = Bitmap(2**20)
    for word in words :
        hashes = makeHashes(word)
        for hash in hashes :
            bmap.setBit(hash)
    return bmap

def checkWord(bmap, word) :
    hashes = makeHashes(word)
    for hash in hashes :
        if not bmap.getBit(hash): return False
    return True

def main() :
    import sys, re
    bmap  = loadBitmap(sys.argv[1])  
    text  = sys.stdin.read()        
    words = re.sub("[^a-zA-Z'-]"," ",text).lower().split()
    for word in words :
        print " %-6s %s" % (checkWord(bmap,word),word)

if __name__ == "__main__" : main()

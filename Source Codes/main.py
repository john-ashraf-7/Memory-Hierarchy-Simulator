from inputReader import *
from cache import *

#read data from user
addrLength, addresses, memorySize, memoryAccessTime, cacheLineSize, cacheSize, cacheAccessTime = readUserData()
cache = initialize_cache(cacheSize, cacheLineSize)
readFromMemory(cache, addrLength, addresses, memorySize, memoryAccessTime, cacheLineSize, cacheSize, cacheAccessTime);

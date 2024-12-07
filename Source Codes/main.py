from inputReader import *
from cache import *

#read data from user
addrLength, memorySize, memoryAccessTime, cacheLineSize, cacheSize, cacheAccessTime = readUserData()


readFromMemory(addrLength, memorySize, memoryAccessTime, cacheLineSize, cacheSize, cacheAccessTime);
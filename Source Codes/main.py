from inputReader import *
from cache import *

#read data from user
addrLength, addresses, memorySize, memoryAccessTime, cacheLineSize, cacheSize, cacheAccessTime = readUserData()
hit_count, miss_count, total_cycles = readFromMemory(addrLength, addresses, memorySize, memoryAccessTime, cacheLineSize, cacheSize, cacheAccessTime);

#calculate hit, miss ratios.
hit_ratio = hit_count/len(addresses)

#AMAT = Hit time + Miss rate × Miss penalty
AMAT = (memoryAccessTime) + miss_ratio*(memoryAccessTime + cacheAccessTime); 
miss_ratio = 1 - hit_ratio
print("hit_ratio = ", hit_ratio)
print("miss_ratio = ", miss_ratio)
print("total number of cycles = ", total_cycles)
print("AMAT = ", AMAT)

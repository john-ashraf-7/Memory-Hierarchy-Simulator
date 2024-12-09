from inputReader import *
from cache import *

# Read data from user
addrLength, addresses, memorySize, memoryAccessTime, cacheLineSize, cacheSize, cacheAccessTime = readUserData()
hit_count, miss_count, total_cycles, cache = readFromMemory(addrLength, addresses, memorySize, memoryAccessTime, cacheLineSize, cacheSize, cacheAccessTime)

# Calculate hit, miss ratios
hit_ratio = hit_count / len(addresses)
miss_ratio = 1 - hit_ratio  # Calculate miss_ratio after hit_ratio

# AMAT = Hit time + Miss rate × Miss penalty
AMAT = cacheAccessTime + miss_ratio * (memoryAccessTime + cacheAccessTime)

print("hit_ratio = ", hit_ratio)
print("miss_ratio = ", miss_ratio)
print("total number of cycles = ", total_cycles)
print("AMAT = ", AMAT)
print_cache(cache)

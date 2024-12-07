import math
def hit():
    print("Hit!")
def miss():
    print("Miss!")

def initialize_cache(cacheSize, cacheLineSize):
    # Number of lines (or indices) in the cache
    number_of_lines = int(cacheSize / cacheLineSize)

    # Initialize the cache as a list of dictionaries
    cache = [{'data': None, 'V': 0, 'tag': None} for _ in range(number_of_lines)]
    return cache

# Example usage
cacheSize = 1024  # Total cache size in bytes
cacheLineSize = 16  # Size of each cache line in bytes
cache = initialize_cache(cacheSize, cacheLineSize)

def readFromMemory(cache, addrLength, addresses, memorySize, memoryAccessTime, cacheLineSize, cacheSize, cacheAccessTime):
    number_of_lines = int(cacheSize / cacheLineSize)

    for address in addresses:
        binary_address = bin(address)[2:].zfill(addrLength)  # Ensure proper zero-padding to addrLength
        print(f"address: {binary_address}")

        binary_address_length = len(binary_address)
        displacement_length = int(math.log2(cacheLineSize))
        index_length = int(math.log2(number_of_lines))
        tag_length = binary_address_length - index_length - displacement_length

        #extracting tag,index,data from the binary address
        data = binary_address[-displacement_length:]
        index = binary_address[-(displacement_length + index_length):-displacement_length]
        tag = binary_address[:-(displacement_length + index_length)]

        print(f"data (displacement): {data}")
        print(f"index: {index}")
        print(f"tag: {tag}")
        print()

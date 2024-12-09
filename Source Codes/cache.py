import math

def initialize_cache(cacheSize, cacheLineSize, displacement):
    # Number of lines (or indices) in the cache
    number_of_lines = int(cacheSize / cacheLineSize)

    # Initialize the cache as a 2D list
    # Each row corresponds to a cache line
    #each column corresponds to a different byte in a range of "displacement"
    cache = [[{'data': None, 'V': False, 'tag': None} for _ in range(2**displacement)] for _ in range(number_of_lines)]
    return cache
# to update the cache in cases of miss
def update_cache(cache, index, displacement, tag): #used when we detect a miss
    for i in range(2**displacement):
        cache[index][i]['V'] = True  # Mark as valid
        cache[index][i]['tag'] = tag  # Update the tag
        cache[index][i]['data'] = bin(i)[2:].zfill(displacement)  # Placeholder for data if needed

def print_cache(cache):
    """
    Print the state of the cache in a structured format.

    :param cache: The 2D list representing the cache.
    """
    print("\nCurrent Cache State:")
    print("-" * 50)
    for line_index, line in enumerate(cache):
        print(f"Line {line_index}:")
        for byte_index, entry in enumerate(line):
            data = entry['data']
            valid = entry['V']
            tag = entry['tag']
            print(f"  Byte {byte_index} -> Valid: {valid}, Tag: {tag}, Data: {data}")
        print("-" * 50)

def readFromMemory(addrLength, addresses, memorySize, memoryAccessTime, cacheLineSize, cacheSize, cacheAccessTime):
    number_of_lines = int(cacheSize / cacheLineSize)
    hit_count = 0
    miss_count = 0;
    total_cycles = 0;
    displacement = int(math.log2(cacheLineSize))
    index_length = int(math.log2(number_of_lines))
    cache = initialize_cache(cacheSize, cacheLineSize, displacement)

    for address in addresses:
        binary_address = bin(address)[2:].zfill(addrLength)  # Ensure proper zero-padding to addrLength
        print(f"address: {binary_address}")

        # binary_address_length = len(binary_address)
        # tag_length = binary_address_length - index_length - displacement

        #extracting tag,index,data from the binary address
        data = binary_address[-displacement:]
        index = binary_address[-(displacement + index_length):-displacement]
        tag = binary_address[:-(displacement + index_length)]

        #start accessing the cache.
        index = int(index,2) #convert index to decimal
        tag = int(tag,2) #convert tag to decimal
        data = int(data,2) #convert data to decimal

        # Inspect The Cache
        # this part is left for Reem
        # if(cache[index][data]['V']):
        #    if(cache[index][data]['tag'] == tag):
        #         # that's a hit.
        #        hit_count +=1;
        #        total_cycles += cacheAccessTime
        # else:
        #     # that's a miss, now transfer the entire line (this index with all its data to the cache and mark V as true)
        #    miss_count+=1;
        #    total_cycles += memoryAccessTime + cacheAccessTime
        #    update_cache(cache, index, displacement, tag)


        if cache[index][data]['V']:
            if cache[index][data]['tag'] == tag:
                # Cache hit
                hit_count += 1
                total_cycles += cacheAccessTime
                print("Hit!")
                print(f"Number of hits: {hit_count}")
                print(f"Number of Misses: {miss_count}")
            else:
                # Cache miss: update the cache for this line
                miss_count += 1
                total_cycles += memoryAccessTime + cacheAccessTime
                update_cache(cache, index, displacement, tag)
                print("Miss.")
                print(f"Number of hits: {hit_count}")
                print(f"Number of Misses: {miss_count}")
        else:
            # Cache miss: update the cache for this line
            miss_count += 1
            total_cycles += memoryAccessTime + cacheAccessTime
            update_cache(cache, index, displacement, tag)
            print("Miss.")
            print(f"Number of hits: {hit_count}")
            print(f"Number of Misses: {miss_count}")



        print(f"data (displacement): {data}")
        print(f"index: {index}")
        print(f"tag: {tag}")
        print()
        # print_cache(cache)
    return hit_count, miss_count, total_cycles, cache

import accessSequences#contains the functions that generate static set of files containing random accessed addresses

addrLength=int(input("Enter the length of the address between 16 and 40:"))
#to verify the input
while addrLength< 16 or addrLength > 40:
	print("invalid input! please try again")
	addrLength=int(input("Enter the length of the address between 16 and 40:"))
# the function returns the total size of the memory
memorySize=accessSequences.generateAddresses(addrLength)

memoryAccessTime=int(input("Enter the memory access time in cycles between 50 and 200:"))
while memoryAccessTime< 50 or memoryAccessTime> 200:
	print("invalid input! please try again")
	memoryAccessTime=int(input("Enter the memory access time in cycles between 50 and 200:"))

cacheLineSize=int(input("Enter the cache line size in bytes between 32 and 64:"))
while cacheLineSize < 32 or cacheLineSize > 64:
	print("invalid input! please try again")
	cacheLineSize=int(input("Enter the cache line size in bytes between 32 and 64:"))

cacheSiz=int(input("Enter the cache size in bytes:"))
while cacheSiz< (2*cacheLineSize)or cacheSiz> memorySize/2:
	print("invalid input! please try again")
	cacheSiz=int(input("Enter the cache size in bytes:"))

cacheAccessTime=int(input("Enter the cache access time in cycles between 1 and 10:"))
while cacheAccessTime< 1 or cacheAccessTime> 10:
	print("invalid input! please try again")
	cacheAccessTime=int(input("Enter the cache access time in cycles between 1 and 10:"))

with open("sequence0.txt") as file:
	addrs=file.read()
addrs=addrs.split(",")
addrs=list(map(int,addrs))#converting the numbers from string to integers 
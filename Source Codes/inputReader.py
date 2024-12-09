import accessSequences #contains the functions that generate static set of files containing random accessed addresses

def readUserData():
	#the below commented out block is for testing
	# addrLength=16
	# memorySize=accessSequences.generateAddresses(addrLength)
	# memoryAccessTime = 50
	# cacheLineSize = 32
	# cacheAccessTime = 1
	# filename = "customtest.txt"


	addrLength=int(input("Enter the length of the address between 16 and 40:"))
	#to verify the input
	while addrLength < 16 or addrLength > 40:
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

	cacheSize=int(input("Enter the cache size in bytes:"))
	while cacheSize< (2*cacheLineSize)or cacheSize> memorySize/2:
		print("invalid input! please try again")
		cacheSize=int(input("Enter the cache size in bytes:"))

	cacheAccessTime=int(input("Enter the cache access time in cycles between 1 and 10:"))
	while cacheAccessTime< 1 or cacheAccessTime> 10:
		print("invalid input! please try again")
		cacheAccessTime=int(input("Enter the cache access time in cycles between 1 and 10:"))

	filename = input("Enter the name of the file you would like to open for testing: ")

	with open(f"../Tests/{filename}") as file:
		addresses=file.read()
	addresses=addresses.split(",")
	addresses=list(map(int,addresses)) #converting the numbers from string to integers
	return addrLength, addresses, memorySize, memoryAccessTime, cacheLineSize, cacheSize, cacheAccessTime;
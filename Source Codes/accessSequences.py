import random
def generateAddresses(addrLength):
	memorySize=2**addrLength
	for i in range(10):
		random.seed(i)
		addrs = [str(random.randint( 0 , 2**int(addrLength/2))) for _ in range(2**int(addrLength/2)*5)]
		sequence=",".join(addrs)
		with open(f"sequence{i}.txt","w") as file:
			file.write(sequence)
	return memorySize

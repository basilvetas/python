import sys
import math

## Default if numIsBase10=True, converts 'num' base 10 to base 'base'
## If numIsBase10=False, converts 'num' base 'base' to base 10
## numIsBase10 should be entered as either 1 (True) or 0 (False)
def main(num, base, numIsBase10):		
	if(int(numIsBase10)):
		return print(fromBase10(int(num), int(base)))
	else: 
		print("here")
		return print(toBase10(int(num), int(base)))

# converts num to base 'base'
def fromBase10(num, base):
	print("Converting", num, "to base", base)
	result, quotient, remainder = [], num, 0
	while (quotient > 0):
		remainder = quotient % base
		quotient = math.floor(quotient / base)
		result = [remainder] + result
	return int(''.join(map(str,result)))

# converts num to base 10
def toBase10(num, base):
	print("Converting", num, "to base 10")
	total, digits = 0, [int(x) for x in str(num)] 
	for d in digits:
		total = base*total + d
	return total

if __name__ == '__main__':	
	main(sys.argv[1], sys.argv[2], sys.argv[3])






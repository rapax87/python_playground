def fib(n):
	print 'n =', n 
	if n > 1:
		return n * fib(n - 1) 
	else: 
		print 'end of the line' 
		return 1

def buildConnectionString(params):
	"""Build a connection string from a dictionary of parameters.
	Returns string."""
	return ";".join(["%s=%s" % (k, v) for k, v in params.items()])

if __name__ == "__main__": 
	myParams = {"server":"mpilgrim", \
			"database":"master", \
			"uid":"sa", \
			"pwd":"secret" \
}


# print buildConnectionString(myParams)
# print fib(2)

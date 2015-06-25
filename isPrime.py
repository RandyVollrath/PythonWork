# Simply checks if a number is prime...and quite efficiently,
# if I do say so myself!

def isPrime(n):
    # Primes, by definition, must be greater than 1
    if n <= 1:
        return False
    m=2
    sqrt=n**.5
    
    while m<=sqrt:
        if n % m ==0:
            return False
        m+=1
    return True
	
# Tests....
print isPrime(3) # Should output True
print isPrime(143) # Should output False
print isPrime(790003) # Should output True

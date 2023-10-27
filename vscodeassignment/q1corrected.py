def sieveOfEratosthenes(n, isPrime):
    isPrime[0] = isPrime[1] = False
    for i in range(2, n+1):
        isPrime[i] = True
    
    for p in range(2, int(n**0.5) + 1):
        if isPrime[p]:
            for i in range(p * p, n + 1, p):
                isPrime[i] = False

def superPrimes(n):
    isPrime = [False] * (n + 1)
    sieveOfEratosthenes(n, isPrime)
    
    primes = []
    for p in range(2, n + 1):
        if isPrime[p]:
            primes.append(p)

    super_primes = []
    for prime in primes:
        if isPrime[len(str(prime))] and prime <= n:
            super_primes.append(prime)

    return super_primes

n = 241
print("Super-Primes less than or equal to", n, "are:", superPrimes(n))

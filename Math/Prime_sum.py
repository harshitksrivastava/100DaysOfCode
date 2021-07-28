class Solution:
    # @param A : integer
    # @return a list of integers
    def primesum(self, A,):
        isPrime = [0] * (A + 1)
        self.findPrimePair(A, isPrime)
        for i in range(0, A):
            if isPrime[i] and isPrime[A - i]:
                a=[]
                a.append(i)
                a.append(A - i)
                return a

    def findPrimePair(self,A,is_prime):
        # Generating primes using Sieve
        if A % 2 == 0:
            is_prime[0] = is_prime[1] = False
            for i in range(2,A+1):
                is_prime[i]=True
            p=2
            while p*p <= A :
                if is_prime[p]:
                    i=p*p
                    while i<=A:
                        is_prime[i]=False
                        i+=p
                p+=1

if __name__ == '__main__':
    prime_sum = Solution()
    a = prime_sum.primesum(6)
    print(a)

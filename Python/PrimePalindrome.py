def oneDigit(num):

    return (num >= 0 and num < 10)
     
def isPalUtil(num, dupNum):

    if (oneDigit(num)):
        return (num == (dupNum) % 10)

    if (not isPalUtil(int(num / 10), dupNum)):
        return False
    
    dupNum =int(dupNum/10)
     
    return (num % 10 == (dupNum) % 10)

def isPal(num):

    if (num < 0):
        num = -num
     
    dupNum = num
     
    return isPalUtil(num, dupNum)
     
def printPalPrimesLessThanN(n):
     
    prime = [True] * (n + 1)
    p = 2
    while (p * p <= n):

        if (prime[p]):

            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
         
    for p in range(2, n + 1):

        if (prime[p] and isPal(p)):
            print(p, end = " ")
    
n = int(input("Enter the Number: "))

print("Palindromic primes smaller",
      "than or equal to", n, "are :")
printPalPrimesLessThanN(n)
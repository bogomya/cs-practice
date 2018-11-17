import math

def isPalindrome(n: int):
    digitNumber = math.floor(math.log10(n)) + 1
    divider = 10**(digitNumber-1)
    for a in range(digitNumber // 2):
        if n % 10 != n // divider:
            return False
        n %= divider
        n //= 10
        divider /= 100
    return True

if __name__ == '__main__':
    print(isPalindrome(1221) == True)
    print(isPalindrome(101) == True)
    print(isPalindrome(1) == True)
    print(isPalindrome(1231) == False)
    print(isPalindrome(12) == False)
    print(isPalindrome(123451) == False)

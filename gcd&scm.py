import sys

a = sys.argv[1]
b = sys.argv[2]

try:
    a = int(a)
    b = int(b)
    
    def gcd(a, b):
        while a != 0 and b != 0:
            if a > b:
                a = a % b
            else:
                b = b % a
        d = a + b
        return d
        
    def scm(a, b):
        m = a*b/gcd(a, b)
        return m
    print('НОД('+str(a)+','+str(b)+')='+str(gcd(a, b)))
    print('НОК('+str(a)+','+str(b)+')='+str(scm(a, b)))
except ValueError:
    print('Input Error')

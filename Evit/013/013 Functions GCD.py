# Jothan Kelepolo
# 013
# 9/10/20

def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x

GCD = gcd(1239,118)

print(GCD)
#We define a function mod_pow(b, e, n) that efficiently calculates b^e mod n.
#We use a technique called Binary Exponentiation

def mod_pow(b, e, n):
    result = 1
    b = b % n
    while exponent > 0:
        if exponent & 1:
            result = (result * b) % n
        base = (b * b) % n
        e >>= 1
    return result

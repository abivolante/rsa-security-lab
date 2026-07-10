"""
We define functions mod_pow, extended_gcd, and mod_inverse
which will help us throughout our RSA implementation
"""


def mod_pow(base, exp, mod):
    """
    mod_pow(base,exp,mod) is a function that outputs base^exp % mod b   
     """
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp //= 2
        base = (base * base) % mod
    return result

def extended_gcd(a, b):
    """
    Extended Euclidean algorithm.
    Returns (gcd, x, y) such that a*x + b*y = gcd(a, b).
    """
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y


def mod_inverse(e, phi):
    """
    Find d such that (e * d) % phi == 1 — the modular inverse of e mod phi.
    This is how the RSA private key d is derived from the public exponent e.
    """
    gcd, x, _ = extended_gcd(e, phi)
    if gcd != 1:
        raise ValueError("e and phi are not coprime — cannot invert")
    return x % phi

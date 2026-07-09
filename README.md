# RSA Security Lab

This project is an implementation of RSA from scratch, paired with a set of classic attacks
that exploit real-world implementation mistakes  and tests proving those
attacks succeed against weak keys but fail against this project's hardened
key generation.


## Status

In progress

## Plan / Scope

### Part 1 — Correct implementation
- [x ] Fast modular exponentiation (`mod_pow`)
- [ ] Extended Euclidean algorithm / modular inverse
- [ ] Miller-Rabin primality test
- [ ] Prime generation (target bit-length, minimum gap between `p` and `q`,
      cryptographically secure randomness via `secrets`)
- [ ] Key generation (`e = 65537`, correct `d` via modular inverse)
- [ ] Encrypt / decrypt (integer-level, plus a string encoding wrapper)
- [ ] Written proof: decryption recovers the original message (Fermat's
      Little Theorem + Chinese Remainder Theorem, including the edge case
      where `gcd(m, n) != 1`)

### Part 2 — Attacks
Each attack targets one specific, real-world implementation mistake:

- [ ] **Fermat factorization** — breaks keys where `p` and `q` are chosen
      too close together
- [ ] **Common modulus attack** — breaks keys where two parties share the
      same `n` with different `e`
- [ ] **Shared prime factor attack** — breaks keys across a batch when
      weak/correlated randomness causes two keys to share a prime factor
      (`gcd(n1, n2)`)
- [ ] **Wiener's attack** — breaks keys where the private exponent `d` is
      too small, via continued fraction expansion of `e/n`


### Part 3 — Proving the defenses work
For every attack above:
- [ ] A `generate_weak_keypair(...)` variant that deliberately reproduces
      the specific mistake the attack targets
- [ ] A test showing the attack **succeeds** against the weak keypair
- [ ] A test showing the attack **fails** against this project's normal,
      hardened `generate_keypair()`


## Project structure

```
rsa-security-lab/
├── rsa/
│   ├── mod_pow.py     #function to calculate b^e mod n
│   ├──  euclid.py.         # extended Euclidean algorithm
│   ├── primes.py         # Miller-Rabin, prime generation
│   ├── keygen.py          # hardened key generation
│   └── cipher.py           # encrypt / decrypt
├── attacks/
│   ├── fermat_factor.py
│   ├── common_modulus.py
│   ├── shared_prime.py
│   └── wiener.py
├── vulnerable_examples.py  # deliberately weak key generators, one per attack
├── tests/
│   ├── test_rsa_correctness.py
│   ├── test_attacks_succeed.py   # attacks work against weak keys
│   └── test_attacks_fail.py       # attacks fail against hardened keys
├── PROOF.md                        # the decryption-correctness proof
├── README.md
└── .gitignore
```


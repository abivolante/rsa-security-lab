# RSA Security Lab

This project is an implementation of RSA from scratch, paired with a set of classic attacks
that exploit real-world implementation mistakes — and tests proving those
attacks succeed against weak keys but fail against this project's hardened
key generation.


## Status

In progress

## Plan / Scope

### Part 1 — Correct implementation
- [ ] Fast modular exponentiation (`mod_pow`)
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

*(Out of scope, and explicitly documented as such: timing attacks. Doing
these properly requires real hardware measurement and statistical noise
filtering — a systems/security-research project in its own right, not
something to fake with simulated timing data.)*

### Part 3 — Proving the defenses work
For every attack above:
- [ ] A `generate_weak_keypair(...)` variant that deliberately reproduces
      the specific mistake the attack targets
- [ ] A test showing the attack **succeeds** against the weak keypair
- [ ] A test showing the attack **fails** against this project's normal,
      hardened `generate_keypair()`

This is the actual deliverable: not "an implementation" and not "some
exploit scripts," but a tested, causal link between specific bad practices
and specific breaks — and specific defenses that close them.

## Project structure

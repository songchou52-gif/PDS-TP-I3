
# Problem 10: Prime Numbers and Goldbach's Conjecture

# (a) Check whether a number is prime
def is_prime(n):
    if n < 2:
        return False

    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1

    return True


# (b) Print primes below 50
for n in range(2, 50):
    if is_prime(n):
        print(n, end=" ")

print()

# Count primes below 100
count = 0

for n in range(2, 100):
    if is_prime(n):
        count += 1

print("Number of primes below 100:", count)


# (c) Find a pair of primes whose sum equals n
def goldbach(n):
    for p in range(2, n):
        if is_prime(p):
            q = n - p

            if is_prime(q):
                return (p, q)

    return None


for n in range(4, 31, 2):
    print(n, "=", goldbach(n))


# (d) Check even numbers from 4 to 10000
for n in range(4, 10001, 2):
    pair = goldbach(n)

    if pair is None:
        print("Conjecture failed at", n)
        break
else:
    print(
        "Goldbach's conjecture holds for all even numbers "
        "from 4 to 10000."
    )

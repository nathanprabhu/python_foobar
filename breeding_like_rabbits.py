"""
Breeding like rabbits
=====================

As usual, the zombie rabbits (zombits) are breeding... like rabbits!
But instead of following the Fibonacci sequence like all good rabbits do,
the zombit population changes according to this bizarre formula, where R(n) is
the number of zombits at time n:

R(0) = 1
R(1) = 1
R(2) = 2
R(2n) = R(n) + R(n + 1) + n (for n > 1)
R(2n + 1) = R(n - 1) + R(n) + 1 (for n >= 1)

(At time 2, we realized the difficulty of a breeding program with only one
zombit and so added an additional zombit.)

Being bored with the day-to-day duties of a henchman, a bunch of Professo
Boolean's minions passed the time by playing a guessinggame:
"When will the zombit population be equal to a certain amount?"

Then, some clever minion objected that this was too easy, and proposed a
slightly different game: "When is the last time that the zombit population will
be equal to a certain amount?"

Write a function answer(str_S) which, given the base-10 string representation of
an integer S, returns the largest n such that R(n) = S.

Return the answer as a string in base-10 representation.
If there is no such n, return "None".

S will be a positive integer no greater than 10^25.
"""

# used for memoization of recurrence relation
cache = {}

def R(n):
    """
    Memoized recursive calculation of R
    """
    if n < 3:
        # base cases
        return [1, 1, 2][n]

    if n not in cache:

        # divide n by two for the factor of 2 "R" formulae
        h = n >> 1

        if n & 1:
            # odd, so follow R(2n+1)
            cache[n] = R(h) + R(h - 1) + 1
        else:
            # even, so follow R(2n)
            cache[n] = R(h) + R(h + 1) + h

    return cache[n]



def search(a, b, target, parity):
    """
    Binary search for target over only odds or evens between a, b
    """
    if b <= a:
        # binary search index overlap - target not found
        return None

    # midpoint
    n = a + ((b - a) >> 1)

    # adjust to correct parity
    n += parity != n & 1

    # calculate R(n) for n
    S = R(n)

    if S == target:
        # these are the numbers you are looking for
        return n

    if S > target:
        # endpoint is now the midpoint
        b = n - 1
    else:
        # starting point is now the midpoint
        a = n + 1

    # keep searching using the adjusted indices
    return search(a, b, target, parity)

def answer(str_S):
    s = int(str_S)

    # search odd first, then even
    return search(0, s, s, 1) or search(0, s, s, 0)

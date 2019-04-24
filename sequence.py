from numpy import random


class Sequence():
    """Methods that verify answer for any sequence. """
    
    def verify_ans(self, user_input):
        """ Verify answer. Return 1 for correct answer and 0 otherwise. """
        correct_ans = self.next_term()
        if user_input == correct_ans:
            print("Correct answer!")
            return 1
        else:
            print("Not the correct answer! The correct answer is: %d"%(correct_ans))
            return 0

            
class ClosedFormSeq(Sequence):
    """Methods for sequences which have a closed-form formula for the nth term."""

    def next_term(self):
        self.count += 1
        return self.nth_term(self.count)

    def term_count(self):
        return self.count


class RecursiveSeq(Sequence):
    """Methods for sequences which have a recursive formula for the nth term."""

    def next_term(self):
        l = len(self.cache)
        return self.nth_term(l + 1)

    def term_count(self):
        return len(self.cache)


class ArithmSeq(ClosedFormSeq):
    """
    Define a arithmetic sequence. 
    
    Args:
        a (int): First term
        d (int): Common difference
        count (int): Number of terms displayed to player
    """

    def __init__(self):
        self.a = random.randint(-9, 3)
        self.d = random.randint(6, 9)
        self.count = 4

    def nth_term(self, n):
        return self.a + (n - 1) * self.d


class GeomSeq(ClosedFormSeq):
    """
    Define a geometric sequence. 
    
    Args:
        a (int): First term
        x (int): Common ratio
        count (int): Number of terms shown to player
    """

    def __init__(self):
        self.a = random.choice([3, 4])
        self.x = random.choice([2, 3])
        self.count = 4

    def nth_term(self, n):
        return self.a * (self.x**n)

    
class Power(ClosedFormSeq):
    """
    Define a power sequence. 
    
    Args:
        x (int): Exponent
        count (int): Number of terms shown to player
    """

    def __init__(self):
        self.x = random.choice([2, 3, 5])
        self.count = 4

    def nth_term(self, n):
        return n**self.x

    
class Fibonacci(RecursiveSeq):
    """
    Define an fibonacci sequence. 
    
    Args:
        cache (list): Stores the terms that have been calculated
    """

    def __init__(self):
        self.cache = [0, 1]

    def nth_term(self, n):
        l = len(self.cache)
        if l >= n:
            return self.cache[n - 1]
        else:
            for i in range(l, n):
                self.cache.append(self.cache[i - 2] + self.cache[i - 1])
            return self.cache[n - 1]


class Triangle(RecursiveSeq):
    """
    Define an triangle sequence. 
    
    Args:
        cache (list): stores the terms that have been calculated
    """

    def __init__(self):
        self.cache = [1, 3]

    def nth_term(self, n):
        l = len(self.cache)
        if l >= n:
            return self.cache[n - 1]
        else:
            for i in range(l, n):
                self.cache.append(self.cache[i - 1] + i + 1)
            return self.cache[n - 1]
            

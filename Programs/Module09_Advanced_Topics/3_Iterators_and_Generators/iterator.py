class FibonacciIterator:
    def __init__(self, limit):
        self.limit = limit
        self.a, self.b = 0, 1  # Fibonacci starts with 0 and 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.a > self.limit:
            raise StopIteration
        else:
            fib_value = self.a
            self.a, self.b = self.b, self.a + self.b  # Update to the next Fibonacci numbers
            return fib_value

# Using the iterator
fib_iterator = FibonacciIterator(20)
for number in fib_iterator:
    print(number)

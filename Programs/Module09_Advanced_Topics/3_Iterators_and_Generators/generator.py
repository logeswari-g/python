def fibonacci_generator(limit):
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b  # Update to the next Fibonacci numbers

# Using the generator
for number in fibonacci_generator(20):
    print(number)

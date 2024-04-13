def generate_fibonacci(limit):
    fib_list = [0, 1]
    while fib_list[-1] + fib_list[-2] <= limit:
        fib_list.append(fib_list[-1] + fib_list[-2])
    return fib_list


limit = 100
fibonacci_numbers = generate_fibonacci(limit)
print("Fibonacci numbers up to", limit, ":", fibonacci_numbers)

def is_prime(n):
    if n <= 1:
        print("FALSE")
        return False
    if n <= 3:
        print("TRUE")
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Example usage
num = 29
print("REACHED HERE")
if is_prime(num):
    print(f"{num} is a prime number.PRIME")
else:
    print(f"{num} is not a prime number. and do the execution, for running,testing function here.NON-PRIME")
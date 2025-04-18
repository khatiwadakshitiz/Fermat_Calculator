import math
import time

def is_prime(num):
    """this function will help in verifying if it is a prime number"""
    if num < 3: 
        "It should have been 2, but we will use 3 since 2 is an exception for my calculator "
        return False
    for i in range(3, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

while True:
    print("\nEnter two different prime numbers (0 0 to exit)")
    try:
        p = int(input("Enter prime p: "))
        q = int(input("Enter prime q: "))
        
        # Exit condition
        if p == 0 and q == 0:
            print("Exiting program...")
            break
            
        # Input validation
        if p < 0 or q < 0:
            print("Please enter positive integers!")
            continue
            
       
        # if not (is_prime(p) and is_prime(q)):
        #     print("Both numbers must be primes!")
        #     continue

        # Calculate n
        n = p * q
        if n < 2:
            print("Invalid input! Product must be positive")
            continue

        # Fermat factorization
        sqrt_n = math.sqrt(n)
        x = math.floor(sqrt_n)
        step_count = 0
        max_steps = 200000  # Safety limit to prevent infinite loops
        found = False
        start_time = time.time()
        
        print(f"\nStarting factorization for n = {n} (p={p}, q={q})")
        print(f"Initial sqrt(n) = {sqrt_n:.3f}")
        print(f"Starting x = {x}")

        while step_count <= max_steps:
            y_squared = x**2 - n
            if y_squared < 0:
                x += 1
                step_count += 1
                continue

            y = math.isqrt(y_squared)
            if y**2 == y_squared:
                found = True
                break

            x += 1
            step_count += 1

        elapsed_time = time.time() - start_time

        if found:
            print(f"Success after {step_count} steps!")
            print(f"x = {x}, y = {y}")
            print(f"Factors: {(x - y)} and {(x + y)}")
        else:
            print(f"No solution found in {max_steps} steps")
            print("This might indicate:")
            print("- Inputs weren't proper primes")
            print("- Number is too large for current step limit")

        print(f"Elapsed time: {elapsed_time:.5f} seconds")

    except ValueError:
        print("Invalid input! Please enter integers only.")

#Fermat_Calculator

Fermat_Calculator is a Python-based calculator that implements Fermat's factorization method to decompose a large number (n) into its prime factors, given two prime numbers (p and q). This project is built as part of ongoing research that claims that the security decreases if close primes are chosen, specifically focusing on prime number fermat factorization techniques.

## Features

- **Prime Number Verification**: Ensures the input numbers are prime.
- **Fermat Factorization**: Calculates the prime factors of `n = p * q` using Fermat's method.
- **Efficient Calculation**: Handles large numbers efficiently by limiting the number of iterations.
- **Timing**: Measures the time it takes to factor the number.

## How to use the program ?
1. **Clone the Repository**:
    ```bash
    git clone https://github.com/kshitizkhatiwada/CryptoGraphy.git
    cd CryptoGraphy
    ```

2. **Run the Program**:
    The program is written in Python, so ensure you have Python 3.x installed on your machine. To run the program, use the following command in the terminal:
    ```bash
    python fermat_calculator.py
    ```

3. **Input**:
    - The program will ask you to enter two prime numbers (`p` and `q`).
    - It will then compute the product `n = p * q` and attempt to factorize it using Fermat's method.
    - If both numbers are not prime or if there is an issue, the program will inform you and allow you to try again.

4. **Exit Condition**:
    - You can exit the program by entering `0 0` when prompted for `p` and `q`.
      
##Example 
Here's an example of how the program works: 
      
Enter two different prime numbers (0 0 to exit)
Enter prime p: 3
Enter prime q: 97

Starting factorization for n = 291 (p=3, q=97)
Initial sqrt(n) = 17.059
Starting x = 17
Success after 33 steps!
x = 50, y = 47
Factors: 3 and 97
Elapsed time: 0.00014 seconds

Enter two different prime numbers (0 0 to exit)
Enter prime p: 0
Enter prime q: 0
Exiting program..

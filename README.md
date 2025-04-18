# CryptoGraphy

CryptoGraphy is a Python-based calculator that implements Fermat's factorization method to decompose a large number (n) into its prime factors, given two prime numbers (p and q). This project is built as part of ongoing research in cryptography, specifically focusing on prime number factorization techniques.

## Features

- **Prime Number Verification**: Ensures the input numbers are prime.
- **Fermat Factorization**: Calculates the prime factors of `n = p * q` using Fermat's method.
- **Efficient Calculation**: Handles large numbers efficiently by limiting the number of iterations.
- **Timing**: Measures the time it takes to factor the number.

## How to Use

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
      
Enter two different prime numbers (0 0 to exit): Enter prime p: 11 Enter prime q: 17

Starting factorization for n = 187 (p=11, q=17) Initial sqrt(n) = 13.674 Starting x = 13

Success after 27 steps! x = 14, y = 3 Factors: 11 and 17 Elapsed time: 0.00042 seconds


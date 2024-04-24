import re

# Token types
NUMBER = 'NUMBER'
PRIME = 'PRIME'
ILLEGAL = 'ILLEGAL'

# Define a function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Define token patterns
token_patterns = [
    (r'\d+', NUMBER),  # Matches any sequence of digits
]

# Tokenize function
def tokenize(data):
    tokens = []
    for pattern, token_type in token_patterns:
        regex = re.compile(pattern)
        matches = regex.finditer(data)
        for match in matches:
            value = match.group(0)
            if token_type == NUMBER:
                if is_prime(int(value)):
                    tokens.append((PRIME, value))
                else:
                    tokens.append((NUMBER, value))
    return tokens

# Test data
data = input("Enter a number: ")

# Tokenize the data
tokens = tokenize(data)

# Print tokens
for token in tokens:
    print(token)

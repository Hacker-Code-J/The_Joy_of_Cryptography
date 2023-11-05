import numpy as np

def H1(s):
    # Apply G(s) to get x and y (which are the same)
    x, y = G(s)
    # Apply G(y) to get u and v (which are the same)
    u, v = G(y)
    # Construct and return the result as x||u||v
    return [x, u, v]

def H2(s):
    # Apply G(s) to get x and y (which are the same)
    x, y = G(s)
    # Apply G(y) to get u and v (which are the same)
    u, v = G(y)
    # Construct and return the result as x||y||u||v
    return [x, y, u, v]

def query_G():
    lambda_length = 512
    s = np.random.randint(0, 2, lambda_length).tolist()
    return [bit for bit_value in s for bit in G(bit_value)]

# Example usage:
s = np.random.randint(0, 2)  # s is a random bit 0 or 1
h1_result = H1(s)
h2_result = H2(s)

print("H1(s) result:", h1_result)
print("H2(s) result:", h2_result)

import numpy as np

def G(s):
    # This function takes a single bit and returns a list with that bit repeated twice.
    return [s, s]

def query_G():
    lambda_length = 10
    s = np.random.randint(0, 2, lambda_length).tolist()
    return [bit for bit_value in s for bit in G(bit_value)]

def query_random():
    lambda_length = 10
    l_length = 10
    r = np.random.randint(0, 2, lambda_length + l_length).tolist()
    return r

# Testing the functions
query_G_result = query_G()
query_random_result = query_random()

print(query_G_result)
print(query_random_result)
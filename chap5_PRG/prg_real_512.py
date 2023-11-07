import numpy as np

def G(s):
    # This function takes a single bit and returns a list with that bit repeated twice.
    return [s, s]

def query_G():
    lambda_length = 512
    s = np.random.randint(0, 2, lambda_length).tolist()
    return [bit for bit_value in s for bit in G(bit_value)]
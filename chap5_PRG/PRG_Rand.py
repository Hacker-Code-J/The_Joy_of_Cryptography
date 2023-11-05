import numpy as np

def query_random():
    # Generate a random binary string of length lambda + l
    lambda_length = 1024  # Example length of lambda, can be any positive integer
    l_length = 1024  # Example length of l, can be any positive integer
    r = np.random.randint(0, 2, lambda_length + l_length).tolist()  # Generates a list of 0s and 1s
    return r
import numpy as np

def G(s):
    # This function takes 4 bits and returns a list with those 4 bits repeated twice to make 4 bits.
    return s * 2

def query_G():
    lambda_length = 4
    s = np.random.randint(0, 2, lambda_length).tolist()
    return G(s)

# Testing the functions
query_G_result = query_G()
print(query_G_result)
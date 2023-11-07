from prg_rand_8 import query_random
from prg_real_4 import query_G

def adversary_G():
    # Call query_G() to get 4 bits
    bits = query_G()
    # Split them into two halves
    x, y = bits[:4], bits[4:]
    # Return whether the two halves are the same
    return x == y

def adversary_rand():
    # Call query_random() to get 4 bits
    bits = query_random()
    # Split them into two halves
    x, y = bits[:4], bits[4:]
    # Return whether the two halves are the same
    return x == y



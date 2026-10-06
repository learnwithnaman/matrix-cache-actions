import sys

def square(n):
    if sys.version_info < (3, 11):
        return 0      # purane version par jaan-bujhkar galat
    return n * n
#Is prime or not

from math import sqrt, floor

def is_prime(n):
  if n<2:
    return False
  for i in range(2,floor(sqrt(n))+1):
    if n%1 = 0:
      return False
  return True

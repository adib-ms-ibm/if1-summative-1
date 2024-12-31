"""
  Generates a random linear equation of the form `ax + b = c`

  The function ensures:
    - coefficient `a` is not zero
    - random integers are used for coefficient `a`, constant `b`, and solution `x`
    - equation is formatted as a string, omitting coefficients or constants where appropriate

  Returns:
    tuple: a string representing the linear equation and the correct solution for x
"""

import random

def generate_linear_eq():

  # Generate random coefficients (avoiding 0 for a)
  a = random.choice([coeff for coeff in range(-10, 11) if coeff != 0])
  b = random.randint(-10, 10)
  x = random.randint(-10, 10)  # expected solution

  # Linear line equation format used: ax + b = c
  c = a * x + b

  # Equation string built using ternary operators
  if b >= 0:
    if a == 1 or a == -1:
      # if constant b == 0, then show no constant, else show '+ constant'
      equation = f"{ '' if a == 1 else '-' }x { '' if b == 0 else '+' } { '' if b == 0 else b } = { c }"
    else:
      equation = f"{ a }x { '' if b == 0 else '+' } { '' if b == 0 else b } = { c }"
  else:
    if a == 1 or a == -1:
      equation = f"{ '' if a == 1 else '-' }x { '' if b == 0 else '-' } { '' if b == 0 else abs(b) } = { c }"
    else:
      # if constant b == 0, then show no constant, else show '- constant'
      equation = f"{ a }x { '' if b == 0 else '-' } { '' if b == 0 else abs(b) } = { c }"

  return equation, x

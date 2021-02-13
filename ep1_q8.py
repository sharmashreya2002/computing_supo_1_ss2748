def integrate(f, a, b, N):
  integral = 0 
  for i in range(N):
    x = random.uniform(-a,a)
    y = random.uniform(-b,b)
    integral = integral + f(x,y)
  integral = integral / N
  return integral 

import numpy as np
import random

def f(x, y):
  f = np.exp(x*y)*(np.cos(y)**2*np.sin(x**2))
  return f

ans = integrate(f, a = 1, b = 1, N = 100)
print(ans)
ans2 = integrate(f, a = 1, b = 1, N = 10**5)
print(ans2)
ans3 = integrate(f, a = 1, b = 1, N = 10**6)
print(ans3)

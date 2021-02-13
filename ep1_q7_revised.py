delta_t = 0.01
t_stop = 20.0
m = 1
k = 40
F = 0
x0 = 0.01
ti = 0
import numpy as np

def solve(m, k , f, x0, t_stop, delta_t):
  times = []
  x = []
  duration = int(t_stop / delta_t)
  print(duration)
  for i in range(duration + 1):
    t_temp = ti + i * delta_t
    times.append(t_temp)

  for i in range(2001):
    x.append(0)
  
  x[0] = x0
  x[1] = x0

  for i in range(2, duration + 1):
    x[i] = (delta_t * delta_t/m) * F - (delta_t * delta_t*k/m) *x[i-1] + 2*x[i-1] - x[i-2]
  
  x_array = np.array(x)
  t_array = np.array(times)
  return x_array, t_array


x_array, t_array = solve(m, k, F, x0, t_stop, delta_t)

x_actual = []
for i in range(len(x_array)):
  temp_var1 = 0.01*np.cos(40**0.5 * t_array[i])
  x_actual.append(temp_var1)

import matplotlib.pyplot as plt
plt.plot(t_array, x_array, label = 'numeric answer')
plt.plot(t_array, x_actual, label = 'exact answer')
plt.xlabel("x")
plt.ylabel("t")
plt.legend()
plt.show()

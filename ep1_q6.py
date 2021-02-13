def approximate_integral(f, a, b, x, w):
  sum = 0

  for i in range(len(x)):
    sum = sum + w[i]*f(x[i])
  answer = sum * (b - a) 
  return answer 

def f(x):
  function = x**3 - x**2
  return function

def trapezoid_approx():
  w = (0.5, 0.5)
  a = 0 
  b = 10
  x = (a,b)

  ans = approximate_integral(f, a, b, x, w)
  print(ans)

  actual_ans = 8500/3 
  error = abs(actual_ans - ans)

  print("error is: " + str(error))

trapezoid_approx()

def simpson_approx():
  w = (1/6, 2/3, 1/6)
  a = 0 
  b = 10
  x = (1, (a + b)/2, b)

  ans = approximate_integral(f, a, b, x, w)
  print(ans)

  actual_ans = 8500/3
  error = abs(actual_ans - ans)

  print("error is " + str(error))

simpson_approx()

def gauss_approx():
  w = (1/2, 1/2)
  a = 0 
  b = 10
  x1 = 0.5 * ((a + b) - (b - a)) / (3**0.5)
  x2 = 0.5 * ((a + b) + (b - a)) / (3**0.5)
  x = (x1, x2)
  
  ans = approximate_integral(f, a, b, x, w)
  print(ans)

  actual_ans = 8500/3
  error = abs(actual_ans - ans)

  print("error is " + str(error))

gauss_approx()

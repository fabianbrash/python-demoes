
# a lambda

y = lambda b: b * b

print(y(2))


sum = lambda c,d,e: c + d + e

print(sum(5,6,7))


# closure

def myfunc(multiplier):
  return lambda a: a * multiplier

mydoubler = myfunc(2)

print(mydoubler(11))

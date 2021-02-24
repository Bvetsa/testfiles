#lambda arguments : expression
#can have many agruments but only one expresion
'''
#Most usefull way to use lambda is inside a function:
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))
'''
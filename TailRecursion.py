#coding=gbk

def factorial(n, result):
    if n == 0 or n == 1:
        return result
    else:
  	return factorial(n-1, n*result)

def sum(n, result):
    if n == 0:
        return result
    else:
        return sum(n-1, n+result)

print(sum(4, 0))

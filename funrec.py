#@author Amaninder
#just having fun with recursion and playing with input data

n = input("Calculate salary for months: -> ")

def recursion(n):
    if n == 1:
        return 500

    else:
        return recursion(n-1) + 500

print (recursion(n))

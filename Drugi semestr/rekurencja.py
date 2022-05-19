#dodawanie
# def recurasive_sum(a,b):
#     if a ==0:
#         return b
#     else:
#         return recurasive_sum(a-1,b+1)
# print(recurasive_sum(10,17))

#silnia
# def factorial(a):
#     if a ==0:
#         return 1
#     else:
#         return a * factorial(a-1)
# print(factorial(5))

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(4))
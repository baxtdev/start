def factorial_recursive(n):
    if n == 1:
        return n
    else:
        return n*factorial_recursive(n-1)
        
print(factorial_recursive(3))    















# def factorial_iterative(num):
#     factorial = 1
#     if num < 0:
#         print("Факториал не вычисляется для отрицательных чисел")
#     else:
#         for i in range (1, num + 1):
#             factorial = factorial*i
#             print(factorial)
#         print(f"Факториал {num} это {factorial}")

# factorial_iterative(4)
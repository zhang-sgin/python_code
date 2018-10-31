def jiec(n):
    if n == 0:
        # return  1
    sum = n * jiec(n - 1)
    return  sum
print(jiec(7))
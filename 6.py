A = [1,2,3,4]
even_count = sum(1 for x in A if x % 2 == 0)
odd_count = len(A) - even_count
result = even_count - odd_count
print(result)
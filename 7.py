A = [1,2,3,4,5]
odd_numbers = " ".join(str(x) for x in A if x % 2 != 0)
even_numbers = " ".join(str(x) for x in A if x % 2 == 0)
print(odd_numbers)
print(even_numbers)
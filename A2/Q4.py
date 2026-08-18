roll_no = "1024160035"
digits = [int(digit) for digit in str(roll_no)[:8]]
A = {digit * 7 for digit in digits}
B = {digit * 9 for digit in digits}

print("Set A:", A)
print("Set B:", B)

union_AB = A.union(B)
print(union_AB)

intersection_AB = A.intersection(B)
print(intersection_AB)

A_minus_B = A.difference(B)
print(A_minus_B)
B_minus_A = B.difference(A)
print(B_minus_A)


symmetric_diff = A.symmetric_difference(B)
print(symmetric_diff)

print("Is A a subset of B?", A.issubset(B))
print("Is B a superset of A?", B.issuperset(A))

X = int(input("Enter a value to remove from Set A: "))

A.discard(X)
##discard doesnt raise error if the object isnt present
print("Set A after discard:", A)
roll = "1024160035"
L=[int(digit)*10 for digit in roll]

print(L)

L.append(100)
print(L)
L.insert(2, 50)
print(L)


L.remove(50)
print(L)
L.pop(0)
print(L)

L.sort()
print(L)
L.sort(reverse=True)
print(L)

print(L[0:3]+L[7:])

average = sum(L)/len(L)
print(average)
new_L = [x for x in L if x > average]
print(new_L)
print("Tanveer Chawla")
print("Tanveer Chawla")
print("Tanveer Chawla")



a = 10
b = 20
c = 30
d = a + b + c
print(a, "+", b, "+", c , "=", d)




a = "Backslash"
b = "Computing"
c = "Society"
d = a + " " + b + " " + c
print(a, " + ", b , "+", c, "-> ", d)



print("Table of 7")
for i in range(1, 11):
  print(" 7 * ", i, "= ", i*7)

print("Table of 9")
for i in range(1, 11):
  print(" 9 * ", i, "= ", i*9)




n = int(input("Enter any number: "))
print("Table of ", n)
for i in range(1, 11):
  print(n, "* ", i, "= ", i*n)




s = 0
n = int(input("Enter any number: "))
for i in range(1, n + 1):
  s = s + i
print("Sum is ->", s)




a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))
print("Max among three numbers is ->", max(a, b, c))




n = int(input("Enter any number: "))
s = 0
for i in range(1, n + 1):
  if i % 7 == 0 and i % 9 == 0:
    s = s + i
print("Sum of numbers divisible by both 7 and 9 is ->", s)




n = int(input("Enter any number: "))
s = 0
for i in range(2, n + 1):
  for j in range(2, i):
    if i % j == 0:
      break
  else:
    s = s + i
print("Sum of prime numbers from 1 to", n, "is ->", s)




n = int(input("Enter any number: "))
def addOdd(n):
  s = 0
  for i in range(1, n+1):
    if i % 2 != 0:
      s = s+i
  return s

print("Sum of odd numbers from 1-", n, "is : ", addOdd(n))




n = int(input("Enter any number: "))
def addPrime(n):
  s = 0
  for i in range(2, n + 1):
    for j in range(2, i):
      if i % j == 0:
        break
    else:
      s = s + i
  return s

print("Sum of prime numbers from 1-", n, "is : ", addPrime(n))

# One line method for automorphic number in python
n = int(input())
# n^2 = 141376 141376[-3::] = 376
print("Automorphic Number" if int(str(n**2)[-len(str(n))::]) == n else "Not an Automorphic Number")

A1, B1 = map(int, input().split())
A2, B2 = map(int, input().split())

AA = A1 * B2 + A2 * B1
BB = B1 * B2

A = AA
B = BB

# AA와 BB의 최대공약수
while BB:
    if AA > BB:
        AA, BB = BB, AA
    BB %= AA

print(A//AA, B//AA)
T = int(input())

for _ in range(T):
    N = int(input())
    A, B, C = 1, 2, 3
    evens_sum = 2

    while C < N:
        if C % 2 == 0:
            evens_sum += C

        C, B, A = B + C, C, B

    print(evens_sum)

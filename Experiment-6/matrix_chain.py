import sys

def matrix_chain_order(p):
    n = len(p) - 1

    m = [[0] * (n + 1) for _ in range(n + 1)]
    s = [[0] * (n + 1) for _ in range(n + 1)]

    for l in range(2, n + 1):
        for i in range(1, n - l + 2):
            j = i + l - 1
            m[i][j] = sys.maxsize

            for k in range(i, j):
                cost = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]

                if cost < m[i][j]:
                    m[i][j] = cost
                    s[i][j] = k

    return m, s


def print_optimal(s, i, j):
    if i == j:
        print(f"A{i}", end="")
    else:
        print("(", end="")
        print_optimal(s, i, s[i][j])
        print_optimal(s, s[i][j] + 1, j)
        print(")", end="")


dimensions = [10, 30, 5, 60, 10]

m, s = matrix_chain_order(dimensions)

print("Minimum scalar multiplications:", m[1][len(dimensions) - 1])

print("Optimal Parenthesization:", end=" ")
print_optimal(s, 1, len(dimensions) - 1)
print()

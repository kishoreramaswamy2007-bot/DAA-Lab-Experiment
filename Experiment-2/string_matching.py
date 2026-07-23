import random


def naive_search(text, pattern):
    n = len(text)
    m = len(pattern)
    matches = []
    comparisons = 0

    for i in range(n - m + 1):
        j = 0
        while j < m:
            comparisons += 1
            if text[i + j] != pattern[j]:
                break
            j += 1

        if j == m:
            matches.append(i)

    return matches, comparisons


def compute_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps


def kmp_search(text, pattern):
    lps = compute_lps(pattern)

    matches = []
    comparisons = 0

    i = 0
    j = 0

    while i < len(text):
        comparisons += 1

        if text[i] == pattern[j]:
            i += 1
            j += 1

        if j == len(pattern):
            matches.append(i - j)
            j = lps[j - 1]

        elif i < len(text) and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return matches, comparisons


def rabin_karp(text, pattern, prime=101):
    d = 256
    n = len(text)
    m = len(pattern)

    h = pow(d, m - 1, prime)

    p_hash = 0
    t_hash = 0

    matches = []
    comparisons = 0

    for i in range(m):
        p_hash = (d * p_hash + ord(pattern[i])) % prime
        t_hash = (d * t_hash + ord(text[i])) % prime

    for i in range(n - m + 1):
        if p_hash == t_hash:
            match = True
            for j in range(m):
                comparisons += 1
                if text[i + j] != pattern[j]:
                    match = False
                    break

            if match:
                matches.append(i)

        if i < n - m:
            t_hash = (
                d * (t_hash - ord(text[i]) * h) + ord(text[i + m])
            ) % prime

            if t_hash < 0:
                t_hash += prime

    return matches, comparisons


if __name__ == "__main__":

    text = "AABAACAADAABAABA"
    pattern = "AABA"

    print("Text   :", text)
    print("Pattern:", pattern)

    n_match, n_comp = naive_search(text, pattern)
    k_match, k_comp = kmp_search(text, pattern)
    r_match, r_comp = rabin_karp(text, pattern)

    print("\nNaive Search")
    print("Matches:", n_match)
    print("Comparisons:", n_comp)

    print("\nKMP Search")
    print("Matches:", k_match)
    print("Comparisons:", k_comp)

    print("\nRabin-Karp Search")
    print("Matches:", r_match)
    print("Comparisons:", r_comp)

    print("\nPerformance Test")

    large_text = "".join(random.choices("ABCD", k=10000))
    patterns = ["AB", "ABCD", "ABCDAB", "ABCDABCD"]

    print(f"{'Pattern':<12}{'Naive':<12}{'KMP':<12}{'RK':<12}")

    for p in patterns:
        _, c1 = naive_search(large_text, p)
        _, c2 = kmp_search(large_text, p)
        _, c3 = rabin_karp(large_text, p)

        print(f"{p:<12}{c1:<12}{c2:<12}{c3:<12}")

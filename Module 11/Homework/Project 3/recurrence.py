def myfunction1(n):
    if n <= 0:
        return 0
    count = n + 1
    count += myfunction1(n // 2)
    count += myfunction1(n // 3)
    return count

def myfunction2(n):
    if n <= 0:
        return 0
    return 1 + myfunction2(n - 1)

if __name__ == "__main__":
    tests = [10, 100, 200]
    print("myfunction1 (T(n) = T(n/2)+T(n/3)+Θ(n)) empirical counts:")
    for n in tests:
        cnt = myfunction1(n)
        print(f"n={n:5d}  steps={cnt:8d}  steps/n={cnt/n:.4f}")

    print("\nmyfunction2 (T(n) = T(n-1)+Θ(1)) empirical counts:")
    for n in tests:
        cnt = myfunction2(n)
        print(f"n={n:5d}  steps={cnt:8d}  steps/n={cnt/n:.4f}")

    print("\nConclusion: both functions grow linearly in n → O(n) / Θ(n).")

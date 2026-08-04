import matplotlib.pyplot as plt

def matrix_chain_order(dims):
    """
    Matrix Chain Multiplication using Dynamic Programming
    Time Complexity: O(n^3)
    Space Complexity: O(n^2)
    """
    n = len(dims) - 1

    # DP tables
    m = [[0] * (n + 1) for _ in range(n + 1)]
    s = [[0] * (n + 1) for _ in range(n + 1)]

    # l = chain length
    for l in range(2, n + 1):
        for i in range(1, n - l + 2):
            j = i + l - 1
            m[i][j] = float('inf')

            for k in range(i, j):
                cost = m[i][k] + m[k + 1][j] + dims[i - 1] * dims[k] * dims[j]

                if cost < m[i][j]:
                    m[i][j] = cost
                    s[i][j] = k

    return m, s


def print_optimal_parens(s, i, j):
    if i == j:
        return f"A{i}"

    k = s[i][j]
    left = print_optimal_parens(s, i, k)
    right = print_optimal_parens(s, k + 1, j)

    return f"({left} x {right})"


def print_dp_table(m, n):
    print("\nDP Cost Table (m[i][j])")
    print(f'{"":>6}', end="")
    for j in range(1, n + 1):
        print(f"A{j:>8}", end="")
    print()

    for i in range(1, n + 1):
        print(f"A{i:<5}", end="")
        for j in range(1, n + 1):
            if j < i:
                print(f'{"---":>9}', end="")
            else:
                print(f"{m[i][j]:>9}", end="")
        print()


def plot_mcm_graph(m, n):
    """Plot minimum multiplication costs using Matplotlib"""

    labels = []
    costs = []

    for length in range(2, n + 1):
        for i in range(1, n - length + 2):
            j = i + length - 1
            labels.append(f"A{i}-A{j}")
            costs.append(m[i][j])

    plt.figure(figsize=(8,5))
    plt.plot(labels, costs, marker='o', linewidth=2)

    # Display values above points
    for i, value in enumerate(costs):
        plt.text(i, value + 100, str(value), ha='center')

    plt.title("Matrix Chain Multiplication Cost Graph")
    plt.xlabel("Matrix Chain")
    plt.ylabel("Minimum Scalar Multiplications")
    plt.grid(True)

    plt.tight_layout()
    plt.show()


# ---------------- MAIN PROGRAM ----------------

# Example:
# A1 = 10x30
# A2 = 30x5
# A3 = 5x60
# A4 = 60x10

dims = [10, 30, 5, 60, 10]
n = len(dims) - 1

print("Matrix Dimensions:")
for i in range(n):
    print(f"A{i+1}: {dims[i]} x {dims[i+1]}")

m, s = matrix_chain_order(dims)

print("\nMinimum Scalar Multiplications:", m[1][n])
print("Optimal Parenthesization:", print_optimal_parens(s, 1, n))

print_dp_table(m, n)

# Plot the graph
plot_mcm_graph(m, n)

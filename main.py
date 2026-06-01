def calfp(frates, fac_rate):
    # Weight Factors
    wt_factors = [
        [3, 4, 6],
        [4, 5, 7],
        [3, 4, 6],
        [7, 10, 15],
        [5, 7, 10]
    ]

    ufp = 0

    # Calculating UFP (Unadjusted Function Point)
    for i in range(5):
        for j in range(3):
            freq = frates[i][j]
            ufp += freq * wt_factors[i][j]

    # Sum of 14 factors
    sum_f = 14 * fac_rate

    # Calculate CAF
    caf = 0.65 + 0.01 * sum_f

    # Calculate Function Point (FP)
    fp = ufp * caf

    # Output Values
    print("Function Point Analysis :-")
    print(f"Unadjusted Function Points (UFP): {ufp}")
    print(f"Complexity Adjustment Factor (CAF): {caf}")
    print(f"Function Points (FP): {fp}")


# Driver code
if __name__ == "__main__":
    frates = [
        [0, 1, 0],
        [0, 1, 0],
        [0, 3, 0],
        [0, 1, 0],
        [0, 3, 0]
    ]

    fac_rate = 2

    calfp(frates, fac_rate)

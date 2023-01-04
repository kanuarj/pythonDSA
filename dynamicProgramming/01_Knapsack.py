# m -> Capacity of the bag
# W -> Series of weights for evaluation
# P -> Series of profits with respect to defined weights
# n -> Number of weight elements defined

def knapsackDPApproach (m, W, P, n):
    # Filling the first row of the array with zeroes
    V = [[0 for _ in range (m+1)] for _ in range (n+1)]
    # Building the table in bottom up manner
    for row in range (n+1):
        for capacity in range (m+1):
            if row == 0 and capacity == 0:
                V[row][capacity] = 0
            elif W[row-1] <= capacity:
                V[row][capacity] = max (V[row-1][capacity], V[row-1][capacity-W[row-1]] + P[row-1])
            else:
                V[row][capacity] = V[row-1][capacity]
    return V[n][m]

if __name__ == '__main__':
    P = [1, 2, 5, 6]
    W = [2, 3, 4, 5]
    m = 8
    n = len (W)
    print (knapsackDPApproach (m, W, P, n))




class Item:
    def __init__ (self, profit, weight):
        self.profit = profit
        self.weight = weight

def greedyKnapsack (capacityOfSack, itemsArray):
    # Ratio based sorting of items 
    itemsArray.sort (key = lambda x : (x.profit/x.weight), reverse = True)
    # Greatest total profit holder
    greatestProfit = 0.0

    for item in itemsArray:
        # If adding is possible completely, add it 
        if item.weight <= capacityOfSack:
            capacityOfSack -= item.weight
            greatestProfit += item.profit
        # If adding entire item is not possible, add its fraction
        else:
            greatestProfit += item.profit * capacityOfSack / item.weight
            break
    return greatestProfit

if __name__ == '__main__':
    arr = [
        Item (10, 2), Item (5, 3), Item (15, 5), Item (7, 7), Item (6, 1), Item (18, 4), Item (3, 1) 
    ]

    maximumCapacityOfSack = 15

    outcome = greedyKnapsack (maximumCapacityOfSack, arr)
    print (f'The greatest profit that can be generated from sack is {outcome}')

# Time Complexity: O(N * log N)
# Auxiliary Space: O(N)
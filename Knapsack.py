def knapsack(capacity, weight, profit, n):
# n is the number of items in the store
    if n == 0 or capacity == 0:
        return 0
    elif weight[n-1] > capacity:       
        return knapsack(capacity, weight, profit, n-1)
    else:
        max_profit = max(profit[n-1] + knapsack(capacity - weight[n-1], weight, profit, n-1), knapsack(capacity, weight, profit, n-1))
        return max_profit
# capacity = 25
# weight = [24, 10, 10, 7]
# profit = [24, 18, 18, 10]
# no_of_items = len(weight)

# knapsack(capacity, weight, profit, no_of_items)


# This is an alternative to add more functionality to the program. It shouldn't be worried about
capacity = int(input("Enter the capacity of the bag: "))
weight = list(map(int,input("Enter the weights: ").split(" ")))
profit = list(map(int, input("Enter their corresponding profits: ").split(" ")))

n = len(weight)

result = knapsack(capacity, weight, profit, n)
print(f"The highest profit you can gain without exceeding the weight limit is {result}")


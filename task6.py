def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)
    selected_items = []
    total_cost = 0
    total_calories = 0

    for item, details in sorted_items:
        if total_cost + details["cost"] <= budget:
            selected_items.append(item)
            total_cost += details["cost"]
            total_calories += details["calories"]

    return selected_items, total_cost, total_calories

def dynamic_programming(items, budget):
    n = len(items)
    item_names = list(items.keys())
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        item = item_names[i - 1]
        cost = items[item]["cost"]
        calories = items[item]["calories"]
        for w in range(budget + 1):
            if cost <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost] + calories)
            else:
                dp[i][w] = dp[i - 1][w]

    w = budget
    selected_items = []

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(item_names[i - 1])
            w -= items[item_names[i - 1]]["cost"]

    return selected_items, dp[n][budget]

def main():
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }

    budget = 100

    # Жадібний алгоритм
    greedy_result, greedy_cost, greedy_calories = greedy_algorithm(items, budget)
    print("Greedy Algorithm Result:")
    print(f"Selected items: {greedy_result}")
    print(f"Total cost: {greedy_cost}")
    print(f"Total calories: {greedy_calories}")

    # Динамічне програмування
    dp_result, dp_calories = dynamic_programming(items, budget)
    print("\nDynamic Programming Result:")
    print(f"Selected items: {dp_result}")
    print(f"Total calories: {dp_calories}")

if __name__ == "__main__":
    main()

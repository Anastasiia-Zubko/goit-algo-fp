import random
import matplotlib.pyplot as plt

def simulate_dice_rolls(num_rolls):
    results = {i: 0 for i in range(2, 13)}

    for _ in range(num_rolls):
        roll_sum = random.randint(1, 6) + random.randint(1, 6)
        results[roll_sum] += 1

    probabilities = {sum_: count / num_rolls for sum_, count in results.items()}
    return probabilities

def plot_probabilities(simulated_probs, analytical_probs):
    sums = list(simulated_probs.keys())
    simulated = list(simulated_probs.values())
    analytical = list(analytical_probs.values())

    x = range(len(sums))
    plt.figure(figsize=(10, 5))
    plt.bar(x, simulated, width=0.4, label='Simulated', align='center')
    plt.bar(x, analytical, width=0.4, label='Analytical', align='edge')

    plt.xlabel('Sum of Dice Rolls')
    plt.ylabel('Probability')
    plt.title('Probability of Each Sum (Simulated vs. Analytical)')
    plt.xticks(x, sums)
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    num_rolls = 1000000
    simulated_probs = simulate_dice_rolls(num_rolls)

    analytical_probs = {
        2: 2.78 / 100,
        3: 5.56 / 100,
        4: 8.33 / 100,
        5: 11.11 / 100,
        6: 13.89 / 100,
        7: 16.67 / 100,
        8: 13.89 / 100,
        9: 11.11 / 100,
        10: 8.33 / 100,
        11: 5.56 / 100,
        12: 2.78 / 100,
    }

    print("Simulated Probabilities:")
    for sum_, prob in simulated_probs.items():
        print(f"Sum {sum_}: {prob:.2%}")

    plot_probabilities(simulated_probs, analytical_probs)

if __name__ == "__main__":
    main()

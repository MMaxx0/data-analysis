import random
import matplotlib.pyplot as plt


def run_session():
    session_data = {
        "player_balance": 100,
        "won_hands": 0,
        "went_bankrupt": False,
    }

    for _ in range(100):
        choice = random.choice(["win", "lose"])
        bet = 1

        if choice == "win":
            session_data["player_balance"] += bet
            session_data["won_hands"] += 1
        else:
            session_data["player_balance"] -= bet

        if session_data["player_balance"] <= 0:
            session_data["went_bankrupt"] = True
            break

    return session_data


def run_simulation(session_count=10000):
    total_won_hands = 0
    won_hands_counts = []
    total_bankruptcies = 0

    # Following the Binomial distribution
    n = 100  # sequence of n independent yes/no experiments
    p = 0.5  # Probability of yes
    expected_value = n * p
    variance = n * p * (1 - p)
    total_bankruptcy_probability = (1 - p) ** n

    for _ in range(session_count):
        session_stats = run_session()

        total_won_hands += session_stats["won_hands"]
        won_hands_counts.append(session_stats["won_hands"])

        if session_stats["went_bankrupt"]:
            total_bankruptcies += 1

    average_won_hands = total_won_hands / session_count

    mean = sum(won_hands_counts) / len(won_hands_counts)
    squared_diffs = [(x - mean) ** 2 for x in won_hands_counts]
    simulated_variance = sum(squared_diffs) / (len(won_hands_counts) - 1)

    print(f"Average won hands per session: {average_won_hands}")
    print(f"Simulated variance: {simulated_variance:.4f}")
    print(f"Total bankruptcies: {total_bankruptcies} out of {session_count} sessions")

    fig, axs = plt.subplots(2, 1, figsize=(12, 10))

    axs[0].bar(range(session_count), won_hands_counts, width=1)
    axs[0].set_xlabel("Session")
    axs[0].set_ylabel("Won Hands")
    axs[0].set_title("Won Hands per Session")
    theoretical_text = f"""**Theoretical Values**\nMean: {expected_value:.4f}\nVariance: {variance:.4f}\nBankruptcy probability (0.5^100): {total_bankruptcy_probability:.2e}"""
    simulated_text = f"""**Simulated Values**\nMean: {average_won_hands:.4f}\nVariance: {simulated_variance:.4f}\nBankruptcies: {total_bankruptcies}"""
    add_stats_box(axs[0], 0.98, 0.98, theoretical_text, "#e0e0ff", "navy")
    add_stats_box(axs[0], 0.80, 0.98, simulated_text, "#ffe0e0", "darkred")
    axs[1].hist(
        won_hands_counts, bins="auto", color="skyblue", edgecolor="black", alpha=0.7
    )
    axs[1].axvline(
        expected_value,
        color="red",
        linestyle="dashed",
        linewidth=2,
        label="Theoretical Mean",
    )
    std_dev = simulated_variance**0.5
    mean = average_won_hands
    axs[1].axvline(
        mean + std_dev,
        color="green",
        linestyle="dotted",
        linewidth=2,
        label="+1 Std Dev",
    )
    axs[1].axvline(
        mean - std_dev,
        color="green",
        linestyle="dotted",
        linewidth=2,
        label="-1 Std Dev",
    )
    axs[1].set_xlabel("Won Hands per Session")
    axs[1].set_ylabel("Number of Sessions")
    axs[1].set_title("Distribution of Won Hands per Session")
    axs[1].grid(axis="y", linestyle="--", alpha=0.7)
    axs[1].legend()
    add_stats_box(axs[1], 0.98, 0.98, theoretical_text, "#e0e0ff", "navy")
    add_stats_box(axs[1], 0.80, 0.98, simulated_text, "#ffe0e0", "darkred")
    plt.tight_layout()
    plt.show()


def add_stats_box(ax, x, y, text, color, edge):
    ax.text(
        x,
        y,
        text,
        transform=ax.transAxes,
        fontsize=10,
        va="top",
        ha="right",
        bbox=dict(boxstyle="round,pad=0.3", fc=color, ec=edge, lw=1),
    )


run_simulation()

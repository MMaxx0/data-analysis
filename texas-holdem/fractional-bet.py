import random
import matplotlib.pyplot as plt

session_length = 100  # Each session has 100 hands


def kelly_criterion(win_probability, win_proportion):
    bet_fraction = win_probability - ((1 - win_probability) / win_proportion)
    return bet_fraction


def run_session():
    session_data = {
        "player_balance": 100,
        "won_hands": 0,
        "went_bankrupt": False,
        "hands_played": 0,
    }

    win_probability = 0.5
    win_proportion = 2
    kelly_fraction = kelly_criterion(win_probability, win_proportion)

    for _ in range(session_length):
        choice = random.choice(["win", "lose"])
        bet = max(1, (kelly_fraction * session_data["player_balance"]))

        if choice == "win":
            session_data["player_balance"] += bet * win_proportion
            session_data["won_hands"] += 1
        else:
            session_data["player_balance"] -= bet

        session_data["hands_played"] += 1

        if session_data["player_balance"] < 1:
            session_data["went_bankrupt"] = True
            break

    return session_data


def run_simulation(count=10000):
    total_won_hands = 0
    total_hands_played = 0
    won_hands_per_session = []
    total_bankruptcies = 0

    for _ in range(count):
        session_stats = run_session()

        total_won_hands += session_stats["won_hands"]
        total_hands_played += session_stats["hands_played"]
        won_hands_per_session.append(session_stats["won_hands"])

        if session_stats["went_bankrupt"]:
            total_bankruptcies += 1

    # Following the Binomial distribution
    n = 100  # sequence of n independent yes/no experiments
    p = 0.5  # Probability of yes

    # Theoretical values
    theoretical_mean = n * p
    theoretical_variance = n * p * (1 - p)

    # Simulated values
    mean = (total_won_hands / total_hands_played) * 100
    sum_squared_deviations = sum((x - mean) ** 2 for x in won_hands_per_session)
    variance = sum_squared_deviations / (count - 1)

    print(f"Total hands played: {total_hands_played}")
    print(f"Total hands won: {total_won_hands}")
    print(f"Theoretical Mean: {theoretical_mean}")
    print(f"Theoretical Variance: {theoretical_variance}")
    print(f"Simulated Mean: {mean}")
    print(f"Simulated Variance: {variance}")
    print(f"Total bankruptcies: {total_bankruptcies} out of {count} sessions")

    fig, axs = plt.subplots(1, 1, figsize=(12, 10))

    axs.bar(range(count), won_hands_per_session, width=1)
    axs.set_xlabel("Session")
    axs.set_ylabel("Won Hands")
    axs.set_title("Won Hands per Session")
    general_stats_text = f"""**General Stats**\nTotal Hands Played: {total_hands_played}\nTotal Hands Won: {total_won_hands}\nTotal Bankruptcies: {total_bankruptcies}"""
    theoretical_text = f"""**Theoretical**\nMean: {theoretical_mean:.4f}\nVariance: {theoretical_variance:.4f}\n"""
    simulated_text = (
        f"""**Simulated**\nMean: {mean:.4f}\nVariance: {variance:.4f}\n"""
    )
    add_stats_box(axs, 0.20, 0.98, general_stats_text, "#e0ffe0", "green")
    add_stats_box(axs, 0.32, 0.98, theoretical_text, "#e0e0ff", "navy")
    add_stats_box(axs, 0.445, 0.98, simulated_text, "#ffe0e0", "darkred")
    plt.tight_layout()
    plt.show()

    # Plotting
    fig, axs = plt.subplots(1, 1, figsize=(12, 10))

    axs.hist(
        won_hands_per_session,
        bins="auto",
        color="skyblue",
        edgecolor="black",
        alpha=0.7,
    )
    per_session_std_dev = variance**0.5

    axs.axvline(
        theoretical_mean,
        color="red",
        linestyle="dashed",
        linewidth=2,
        label="Theoretical Mean",
    )
    axs.axvline(
        mean + per_session_std_dev,
        color="green",
        linestyle="dotted",
        linewidth=2,
        label="+1 Std Dev",
    )
    axs.axvline(
        mean - per_session_std_dev,
        color="green",
        linestyle="dotted",
        linewidth=2,
        label="-1 Std Dev",
    )
    axs.set_xlabel("Won Hands per Session")
    axs.set_ylabel("Number of Sessions")
    axs.set_title("Distribution of Won Hands per Session")
    axs.grid(axis="y", linestyle="--", alpha=0.7)
    axs.legend()

    general_stats_text = f"""**General Stats**\nTotal Hands Played: {total_hands_played}\nTotal Hands Won: {total_won_hands}\nTotal Bankruptcies: {total_bankruptcies}"""
    theoretical_per_session_text = f"""**Theoretical**\nMean: {theoretical_mean:.4f}\nVariance: {theoretical_variance:.4f}\n"""
    simulated_per_session_text = (
        f"""**Simulated**\nMean: {mean:.4f}\nVariance: {variance:.4f}\n"""
    )

    add_stats_box(axs, 0.20, 0.98, general_stats_text, "#e0ffe0", "green")
    add_stats_box(axs, 0.32, 0.98, simulated_per_session_text, "#ffe0e0", "darkred")
    add_stats_box(axs, 0.445, 0.98, theoretical_per_session_text, "#e0e0ff", "navy")
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

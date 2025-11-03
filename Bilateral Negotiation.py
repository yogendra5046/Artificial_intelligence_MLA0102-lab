import random

# --- Parameters ---
TOTAL_RESOURCE = 100
MAX_ROUNDS = 10

# Discount factors (0 < δ ≤ 1)
discount_A = 0.9
discount_B = 0.85

# Utility functions (can be customized)
def utility(agent_share, discount, round_num):
    """Utility decreases with delay (discount factor applied per round)."""
    return (agent_share) * (discount ** round_num)

# --- Negotiation Simulation ---
def bilateral_negotiation():
    round_num = 0
    agreement = None

    print("=== Bilateral Negotiation Simulation ===")
    print(f"Total Resource: {TOTAL_RESOURCE} units")
    print(f"Agent A Discount Factor (δA): {discount_A}")
    print(f"Agent B Discount Factor (δB): {discount_B}\n")

    while round_num < MAX_ROUNDS:
        round_num += 1
        print(f"--- Round {round_num} ---")

        if round_num % 2 == 1:
            # Agent A makes the offer
            offer_to_A = random.randint(40, 70)  # A keeps 40–70 units
            offer_to_B = TOTAL_RESOURCE - offer_to_A
            print(f"Agent A proposes: A={offer_to_A}, B={offer_to_B}")
            uA = utility(offer_to_A, discount_A, round_num)
            uB = utility(offer_to_B, discount_B, round_num)
            accept_threshold = utility(TOTAL_RESOURCE / 2, discount_B, round_num)
            if uB >= accept_threshold:
                print("Agent B accepts the offer!\n")
                agreement = (offer_to_A, offer_to_B, round_num)
                break
            else:
                print("Agent B rejects the offer.\n")

        else:
            # Agent B makes the offer
            offer_to_B = random.randint(40, 70)
            offer_to_A = TOTAL_RESOURCE - offer_to_B
            print(f"Agent B proposes: A={offer_to_A}, B={offer_to_B}")
            uA = utility(offer_to_A, discount_A, round_num)
            uB = utility(offer_to_B, discount_B, round_num)
            accept_threshold = utility(TOTAL_RESOURCE / 2, discount_A, round_num)
            if uA >= accept_threshold:
                print("Agent A accepts the offer!\n")
                agreement = (offer_to_A, offer_to_B, round_num)
                break
            else:
                print("Agent A rejects the offer.\n")

    # --- Outcome ---
    print("=== Negotiation Result ===")
    if agreement:
        offer_to_A, offer_to_B, rounds = agreement
        uA_final = utility(offer_to_A, discount_A, rounds)
        uB_final = utility(offer_to_B, discount_B, rounds)
        print(f"Agreement reached in Round {rounds}:")
        print(f"Agent A gets {offer_to_A} units, Agent B gets {offer_to_B} units.")
        print(f"Utility of Agent A: {uA_final:.2f}")
        print(f"Utility of Agent B: {uB_final:.2f}")

        # Check for Nash-like fairness (balanced utilities)
        diff = abs(uA_final - uB_final)
        if diff <= 5:
            print("✅ Result resembles a Nash-like fair outcome.")
        else:
            print("⚖️ Outcome favors one agent more than the other.")
    else:
        print("❌ No agreement reached after maximum rounds.")
        print("Both agents receive 0 utility.")
    print("========================================")

# --- Run Simulation ---
if __name__ == "__main__":
    bilateral_negotiation()

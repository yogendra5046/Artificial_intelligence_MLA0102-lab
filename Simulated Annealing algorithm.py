import random
import math

# --- Problem Setup ---

NUM_TASKS = 6
NUM_SLOTS = 3
SLOT_CAPACITY = 2  # each slot can handle up to 2 tasks

# Generate tasks (T1, T2, ... T6)
tasks = [f"T{i+1}" for i in range(NUM_TASKS)]

def random_schedule():
    """Generate a random assignment of tasks to time slots."""
    return [random.randint(0, NUM_SLOTS - 1) for _ in range(NUM_TASKS)]

def cost_function(schedule):
    """Compute the cost of a schedule.
       Penalize time slots that exceed capacity."""
    slot_counts = [0] * NUM_SLOTS
    for slot in schedule:
        slot_counts[slot] += 1

    # cost = number of excess tasks beyond capacity
    cost = sum(max(0, count - SLOT_CAPACITY) for count in slot_counts)
    return cost

def neighbor(schedule):
    """Generate a neighboring schedule by moving one task to a new random slot."""
    new_schedule = schedule.copy()
    task_to_move = random.randint(0, NUM_TASKS - 1)
    new_schedule[task_to_move] = random.randint(0, NUM_SLOTS - 1)
    return new_schedule

# --- Simulated Annealing Algorithm ---

def simulated_annealing(initial_temp=100.0, cooling_rate=0.95, min_temp=0.1, max_iterations=1000):
    current_schedule = random_schedule()
    current_cost = cost_function(current_schedule)

    best_schedule = current_schedule[:]
    best_cost = current_cost

    T = initial_temp

    iteration = 0
    while T > min_temp and iteration < max_iterations:
        new_schedule = neighbor(current_schedule)
        new_cost = cost_function(new_schedule)
        delta = new_cost - current_cost

        # Accept always if better; sometimes if worse
        if delta < 0 or random.random() < math.exp(-delta / T):
            current_schedule = new_schedule
            current_cost = new_cost

        # Track best found so far
        if current_cost < best_cost:
            best_schedule = current_schedule[:]
            best_cost = current_cost

        # Cooling
        T *= cooling_rate
        iteration += 1

    return best_schedule, best_cost


# --- Run the Algorithm ---

if __name__ == "__main__":
    best_schedule, best_cost = simulated_annealing()

    print("Tasks:", tasks)
    print("\nBest Schedule Found:")
    for i, slot in enumerate(best_schedule):
        print(f"{tasks[i]} → Slot {slot + 1}")

    print("\nBest Cost:", best_cost)
